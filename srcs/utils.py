import pyautogui
import time
import random
import math

from config import STOP_NEW
from config import STOP_THREAD
from config import SCREEN_SIZE

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
    if pyautogui.pixel(997, 927)[1] > 150: # do scroll
        if pyautogui.pixel(997, 1094)[1] > 150: count = 6
        elif pyautogui.pixel(997, 1067)[1] > 150: count = 7
        elif pyautogui.pixel(997, 1047)[1] > 150: count = 8
        elif pyautogui.pixel(997, 1034)[1] > 150: count = 9
        else: count = 10
    else:
        if pyautogui.pixel(509, 1119) > (150, 150, 150): count = 5
        elif pyautogui.pixel(509, 1072) > (150, 150, 150): count = 4
        elif pyautogui.pixel(509, 1026) > (150, 150, 150): count = 3
        elif pyautogui.pixel(509, 980) > (150, 150, 150): count = 2
        elif pyautogui.pixel(509, 932) > (150, 150, 150): count = 1
    return count

def get_count_etable():
    if pyautogui.pixel(997, 608)[1] > 150: return 9
    elif pyautogui.pixel(997, 547)[1] > 150: return 10
    elif pyautogui.pixel(997, 486)[1] > 150: return 11
    elif pyautogui.pixel(997, 425)[1] > 150: return 12
    elif pyautogui.pixel(997, 364)[1] > 150: return 13
    elif pyautogui.pixel(997, 303)[1] > 150: return 14

    if pyautogui.pixel(510, 633) > (150, 150, 150): return 8 #8 +48
    elif pyautogui.pixel(510, 585) > (150, 150, 150): return 7 #7 +49
    elif pyautogui.pixel(510, 538) > (150, 150, 150): return 6 #6 +48
    elif pyautogui.pixel(510, 490) > (150, 150, 150): return 5 #5 +49
    elif pyautogui.pixel(510, 442) > (150, 150, 150): return 4 #4 +48
    elif pyautogui.pixel(510, 396) > (150, 150, 150): return 3 #3 +49
    elif pyautogui.pixel(510, 348) > (150, 150, 150): return 2 #2 +48
    elif pyautogui.pixel(510, 300) > (150, 150, 150): return 1 #1
    else: return 0

def go_and_click(pos): # move mouse and left click
    pyautogui.moveTo(pos[0], pos[1], duration=0.1)
    time.sleep(random.uniform(0.2, 0.2))
    pyautogui.leftClick()
    time.sleep(random.uniform(0.5, 0.5))

def press_key(key): # press key
    pyautogui.press(key)
    time.sleep(random.uniform(0.2, 0.2))

def translate_pos(pos_x, pos_y):
    if (SCREEN_SIZE) == (2560, 1440):
        return (pos_x, pos_y)
    ratio_x = 1920 / 2560
    ratio_y = 1080 / 1440
    new_x = math.ceil(pos_x * ratio_x)
    new_y = math.ceil(pos_y * ratio_y)
    return (new_x, new_y)
