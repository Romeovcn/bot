import pyautogui
import time
import random

def move_items(type):

    # position of items inside
    position_item_etable = [[980, 529], [1027, 552],
                            [1026, 598], [884, 576], [933, 596]]
    
    # x and y by type
    if type == "ENDURANCE":
        x=850
        y=988
    elif type == "AMOUR":
        x=1075
        y=988
    elif type == "CARESSEUR":
        x=850
        y=1028
    elif type == "BAFFEUR":
        x=1075
        y=1028
    elif type == "MATURITE":
        x=850
        y=988
        # change page for items
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(1291, 1030, duration=0.1)
        time.sleep(random.uniform(0.75, 1))
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))
    elif type == "ENERGIE":
        x=1075
        y=988
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

def remove_items():
    # x, y
    first_click=[[886,566],[934,590],[1027,590], [1027,542],[980,520]] 
    # x, y
    second_click=[[936, 582],[985,608],[1074,608], [1073,559],[1027,539]]

    # loop remove items
    for i in range(0,5):
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(first_click[0+i][0], first_click[0+i][1], duration=0.1)
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))
        pyautogui.moveTo(second_click[0+i][0], second_click[0+i][1], duration=0.1)
        pyautogui.leftClick()
        time.sleep(random.uniform(0.75, 1))
   
if __name__ == "__main__":
    time.sleep(2)
    move_items("MATURITE")
    remove_items()
