import pyautogui
import keyboard
import random
import sys
import time
import threading

from srcs.main_bot import do_main_bot
from srcs.bot_seren_female import do_seren_female_bot
from srcs.bot_seren_male import do_seren_male_bot
from config import STOP_THREAD

def check_exit_thread(): # check bot exit thread loop
    while STOP_THREAD.is_set() == False:
        if keyboard.is_pressed("0"):
            STOP_THREAD.set()
        time.sleep(0.01)
    print("exit thread stopped")

def main_bot_thread(): # main bot thread loop
    do_main_bot("AMOUR")

if __name__ == "__main__":
    time.sleep(2)
    thread_1 = threading.Thread(target=check_exit_thread)
    thread_2 = threading.Thread(target=main_bot_thread)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Les deux threads ont été arrêtés.")