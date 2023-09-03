import time

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
def remove_items():

    first_click = [[1247, 792], [1185, 763], [1182, 648], [1309, 691], [1375, 728]] # x, y of items inside bonta stable
    second_click = [[1316, 807], [1250, 778], [1250, 665], [1374, 710], [1441, 742]] # x, y of button "remove item"

    # loop remove items
    for i in range(0, 5):
        go_and_click((first_click[i][0], first_click[i][1]))
        go_and_click((second_click[i][0], second_click[i][1]))

    # open inventory / put your inventory shortcut here
    # press_key('p')
    # for i in range(0, 5):
    #     j = 65
    #     k = 45
    #     go_and_click(x-j*i, y)
    #     go_and_click(x_drag_to+k*i, y_drag_to)
    
    # go_and_click(1584, 77)

if __name__ == "__main__":
    time.sleep(2)
    add_items("ENERGY")
    remove_items("ENERGY")
