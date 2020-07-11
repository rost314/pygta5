import logging
import time

import numpy as np
from PIL import ImageGrab

from scenario_automation.text_extraction import find_text


def wait_for_press_field_to_appear(search_texts):
    press_x_to_y_field = dict(x=470, y=35, w=600, h=40)
    while True:
        last_time = time.time()
        screen = grab_screen(**press_x_to_y_field)
        if find_text(screen, search_texts):
            break
        logging.info(f'Frame took {(time.time() - last_time) * 1000:.0f} ms')
    logging.info(f'Frame took {(time.time() - last_time) * 1000:.0f} ms')


def wait_for_confirm_field_to_appear(search_texts):
    lower_right_text_field = dict(x=2230, y=1400, w=650, h=30)
    while True:
        last_time = time.time()
        screen = grab_screen(**lower_right_text_field)
        if find_text(screen, search_texts):
            break
        logging.info(f'Frame took {(time.time() - last_time) * 1000:.0f} ms')
    logging.info(f'Frame took {(time.time() - last_time) * 1000:.0f} ms')


def grab_screen(x, y, w, h):
    screen = np.array(ImageGrab.grab(bbox=(x, y, x + w, y + h)))
    return screen