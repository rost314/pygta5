import time
import logging

from scenario_automation.activate_gta5_window import activate_gta5_window
from scenario_automation.send_gta5_keys import short_press_and_wait, short_press_key
from scenario_automation.grab_screen import wait_for_press_field_to_appear, wait_for_confirm_field_to_appear

wheel_outcome = [
    'T0',
    'RP2.5k',
    '$20k',
    'J10k',
    'D',
    'RP5k',
    '$30k',
    'J15k',
    'T1',
    'RP7.5k',
    'J20k',
    'M?',
    'T2',
    'RP10k',
    '$40k',
    'j25k',
    'T3',
    'RP15k',
    'V',
    '$50k'
 ]

# short_press_and_wait(key="return", wait=4.1)  # $20k
# short_press_and_wait(key="return", wait=4.6)  # RP7.5k
# short_press_and_wait(key="return", wait=5.0)  # j25k

# short_press_and_wait(key="return", wait=5.3)  # $50k
# short_press_and_wait(key="return", wait=5.35)  # RP15K
# short_press_and_wait(key="return", wait=5.32)  # j25k ??
# short_press_and_wait(key="return", wait=5.3)  # T2 ??
# short_press_and_wait(key="return", wait=5.3)  # J25 ??
# short_press_and_wait(key="return", wait=5.3)  # $50K
# short_press_and_wait(key="return", wait=5.31)  # M? ??
# short_press_and_wait(key="return", wait=5.3)  # RP15k
# short_press_and_wait(key="return", wait=5.3)  # RP2.5k
# short_press_and_wait(key="return", wait=5.3)  # $20k
# short_press_and_wait(key="return", wait=5.3)  # J15k

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        # datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.Formatter(fmt='%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d,%H:%M:%S')
    activate_gta5_window()
    # time.sleep(1)

    wait_for_press_field_to_appear(search_texts=['zu drehen'])
    short_press_key(key="e", jitter=False)

# not always there, need short timeout
#     wait_for_confirm_field_to_appear(search_texts=['Fortfahren'])
#     short_press_key(key="return", jitter=False)

    wait_for_press_field_to_appear(search_texts=['zu drehen'])
    logging.info('wait before pressing')
    # time.sleep(3.2)  # J25k
    # time.sleep(3.1)  # RP15k
    # time.sleep(3.05)  # T2 ohne Fortfahren
    # time.sleep(3.0)  # T3 mit Fortfahren
    # time.sleep(2.9)  # RP2.5k
    time.sleep(2.95)  # RP10k
    time.sleep(2.8)  #
    logging.info('pressing s')
    short_press_key(key="s", jitter=False)
