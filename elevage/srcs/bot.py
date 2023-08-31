import pyautogui
import time
import keyboard
import random
import sys

from srcs.utils import ft_sleep
from srcs.utils import remove_done_dd
from srcs.utils import get_count_enclos
from srcs.utils import get_count_etable

CONTINUE_THREAD = True
CONTINUE_BOT = True
ADD_NEW = True
#  + 2560

def do_main_bot():
    global CONTINUE_THREAD
    global CONTINUE_BOT
    global ADD_NEW
    count = 0
    key = "8"

    if ADD_NEW == True: add_new_dd()

    while CONTINUE_BOT and CONTINUE_THREAD:
        if ADD_NEW == True:
            if check_dd() == True: break
        else:
            count += check_last_dds()
            print(f"ADDED {count} last")
            if count >= 10: break
        pyautogui.press(key)
        key = "8" if key == "7" else "7"
    CONTINUE_THREAD = False

def check_last_dds():
    # put_filter()
    # count = get_count_enclos()
    # put_filter()
    # if ft_sleep(2, 2): return True # wait for done dd to pop
    # if pyautogui.pixel(509, 932) > (200, 200, 200):
    #     print("\033[32mDD DETECTED\033[0m")
    #     remove_done_dd()
    #     if ft_sleep(0.9, 0.9): return True
    #     return count
    # if ft_sleep(1.5, 1.5): return True
    # print(f".", end="")
    return count

def check_dd():    
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

def add_new_dd(): # total time = 0.6s
    global ADD_NEW
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
    print(f"count={count} new_count={new_count}")
    if new_count == 0 or new_count > count:
        ADD_NEW = False
        print("\033[31mStop to add new DD!\033[0m")