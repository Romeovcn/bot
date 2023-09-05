import pyautogui
import time
from srcs.utils import go_and_click
from srcs.utils import press_key
from srcs.utils import translate_pos

# always keep a special dd in etable for male / female
# order to up DD : FEMELLE -> POSITIVE -> AMOUR -> NEGATIVE -1100 -> ENDURANCE (-> MATURITE) -> ENERGIE 
#                  MALE -> NEGATIVE -> ENDURANCE -> POSITIVE +1100 -> AMOUR (-> MATURITE) -> ENERGIE

def set_filter_etable_female(type, is_first_cycle, is_maturity_cycle):
    if is_first_cycle == False: nbr_click = 4
    else: nbr_click = 5

    go_and_click(translate_pos(732, 153)) # open first filter
    press_key("backspace")
    press_key("t")
    
    press_key("backspace")
    for i in range(nbr_click): # number clicks on "m"
        press_key('m')
    go_and_click(translate_pos(477, 196)) # close first filter

    go_and_click(translate_pos(732, 201)) # open second filter
    press_key("backspace")
    press_key("t")

    if type == "AMOUR": nbr_click, key = 1, 'b'
    elif type == "ENDURANCE": nbr_click, key = 1, 'b'
    elif type == "ENERGIE": nbr_click, key = 1, 'b'
    elif type == "POSITIVE": nbr_click, key = 1, 's'
    elif type == "NEGATIVE": nbr_click, key = 2, 's' # PROBLEM MUST BE 2 THEN 1
    elif type == "MATURITE": nbr_click, key = 2, 'b'
    else: return print("WRONG GENDER ARG set_filter_etable")

    press_key("backspace")
    print(nbr_click)
    print(key)
    for i in range(nbr_click): # number clicks on key
        press_key(key)
    go_and_click(translate_pos(477, 196)) # close SECOND filter

def set_filter_etable_male(type, is_first_cycle, is_maturity_cycle):
    if STOP_THREAD.is_set(): return True
    if is_first_cycle == False: nbr_click = 3
    else: nbr_click = 4

    go_and_click(translate_pos(732, 153)) # open first filter
    press_key("backspace")
    press_key("t")
    
    press_key("backspace")
    for i in range(nbr_click): # number clicks on "m"
        press_key('m')
    go_and_click(translate_pos(477, 196)) # close first filter

    go_and_click(translate_pos(732, 201)) # open second filter
    press_key("backspace")
    press_key("t")

    if type == "AMOUR": nbr_click, key = 1, 'b'
    elif type == "ENDURANCE": nbr_click, key = 2, 'b'
    elif type == "ENERGIE": nbr_click, key = 1, 'b'
    elif type == "POSITIVE": nbr_click, key = 1, 's'
    elif type == "NEGATIVE": nbr_click, key = 2, 's' # PROBLEM MUST BE 2 THEN 1
    elif type == "MATURITE": nbr_click, key = 2, 'b'
    else: return print("WRONG GENDER ARG set_filter_etable")

    press_key("backspace")
    print(nbr_click)
    print(key)
    for i in range(nbr_click): # number clicks on key
        press_key(key)
    go_and_click(translate_pos(477, 196)) # close SECOND filter
    return False

def set_filter_enclos(type):
    key = "t"
    nbr_click=0

    go_and_click(translate_pos(902, 837))
    press_key("backspace")
    press_key(key)

    if type == "NONE": nbr_click = 0
    elif type == "AMOUR": nbr_click, key = 1, "a"
    elif type == "ENDURANCE": nbr_click, key = 1, "e"
    elif type == "ENERGIE": nbr_click, key = 2, "e"
    elif type == "POSITIVE": nbr_click, key = 1, "s"
    elif type == "NEGATIVE": nbr_click, key = 2, "s"
    else: print("WRONG TYPE ARG set_filter_enclos")
    
    press_key("backspace")
    for i in range(nbr_click):
        pyautogui.press(key)
        time.sleep(0.05)
    go_and_click(translate_pos(496, 830))
    return False