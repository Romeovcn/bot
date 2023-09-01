import pyautogui
import time
import random

from config import STOP_NEW
from config import STOP_THREAD

def ft_sleep(min_time_to_sleep, max_time_to_sleep):
    i = 0
    time_to_sleep = random.uniform(min_time_to_sleep, max_time_to_sleep)
    while i < 100:
        if STOP_THREAD.is_set():
            return True
        time.sleep(time_to_sleep / 100)
        i += 1

def add_new_dd(): # total time = 0.6s
    count = get_count_etable()

    pyautogui.moveTo(993, 151, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.moveTo(1153, 173, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.1)

    new_count = get_count_etable()
    if new_count == 0 or new_count > count:
        STOP_NEW.set()
        print(f"new_count={new_count} count={count}")
        print("\033[31mStop to add new DD!\033[0m")

def remove_done_dd(): # 0.6s
    time.sleep(0.1)
    pyautogui.moveTo(985, 831, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.moveTo(1152, 859, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()

def get_count_enclos():
    count = 0
    if pyautogui.pixel(997, 927)[1] > 200: # do scroll
        if pyautogui.pixel(997, 1094)[1] > 200: count = 6
        elif pyautogui.pixel(997, 1067)[1] > 200: count = 7
        elif pyautogui.pixel(997, 1047)[1] > 200: count = 8
        elif pyautogui.pixel(997, 1034)[1] > 200: count = 9
        else: count = 10
    else:
        if pyautogui.pixel(509, 1119) > (200, 200, 200): count = 5
        elif pyautogui.pixel(509, 1072) > (200, 200, 200): count = 4
        elif pyautogui.pixel(509, 1026) > (200, 200, 200): count = 3
        elif pyautogui.pixel(509, 980) > (200, 200, 200): count = 2
        elif pyautogui.pixel(509, 932) > (200, 200, 200): count = 1
    return count

def get_count_etable():
    if pyautogui.pixel(997, 602)[1] > 200: return 9
    elif pyautogui.pixel(997, 538)[1] > 200: return 10
    elif pyautogui.pixel(997, 474)[1] > 200: return 11
    elif pyautogui.pixel(997, 410)[1] > 200: return 12
    elif pyautogui.pixel(997, 346)[1] > 200: return 13
    elif pyautogui.pixel(997, 282)[1] > 200: return 14

    if pyautogui.pixel(510, 633) > (200, 200, 200): return 8 #8 +48
    elif pyautogui.pixel(510, 585) > (200, 200, 200): return 7 #7 +49
    elif pyautogui.pixel(510, 538) > (200, 200, 200): return 6 #6 +48
    elif pyautogui.pixel(510, 490) > (200, 200, 200): return 5 #5 +49
    elif pyautogui.pixel(510, 442) > (200, 200, 200): return 4 #4 +48
    elif pyautogui.pixel(510, 396) > (200, 200, 200): return 3 #3 +49
    elif pyautogui.pixel(510, 348) > (200, 200, 200): return 2 #2 +48
    elif pyautogui.pixel(510, 300) > (200, 200, 200): return 1 #1
    else: return 0

def go_and_click(pos_x, pos_y):
    # move mouse and left click
    pyautogui.moveTo(pos_x, pos_y, duration=0.1)
    time.sleep(random.uniform(0.1, 0.3))
    pyautogui.leftClick()
    time.sleep(random.uniform(0.1, 0.3))

def press_key(key):
    # press key
    pyautogui.press(key)
    time.sleep(random.uniform(0.075, 0.1))

