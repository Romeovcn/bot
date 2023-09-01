import pyautogui
import time
import random

from srcs.utils import go_and_click
from srcs.utils import press_key

# function to add items to stable
def add_items(type):

    # position of items inside (bonta stable)
    # follow schema to know indexes 
    # ------5X--------
    # -----1X-4X------
    # ----2X---3X-----
    position_item_etable = [[982, 532], [1034, 548], [889, 530], [889, 581], [938, 605]]

    # x and y by type in down inventory / order : page 1 -> endurance -> love -> caressor -> baffle / page 2 : maturity -> energy
    if type == "ENDURANCE":
        x = 850
        y = 988
    elif type == "LOVE":
        x = 1075
        y = 988
    elif type == "CARESSOR":
        x = 850
        y = 1028
    elif type == "BAFFLE":
        x = 1075
        y = 1028
    elif type == "MATURITY":
        x = 850
        y = 988
        # change page for items / click on down arrow
        go_and_click(1291, 1030)
    elif type == "ENERGY":
        x = 1075
        y = 988
        # change page for items / click on down arrow
        go_and_click(1291, 1030)

    # loop to place items inside
    for i in range(0, 5):
        j = 45
        go_and_click(x+j*i, y)
        go_and_click(position_item_etable[0+i][0], position_item_etable[0+i][1], duration=0.1)

# function to remove items
def remove_items(type):

    # x, y of items inside bonta stable
    first_click = [[889, 583], [934, 601], [1030, 552], [980, 531], [888, 529]]
    # x, y of button "remove item"
    second_click = [[930, 598], [968, 619], [
        1063, 562], [1022, 547], [930, 544]]

    # loop remove items
    for i in range(0, 5):
        go_and_click(first_click[0+i][0], first_click[0+i][1])
        go_and_click(second_click[0+i][0], second_click[0+i][1])

    # x and y by type on real inventory (five firsts items)
    x = 1544
    y = 210
    # x and y to drag on down inventory
    if type == "ENDURANCE":
        x_drag_to = 850
        y_drag_to = 988
    elif type == "LOVE":
        x_drag_to = 1075
        y_drag_to = 988
    elif type == "CARESSOR":
        x_drag_to = 850
        y_drag_to = 1028
    elif type == "BAFFLE":
        x_drag_to = 1075
        y_drag_to = 1028
    elif type == "MATURITY":
        x_drag_to = 850
        y_drag_to = 988
    elif type == "ENERGY":
        x_drag_to = 1075
        y_drag_to = 988

    # open inventory / put your inventory shortcut here
    press_key('p')
    for i in range(0, 5):
        j = 65
        k = 45
        go_and_click(x-j*i, y)
        go_and_click(x_drag_to+k*i, y_drag_to)
    
    go_and_click(1584, 77)

    # change page to back on starting page / click on up arrow 
    if type == "MATURITY":
        # change page for items
        go_and_click(1291, 985)
    elif type == "ENERGY":
        # change page for items
        go_and_click(1291, 985)

if __name__ == "__main__":
    time.sleep(2)
    add_items("ENERGY")
    remove_items("ENERGY")
