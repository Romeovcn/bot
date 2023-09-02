import pyautogui
import time
import keyboard
import threading
import random
import sys

from config import STOP_NEW
from config import STOP_THREAD
from srcs.utils import ft_sleep
from srcs.utils import add_new_dd

def do_maturity_bot(): # main bot thread loop
    global CONTINUE_THREAD
    key = "8"

    if STOP_NEW.is_set() == False: add_new_dd()
    while STOP_THREAD.is_set() == False:
        if check_dd() == True: break
        for i in range(10):
            if STOP_THREAD.is_set(): break
            pyautogui.press(key)
            key = "8" if key == "7" else "7"
            if ft_sleep(3.5, 3.5): STOP_THREAD.set()

    while STOP_THREAD.is_set() == False:
        if check_last_dds(): break
        pyautogui.press(key)
        key = "8" if key == "7" else "7"
        if ft_sleep(3.5, 3.5): STOP_THREAD.set()

    print("Stop 1 thread")

def check_dd():
    if STOP_NEW.is_set() == True: return True
    dd_removed = False

    pyautogui.moveTo(713, 937, duration=0.15)
    time.sleep(0.15)
    pyautogui.leftClick()
    time.sleep(0.5)

    for i in range(10):
        pyautogui.press("up")
        time.sleep(0.05)

    for i in range(10):
        if pyautogui.pixel(1375, 856)[1] > 150:
            pyautogui.press("1")
            dd_removed = True
            time.sleep(0.2)
        else:
            pyautogui.press("down")
            time.sleep(0.2)
    
    if dd_removed == True:
        add_new_dd()
    return False

def check_last_dds():
    if pyautogui.pixel(509, 934) < (200, 200, 200):
        print("\033[31mNo more DD stopping!\033[0m")
        return True

    pyautogui.moveTo(713, 937, duration=0.15)
    time.sleep(0.15)
    pyautogui.leftClick()
    time.sleep(0.5)

    for i in range(10):
        pyautogui.press("up")
        time.sleep(0.05)

    for i in range(10):
        if pyautogui.pixel(1375, 856)[1] > 150:
            pyautogui.press("1")
            time.sleep(0.2)
        else:
            pyautogui.press("down")
            time.sleep(0.2)
    return False