import time
import pyautogui
import random

from srcs.utils import go_and_click
from srcs.utils import press_key
from srcs.utils import translate_pos

def type_word(word):
    for char in word:
        pyautogui.press(char)
        time.sleep(0.1)

def right_click(pos): # move mouse and left click
    pyautogui.moveTo(pos[0], pos[1], duration=0.1)
    time.sleep(random.uniform(0.1, 0.1))
    pyautogui.rightClick()
    time.sleep(random.uniform(0.1, 0.1))

def add_items(type):
    position_item_etable = [(1188, 710), (1313, 709), (1374, 726), (1184, 769), (1245, 801)]

    if type == "ENDURANCE":
        item = "foudroyeur"
    elif type == "AMOURE":
        item = "dragofesse"
    elif type == "MATURITE":
        item = "abreuvoir"
    elif type == "POSITIVE":
        item = "caresseur"
    elif type == "NEGATIVE":
        item = "baffeur"
    elif type == "ENERGIE":
        item = "mangeoire"

    for i in position_item_etable:
        pyautogui.press("i")
        time.sleep(1)
        go_and_click(translate_pos(2292, 1324))
        time.sleep(1)
        type_word(item)
        time.sleep(1)
        right_click(translate_pos(2109, 491))
        time.sleep(1)
        go_and_click(translate_pos(2096, 505))
        time.sleep(1)
        go_and_click(i)
        time.sleep(1)
        print(i)

def remove_items(): # function to remove items
    first_click = [[1247, 792], [1185, 763], [1182, 648], [1309, 691], [1375, 728]] # x, y of items inside bonta stable
    second_click = [[1316, 807], [1250, 778], [1250, 665], [1374, 710], [1441, 742]] # x, y of button "remove item"

    for i in range(0, 5): # loop remove items
        go_and_click((first_click[i][0], first_click[i][1]))
        go_and_click((second_click[i][0], second_click[i][1]))

if __name__ == "__main__":
    time.sleep(2)
    add_items("ENERGY")
    remove_items("ENERGY")
