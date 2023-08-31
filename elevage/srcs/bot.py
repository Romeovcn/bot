import pyautogui
import time
import keyboard
import random
import sys

CONTINUE_THREAD = True
CONTINUE_BOT = True
ADD_NEW = True
#  + 2560

def check_exit_thread(): # check bot exit thread loop
    global CONTINUE_THREAD

    while CONTINUE_THREAD:
        if keyboard.is_pressed("0"):
            CONTINUE_THREAD = False
        time.sleep(0.01)
    print("exit thread stopped")

def main_bot_thread(): # main bot thread loop
    global CONTINUE_THREAD
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
    print("bot thread stopped")

def ft_sleep(min_time_to_sleep, max_time_to_sleep):
    i = 0
    time_to_sleep = random.uniform(min_time_to_sleep, max_time_to_sleep)
    while i < 100:
        if CONTINUE_THREAD == False:
            return True
        time.sleep(time_to_sleep / 100)
        i += 1

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

def check_last_dds():
    if ft_sleep(2, 2): return True # wait for done dd to pop
    count = get_count_enclos()
    if pyautogui.pixel(509, 932) > (200, 200, 200):
        print("\033[32mDD DETECTED\033[0m")
        remove_done_dd()
        if ft_sleep(0.9, 0.9): return True
        return count
    if ft_sleep(1.5, 1.5): return True
    print(f".", end="")
    return count

def remove_done_dd(): # 0.6s
    time.sleep(0.1)
    pyautogui.moveTo(985, 831, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.moveTo(1152, 859, duration=0.1)
    time.sleep(0.1)
    pyautogui.leftClick()

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

if __name__ == "__main__":
    time.sleep(2)

    thread_1 = threading.Thread(target=check_exit_thread)
    thread_2 = threading.Thread(target=main_bot_thread)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Les deux threads ont été arrêtés.")

    ETABLE: 0
    ENCLOS: 9