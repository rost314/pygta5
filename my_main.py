import cv2

from scenario_automation.send_gta5_keys import short_press_key
from scenario_automation.grab_screen import wait_for_press_field_to_appear


def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

# Fenstermodus 3434x1411
lower_right_text_field = dict(x=2230, y=1400, w=650, h=30)
online_loading_field = dict(x=2690, y=1400, w=220, h=30)


def main():
    wait_for_press_field_to_appear(search_texts=['Drücke', 'ins Bett zu gehen'])
    print('pressing e')
    short_press_key(key="e")


if __name__ == '__main__':
    main()
