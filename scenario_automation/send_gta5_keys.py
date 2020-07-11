from time import sleep
import random

from .activate_gta5_window import is_gta5_window
from keys import Keys

keys = Keys()


def press_key_for_duration(key, duration, jitter=True):
    # with active_gta5_window():
    if not is_gta5_window():
        return
    keys.directKey(key)
    if jitter:
        sleep(duration+random.random()/100)
    keys.directKey(key, keys.key_release)


def short_press_key(key, jitter=True):
    press_key_for_duration(key=key, duration=0.1, jitter=jitter)


def short_press_and_wait(key, wait, jitter=True):
    short_press_key(key=key, jitter=jitter)
    if wait:
        if jitter:
            wait = wait + random.random()/50
        sleep(wait)
