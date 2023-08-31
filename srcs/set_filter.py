import pyautogui
import time
import random

# order to up DD : female -----> caressor -> love -> baffle -> endurance -> energy /// male -----> baffle -> endurance -> caressor -> love -> energy
# always keep a special dd in etable for male / female

def set_filters_stable(gender, type, is_first_cycle):

    if gender == "FEMALE":
        nb_click = 4
    elif gender == "MALE":
        nb_click = 3

    if is_first_cycle == "NO":
        # click on first top searchbar
        pyautogui.moveTo(494, 112, duration=0.1)
        time.sleep(random.uniform(0.75, 1))
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))

        # 4 clicks on "m"
        for i in range(nb_click):
            pyautogui.press('m')
            time.sleep(0.5)

        # click on plus button
        pyautogui.moveTo(358, 115, duration=0.1)
        time.sleep(random.uniform(0.75, 1))
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))

        # click on second searchbar
        pyautogui.moveTo(507, 149, duration=0.1)
        time.sleep(random.uniform(0.75, 1))
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))

        if type == "ENERGY":
            nb_click = 3
            key = 'b'
        elif type == "LOVE":
            nb_click = 1
            key = 'b'
        elif type == "ENDURANCE":
            nb_click = 2
            key = 'b'
        elif type == "BAFFLE":
            nb_click = 1
            key = 's'
        elif type == "CARESSOR":
            nb_click = 2
            key = 's'

        # number clicks on key
        for i in range(nb_click):
            pyautogui.press(key)
            time.sleep(0.5)
    elif is_first_cycle == "YES":
        print("Pas encore codé")

       

def set_filter_enclos(type):
    pyautogui.moveTo(901, 837, duration=0.1)
    time.sleep(random.uniform(0.75, 1))
    pyautogui.leftClick()
    time.sleep(random.uniform(0.75, 1))
    pyautogui.leftClick()
    time.sleep(random.uniform(0.75, 1))

    for i in range(26):
        pyautogui.press('up')
        time.sleep(0.1)

    if type == "NONE":
        return
    elif type == "AMOUR":
        nbr_click = 15
    elif type == "ENDURANCE":
        nbr_click = 17
    elif type == "ENERGIE":
        nbr_click = 20
    elif type == "POSITIVE":
        nbr_click = 12
    elif type == "NEGATIVE":
        nbr_click = 13
    elif type == "MATURITE":
        nbr_click = 13
    
    for i in range(nbr_click):
        pyautogui.press('down')
        time.sleep(0.1)

if __name__ == "__main__":
    set_filter_enclos("LOVE")
    # set_filters_enclos("LOVE")
    # set_filters_enclos("NONE")