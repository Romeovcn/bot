import pyautogui
import time
import random

# order to up DD : female -----> caressor -> love -> baffle -> endurance -> energy /// male -----> baffle -> endurance -> caressor -> love -> energy
# always keep a special dd in etable for male / female

def set_filters_stable(gender, type, is_first_cycle):
    # if gender == "FEMALE":
    # else:

    if gender == "FEMALE":
        nb_click_female = 4
        if first == "NO":

            # click on first top searchbar
            time.sleep(random.uniform(0.75, 1))
            pyautogui.moveTo(494, 112, duration=0.1)
            time.sleep(random.uniform(0.75, 1))
            pyautogui.leftClick()
            time.sleep(random.uniform(0.75, 1))

            # 4 clicks on "m"
            for _ in range(nb_click_female):
                pyautogui.press('m')
                time.sleep(0.5)

            # click on first result
            time.sleep(random.uniform(0.75, 1))
            pyautogui.moveTo(506, 144, duration=0.1)
            time.sleep(random.uniform(0.75, 1))
            pyautogui.leftClick()

            # click on plus button
            time.sleep(random.uniform(0.75, 1))
            pyautogui.moveTo(358, 115, duration=0.1)
            time.sleep(random.uniform(0.75, 1))
            pyautogui.leftClick()

            # click on second searchbar
            time.sleep(random.uniform(0.75, 1))
            pyautogui.moveTo(507, 149, duration=0.1)
            time.sleep(random.uniform(0.75, 1))
            pyautogui.leftClick()

            if type == "ENERGY":
                nb_click = 3
                # 3 clicks on "b"
                for _ in range(nb_click):
                    pyautogui.press('b')
                    time.sleep(0.5)
            elif type == "LOVE":
                # 1 click on "b"
                pyautogui.press('b')
                time.sleep(0.5)
            elif type == "ENDURANCE":
                nb_click = 2
                # 2 clicks on "b"
                for _ in range(nb_click):
                    pyautogui.press('b')
                    time.sleep(0.5)
            elif type == "BAFFLE":
                # 1 click on "s"
                pyautogui.press('s')
                time.sleep(0.5)
            elif type == "CARESSOR":
                nb_click = 2
                # 2 clicks on "s"
                for _ in range(nb_click):
                    pyautogui.press('s')
                    time.sleep(0.5)

            # click on first result
            time.sleep(random.uniform(0.75, 1))
            pyautogui.moveTo(632, 595, duration=0.1)
            time.sleep(random.uniform(0.75, 1))
            pyautogui.leftClick()
        elif first == "YES":
            print("Pas encore codé")
    elif gender == "MALE":
        nb_click_male = 3
        if first == "NO":

            # click on first top searchbar
            time.sleep(random.uniform(0.75, 1))
            pyautogui.moveTo(494, 112, duration=0.1)
            time.sleep(random.uniform(0.75, 1))
            pyautogui.leftClick()
            time.sleep(random.uniform(0.75, 1))

            # 4 clicks on "m"
            for _ in range(nb_click_male):
                pyautogui.press('m')
                time.sleep(0.5)

            # click on first result
            time.sleep(random.uniform(0.75, 1))
            pyautogui.moveTo(506, 144, duration=0.1)
            time.sleep(random.uniform(0.75, 1))
            pyautogui.leftClick()

            # click on plus button
            time.sleep(random.uniform(0.75, 1))
            pyautogui.moveTo(358, 115, duration=0.1)
            time.sleep(random.uniform(0.75, 1))
            pyautogui.leftClick()

            # click on second searchbar
            time.sleep(random.uniform(0.75, 1))
            pyautogui.moveTo(507, 149, duration=0.1)
            time.sleep(random.uniform(0.75, 1))
            pyautogui.leftClick()

            if type == "ENERGY":
                nb_click = 3
                # 3 clicks on "b"
                for _ in range(nb_click):
                    pyautogui.press('b')
                    time.sleep(0.5)
            elif type == "LOVE":
                # 1 click on "b"
                pyautogui.press('b')
                time.sleep(0.5)
            elif type == "ENDURANCE":
                nb_click = 2
                # 2 clicks on "b"
                for _ in range(nb_click):
                    pyautogui.press('b')
                    time.sleep(0.5)
            elif type == "BAFFLE":
                # 1 click on "s"
                pyautogui.press('s')
                time.sleep(0.5)
            elif type == "CARESSOR":
                nb_click = 2
                # 2 clicks on "s"
                for _ in range(nb_click):
                    pyautogui.press('s')
                    time.sleep(0.5)
        elif first == "YES":
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