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
    while CONTINUE_THREAD:
        if keyboard.is_pressed("0"):
            CONTINUE_THREAD = False
        time.sleep(0.01)

def bot_thread(bot_mode): # main bot thread loop
    global CONTINUE_THREAD
    key = "8"
    last_nbr_etable = 0

    if bot_mode == "1":
        add_new_dd()
    while CONTINUE_THREAD:
        if (bot_mode == "2"):
            if ft_sleep(5, 5): return
        elif check_dd() == True: return
        pyautogui.press(key)
        key = "8" if key == "7" else "7"

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

    time.sleep(0.5)
    if (pyautogui.pixel(510, 932) == (255, 255, 255)):
        print("\033[32mDD DETECTED\033[0m")
        remove_done_dd()
        if ADD_NEW:
            add_new_dd()
        else:
            time.sleep(0.5)
        if ft_sleep(1, 1): return True
    else:
        if ft_sleep(2.8, 2.8):
            return True
        print(f".", end="")
    return False

def remove_done_dd():
    time.sleep(0.1)
    pyautogui.moveTo(985, 831, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.moveTo(1152, 859, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()

def check_last_nbr_etable():
    global ADD_NEW
    global LAST_NBR_ETABLE
    i = 0
    
    if pyautogui.pixel(509, 252) > (200, 200, 200): i += 1 #1
    if pyautogui.pixel(509, 300) > (200, 200, 200): i += 1 #2 +48
    if pyautogui.pixel(509, 349) > (200, 200, 200): i += 1 #3 +49
    if pyautogui.pixel(509, 397) > (200, 200, 200): i += 1 #4 +48
    if pyautogui.pixel(509, 446) > (200, 200, 200): i += 1 #5 +49
    if pyautogui.pixel(509, 494) > (200, 200, 200): i += 1 #6 +48
    if pyautogui.pixel(509, 543) > (200, 200, 200): i += 1 #7 +49
    if pyautogui.pixel(509, 591) > (200, 200, 200): i += 1 #8 +48
    if pyautogui.pixel(509, 640) > (200, 200, 200): i += 1 #9 +49
    if i == 0 or i > LAST_NBR_ETABLE:
        ADD_NEW = False
        print("\033[31mStop to add new DD!\033[0m")
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
    if len(sys.argv) < 2:
        print("Veuillez choisir un des modes ci-dessous:")
        print("1 - Mode normal avec transfert auto")
        print("2 - Mode sans transfert auto")
        sys.exit(1)
    if sys.argv[1] != "1" and sys.argv[1] != "2":
        print("Veuillez choisir un mode entre 1 et 2")
        sys.exit(1)

    bot_mode = sys.argv[1]
    time.sleep(2)
    thread_1 = threading.Thread(target=check_exit_thread)
    thread_2 = threading.Thread(target=bot_thread, args=bot_mode)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Les deux threads ont été arrêtés.")