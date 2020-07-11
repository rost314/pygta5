import random
from time import sleep

from scenario_automation.activate_gta5_window import activate_gta5_window
from scenario_automation.send_gta5_keys import short_press_and_wait

if __name__ == '__main__':
    activate_gta5_window()
    sleep(1)
    short_press_and_wait(key='e', wait=1)

    i = 0
    rand_key = random.choice(['w', 'a', 's', 'd'])
    while True:
        i = (i + 1) % 4
        if i == 0:
            rand_key = random.choice(['w', 'a', 's', 'd'])
        short_press_and_wait(key=rand_key, wait=0)
        short_press_and_wait(key='space', wait=0.46)
