import pyautogui
import time
import random

def ft_sleep(min_time_to_sleep, max_time_to_sleep):
    i = 0
    time_to_sleep = random.uniform(min_time_to_sleep, max_time_to_sleep)
    while i < 100:
        if CONTINUE_THREAD == False:
            return True
        time.sleep(time_to_sleep / 100)
        i += 1

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
    if pyautogui.pixel(997, 602)[1] > 200: return 10
    elif pyautogui.pixel(997, 530)[1] > 200: return 11
    elif pyautogui.pixel(997, 458)[1] > 200: return 12
    elif pyautogui.pixel(997, 386)[1] > 200: return 13
    elif pyautogui.pixel(997, 314)[1] > 200: return 14
    elif pyautogui.pixel(997, 242)[1] > 200: return 15

    if pyautogui.pixel(510, 640) > (200, 200, 200): return 9 #9 +49
    elif pyautogui.pixel(510, 591) > (200, 200, 200): return 8 #8 +48
    elif pyautogui.pixel(510, 543) > (200, 200, 200): return 7 #7 +49
    elif pyautogui.pixel(510, 494) > (200, 200, 200): return 6 #6 +48
    elif pyautogui.pixel(510, 446) > (200, 200, 200): return 5 #5 +49
    elif pyautogui.pixel(510, 397) > (200, 200, 200): return 4 #4 +48
    elif pyautogui.pixel(510, 349) > (200, 200, 200): return 3 #3 +49
    elif pyautogui.pixel(510, 300) > (200, 200, 200): return 2 #2 +48
    elif pyautogui.pixel(510, 252) > (200, 200, 200): return 1 #1
    else: return 0