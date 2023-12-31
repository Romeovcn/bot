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

#  + 2560

def do_seren_female_bot():
    key = "8"

    if STOP_NEW.is_set() == False: add_new_dd()
    while STOP_THREAD.is_set() == False:
        if check_dd() == True: break
        pyautogui.press(key)
        key = "8" if key == "7" else "7"
    
    STOP_THREAD.set()
    print("Stop 1 thread")

def check_dd():
    dd_removed = False

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
        if pyautogui.pixel(1271, 998)[1] < 100:
            pyautogui.press("1")
            dd_removed = True
            time.sleep(0.2)
        else:
            pyautogui.press("down")
            time.sleep(0.2)
    
    if STOP_NEW.is_set() == False and dd_removed == True:
        add_new_dd()
    return False