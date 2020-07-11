from contextlib import contextmanager
from time import sleep

import win32gui
import pywintypes
from functools import lru_cache


def window_enumeration_handler(window_handle, top_windows):
    top_windows.append((window_handle, win32gui.GetWindowText(window_handle)))


def current_window_title():
    foreground = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    return foreground


def is_gta5_window():
    return current_window_title() == 'Grand Theft Auto V'


@lru_cache()
def gta5_window_handle():
    top_windows = []
    win32gui.EnumWindows(window_enumeration_handler, top_windows)
    for window_handle, window_title in top_windows:
        if 'Grand Theft Auto V' == window_title:
            print('found GTA5 window')
            return window_handle


def activate_gta5_window():
    window_handle = gta5_window_handle()
    if window_handle:
        win32gui.ShowWindow(window_handle, 5)
        win32gui.SetForegroundWindow(window_handle)


@contextmanager
def active_gta5_window():
    current_handle = win32gui.GetForegroundWindow()
    gta5_handle = gta5_window_handle()
    if current_handle and current_handle != gta5_handle:
        print(win32gui.GetWindowText(current_handle))
        activate_gta5_window()
        sleep(0.01)
    yield
    if current_handle and current_handle != gta5_handle:
        try:
            win32gui.ShowWindow(current_handle, 5)
            win32gui.SetForegroundWindow(current_handle)
        except pywintypes.error as e:
            #print(e)
            print(current_handle)


if __name__ == "__main__":
    activate_gta5_window()
