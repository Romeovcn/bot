import pyautogui
import time
from utils import go_and_click
from utils import press_key

# order to up DD : female -----> caressor -> love -> baffle -> endurance -> energy /// male -----> baffle -> endurance -> caressor -> love -> energy
# always keep a special dd in etable for male / female
def set_filters_stable(gender, type, is_first_cycle):
    if is_first_cycle == "NO":
        nb_click = 0
        if gender == "FEMALE":
            nb_click = 4
        else:
            nb_click = 3

        #  click on first top filterbar
        go_and_click(494, 112)

        # number clicks on "m"
        for i in range(nb_click):
            press_key('m')

        # click on plus button
        go_and_click(358, 115)

        # click on second searchbar
        go_and_click(507, 149)

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
        else:
            nb_click = 2
            key = 's'

        # number clicks on key
        for i in range(nb_click):
            press_key(key)
    elif is_first_cycle == "YES":
        print("Pas encore codé")

def set_filter_enclos(type):
    nbr_click=0
    # click on bot filterbar
    go_and_click(512, 627)

    for i in range(26):
        press_key('up')

    if type == "NONE":
        return
    elif type == "AMOUR":
        nbr_click = 16
    elif type == "ENDURANCE":
        nbr_click = 18
    elif type == "ENERGIE":
        nbr_click = 20
    elif type == "POSITIVE":
        nbr_click = 12
    elif type == "NEGATIVE":
        nbr_click = 13
    elif type == "MATURITE":
        nbr_click = 13
    
    for i in range(nbr_click):
        press_key('down')

if __name__ == "__main__":
    time.sleep(3)
    set_filters_stable("MALE", "CARESSOR", "NO")
    set_filter_enclos("POSITIVE")