import pyautogui
import time
import keyboard
import random
import sys

from srcs.utils import ft_sleep
from srcs.utils import remove_done_dd
from srcs.utils import add_new_dd
from srcs.utils import get_count_enclos
from srcs.set_filter import set_filter_enclos
from config import STOP_THREAD
from config import STOP_NEW

#  + 2560

def do_main_bot(bot_mode):
    count = 0
    key = "8"

    if STOP_NEW.is_set() == False: add_new_dd()
    while STOP_THREAD.is_set() == False:
        print("ok")
        if check_dd() == True: break
        pyautogui.press(key)
        key = "8" if key == "7" else "7"

    set_filter_enclos("NONE")
    enclos_count = get_count_enclos()
    set_filter_enclos(bot_mode)

    while STOP_THREAD.is_set() == False:
        count += check_last_dds()
        if count >= enclos_count: break
        pyautogui.press(key)
        key = "8" if key == "7" else "7"
    
    STOP_THREAD.set()

def check_last_dds():
    if ft_sleep(2, 2): return 20 # wait for done dd to pop
    if pyautogui.pixel(509, 932) > (200, 200, 200):
        print("\033[32mLAST DD DETECTED\033[0m")
        count = get_count_enclos()
        remove_done_dd()
        if ft_sleep(0.9, 0.9): return 20
        return count
    if ft_sleep(1.5, 1.5): return 20
    print(f".", end="")
    return 0

def check_dd():
    if STOP_NEW.is_set() == True: return True

    if ft_sleep(2, 2): return True # wait for done dd to pop
    if pyautogui.pixel(510, 932) > (200, 200, 200):
        print("\033[32mDD DETECTED\033[0m")
        remove_done_dd()
        add_new_dd()
        if ft_sleep(0.3, 0.3): return True
        return False
    if ft_sleep(1.5, 1.5): return True
    print(f".", end="")
    return False