import pyautogui
import time
import keyboard
import threading
import random
import sys

CONTINUE_THREAD = True
ADD_NEW = True
LAST_NBR_ETABLE = 9
#  + 2560

def check_exit_thread(): # check bot exit thread loop
    global CONTINUE_THREAD

    while CONTINUE_THREAD == True:
        if keyboard.is_pressed("0"):
            CONTINUE_THREAD = False
        time.sleep(0.01)
    print("Stop 2 thread")

def bot_thread(): # main bot thread loop
    global CONTINUE_THREAD
    key = "8"

    add_new_dd()
    while CONTINUE_THREAD == True:
        pyautogui.press(key)
        if check_dd() == True: 
            CONTINUE_THREAD = False
        key = "8" if key == "7" else "7"
    print("Stop 1 thread")

def ft_sleep(min_time_to_sleep, max_time_to_sleep):
    i = 0
    time_to_sleep = random.uniform(min_time_to_sleep, max_time_to_sleep)
    while i < 100:
        if CONTINUE_THREAD == False:
            return True
        time.sleep(time_to_sleep / 100)
        i += 1

def check_dd():
    global ADD_NEW
    dd_removed = False

    if pyautogui.pixel(509, 934) != (255, 255, 255): # if there is no more DD stop the prog
        print("NO MORE DD STOP PROG")
        return True
    pyautogui.moveTo(713, 937, duration=0.15)
    time.sleep(0.15)
    pyautogui.leftClick()
    time.sleep(0.5)
    for i in range(0, 10):
        print(i)
        pyautogui.press("up")
        time.sleep(0.05)
    for i in range(0, 10):
        pixel_checked = pyautogui.pixel(1309, 998)[1]
        print(f"checking dd nbr {i}: pixel color = {pixel_checked}")
        if pixel_checked > 100:
            pyautogui.press("1")
            dd_removed = True
            time.sleep(0.2)
        else:
            pyautogui.press("down")
            time.sleep(0.2)
    if ADD_NEW == True and dd_removed == True:
        add_new_dd()


def check_last_nbr_etable():
    global ADD_NEW
    global LAST_NBR_ETABLE
    i = 0

    if (pyautogui.pixel(511, 252) == (255, 255, 255)): i += 1
    if (pyautogui.pixel(511, 252 + 47 * 1) == (255, 255, 255)): i += 1
    if (pyautogui.pixel(511, 252 + 47 * 2) == (255, 255, 255)): i += 1
    if (pyautogui.pixel(511, 252 + 47 * 3) == (255, 255, 255)): i += 1
    if (pyautogui.pixel(511, 252 + 47 * 4) == (255, 255, 255)): i += 1
    if (pyautogui.pixel(511, 252 + 47 * 5) == (255, 255, 255)): i += 1
    if (pyautogui.pixel(511, 252 + 47 * 6) == (255, 255, 255)): i += 1
    if (pyautogui.pixel(511, 252 + 47 * 7) == (255, 255, 255)): i += 1
    if (pyautogui.pixel(511, 252 + 47 * 8) == (255, 255, 255)): i += 1
    if i == 0 or i > LAST_NBR_ETABLE:
        ADD_NEW = False
        print("STOP TO ADD NEW")
        return True
    LAST_NBR_ETABLE = i
    return False

def add_new_dd():
    if check_last_nbr_etable(): return

    time.sleep(0.1)
    pyautogui.moveTo(993, 151, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.moveTo(1153, 173, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()

if __name__ == "__main__":
    time.sleep(2)
    thread_1 = threading.Thread(target=check_exit_thread)
    thread_2 = threading.Thread(target=bot_thread)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Les deux threads ont été arrêtés.")