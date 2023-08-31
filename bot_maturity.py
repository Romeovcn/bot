import pyautogui
import time
import keyboard
import threading
import random

CONTINUE_THREAD = True
ADD_NEW = True
LAST_NBR_ETABLE = 9
#  + 2560

def check_exit_thread():  # check bot exit thread loop
    global CONTINUE_THREAD

    while CONTINUE_THREAD == True:
        if keyboard.is_pressed("0"):
            CONTINUE_THREAD = False
        time.sleep(0.01)
    print("Stop 2 thread")

def bot_thread():  # main bot thread loop
    global CONTINUE_THREAD
    key = "8"

    add_new_dd()
    while CONTINUE_THREAD:
        for i in range(0, 10):
            if CONTINUE_THREAD == False:
                break
            pyautogui.press(key)
            if ft_sleep(3.5, 3.5):
                CONTINUE_THREAD = False
            key = "8" if key == "7" else "7"
        remove_done_dd()
        add_new_dd()
    print("Stop 1 thread")


def ft_sleep(min_time_to_sleep, max_time_to_sleep):
    i = 0
    time_to_sleep = random.uniform(min_time_to_sleep, max_time_to_sleep)
    while i < 100:
        if CONTINUE_THREAD == False:
            return True
        time.sleep(time_to_sleep / 100)
        i += 1


def remove_done_dd():
    time.sleep(0.1)
    pyautogui.moveTo(985, 831, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.moveTo(1152, 859, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()


def add_new_dd():
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
