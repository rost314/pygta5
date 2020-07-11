import logging
import os
import time

from pytesseract import Output
import pytesseract
import cv2


def crop(image, x, y, w, h):
    return image[y:y+h, x:x+w]


def cv2_show_image(window_name, image,
                   size_wh=None, location_xy=None):
    """Helper function for specifying window size and location when
    displaying images with cv2.

    Args:
        window_name: str window name
        image: ndarray image to display
        size_wh: window size (w, h)
        location_xy: window location (x, y)
    """

    if size_wh is not None:
        cv2.namedWindow(window_name,
                        cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_NORMAL)
        cv2.resizeWindow(window_name, *size_wh)
    else:
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    if location_xy is not None:
        cv2.moveWindow(window_name, *location_xy)

    cv2.imshow(window_name, image)


def find_text(image, search_strings, min_conf=20):
    os.environ['OMP_THREAD_LIMIT'] = '1'
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image, 250, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # image = cv2.GaussianBlur(image, (3, 3), 0)
    results = pytesseract.image_to_data(image, output_type=Output.DICT, lang='deu', config='--psm 6')
    conf_results = [(text, conf, x, y, w, h) for (text, conf, x, y, w, h) in
                    zip(results['text'], map(int, results['conf']),
                        results['left'], results['top'], results['width'], results['height'])
                    if conf > min_conf]

    confident_text = ' '.join(list(zip(*conf_results))[0]) if conf_results else ''
    logging.info(f'extracted text: "{confident_text}"')

    # loop over each of the individual text localizations
    for text, conf, x, y, w, h in conf_results:
        # display the confidence and text to our terminal
        logging.debug("Confidence: {}".format(conf))
        logging.debug("Text: {}".format(text))
        # strip out non-ASCII text so we can draw the text on taaahe image
        # using OpenCV, then draw a bounding box around the text along
        # with the text itself
        # text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    found = all(search_string in confident_text for search_string in search_strings)
    logging.info(f"'{search_strings}' contained in image: {found}")
    # show the output image
    cv2_show_image("Image", image, location_xy=(3500, 200))
    # cv2.waitKey(0)
    return found


def main():
    image_path = r'D:\Bilder\Screenshots\Screenshot_press_s.png'

    img = cv2.imread(image_path)
    # img = crop(img, x=480, y=20, w=350, h=100)
    press_x_to_y_field = dict(x=470, y=35, w=500, h=40)
    img = crop(img, **press_x_to_y_field)
    search_string = 'um zu drehen'

    last_time = time.time()
    found_text = find_text(img, search_string)
    print(f'Frame took {(time.time() - last_time) * 1000:.0f} ms')


if __name__ == '__main__':
    import timeit
    main()
    # timeit.timeit(main, number=10)
