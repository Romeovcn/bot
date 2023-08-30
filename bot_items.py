import pyautogui
import time
import random

# function to open stable window
def open_window():
    # click to open window
    time.sleep(random.uniform(1.5, 2.5))
    pyautogui.moveTo(1023, 589, duration=0.1)
    time.sleep(random.uniform(1.5, 2.5))
    pyautogui.leftClick()
    time.sleep(random.uniform(1.5, 2.5))

# function to close stable window
def close_window():
    # click to close window
    time.sleep(random.uniform(1.5, 2.5))
    pyautogui.moveTo(1579, 69, duration=0.1)
    time.sleep(random.uniform(1.5, 2.5))
    pyautogui.leftClick()
    time.sleep(random.uniform(1.5, 2.5))

# function to add items to stable
def add_items(type):

    # position of items inside
    position_item_etable = [[982, 532], [1034, 548],
                            [889, 530], [889, 581], [938, 605]]

    # x and y by type
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
        # change page for items
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(1291, 1030, duration=0.1)
        time.sleep(random.uniform(0.75, 1))
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))
    elif type == "ENERGY":
        x = 1075
        y = 988
        # change page for items
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(1291, 1030, duration=0.1)
        time.sleep(random.uniform(0.75, 1))
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))

    # loop to place items inside
    for i in range(0, 5):
        j = 45
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(x+j*i, y, duration=0.1)
        time.sleep(random.uniform(0.75, 1))
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(
            position_item_etable[0+i][0], position_item_etable[0+i][1], duration=0.1)
        time.sleep(random.uniform(0.75, 1))
        pyautogui.leftClick()

# function to remove items
def remove_items(type):

    # x, y
    first_click = [[889, 583], [934, 601], [1030, 552], [980, 531], [888, 529]]
    # x, y
    second_click = [[930, 598], [968, 619], [
        1063, 562], [1022, 547], [930, 544]]

    # loop remove items
    for i in range(0, 5):
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(first_click[0+i][0],
                         first_click[0+i][1], duration=0.1)
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(second_click[0+i][0],
                         second_click[0+i][1], duration=0.1)
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))

    # x and y by type
    x = 1544
    y = 210
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

    # open inventory
    pyautogui.press('p', interval=0.5)

    for i in range(0, 5):
        j = 65
        k = 45
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(x-j*i, y, duration=0.1)
        time.sleep(random.uniform(0.75, 1))
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))
        pyautogui.dragTo(x_drag_to+k*i, y_drag_to, duration=1)
        time.sleep(random.uniform(0.75, 1))

    time.sleep(random.uniform(0.75, 1))
    pyautogui.moveTo(1584, 77, duration=0.1)
    time.sleep(random.uniform(0.75, 1))
    pyautogui.leftClick()

    # change page to back on starting page
    if type == "MATURITY":
        # change page for items
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(1291, 985, duration=0.1)
        time.sleep(random.uniform(0.75, 1))
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))
    elif type == "ENERGY":
        # change page for items
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(1291, 985, duration=0.1)
        time.sleep(random.uniform(0.75, 1))
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))

# order to up DD : female and male : energy -> female : love - serenity - endurance -> male : endurance - serenity - love
# always keep a special dd in stable for male / female
# def searchbar(type, first, gender):
#     if first == "NON" and type == "ENERGY" and gender == "FEMALE":



if __name__ == "__main__":
    time.sleep(2)
    add_items("ENERGY")
    open_window()
    close_window()
    remove_items("ENERGY")
