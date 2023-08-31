import pyautogui
import time
import random

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

# order to up DD : female -----> energy -> caressor -> love -> baffle -> endurance /// male -----> energy -> baffle -> endurance -> caressor -> love
# always keep a special dd in stable for male / female


def filters(type, first, gender):
    if gender == "FEMALE":
        nb_click_female = 4
        if first == "NON":

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
                # click on bot searchbar
                time.sleep(random.uniform(0.75, 1))
                pyautogui.moveTo(515, 629, duration=0.1)
                time.sleep(random.uniform(0.75, 1))
                pyautogui.leftClick()

                nb_click_bot = 2
                # 2 clicks on "e"
                for _ in range(nb_click_bot):
                    pyautogui.press('e')
                    time.sleep(0.5)
            elif type == "LOVE":
                # 1 click on "b"
                pyautogui.press('b')
                time.sleep(0.5)
                # click on bot searchbar
                time.sleep(random.uniform(0.75, 1))
                pyautogui.moveTo(515, 629, duration=0.1)
                time.sleep(random.uniform(0.75, 1))
                pyautogui.leftClick()

                # 1 click on "a"
                pyautogui.press('a')
                time.sleep(0.5)
            elif type == "ENDURANCE":
                nb_click = 2
                # 2 clicks on "b"
                for _ in range(nb_click):
                    pyautogui.press('b')
                    time.sleep(0.5)
                # click on bot searchbar
                time.sleep(random.uniform(0.75, 1))
                pyautogui.moveTo(515, 629, duration=0.1)
                time.sleep(random.uniform(0.75, 1))
                pyautogui.leftClick()

                # 1 click on "e"
                pyautogui.press('e')
                time.sleep(0.5)
            elif type == "BAFFLE":
                # 1 click on "s"
                pyautogui.press('s')
                time.sleep(0.5)

                # click on bot searchbar
                time.sleep(random.uniform(0.75, 1))
                pyautogui.moveTo(515, 629, duration=0.1)
                time.sleep(random.uniform(0.75, 1))
                pyautogui.leftClick()

                nb_click_bot = 2
                # 2 clicks on "s"
                for _ in range(nb_click_bot):
                    pyautogui.press('s')
                    time.sleep(0.5)
            elif type == "CARESSOR":
                nb_click = 2
                # 2 clicks on "s"
                for _ in range(nb_click):
                    pyautogui.press('s')
                    time.sleep(0.5)
                # click on bot searchbar
                time.sleep(random.uniform(0.75, 1))
                pyautogui.moveTo(515, 629, duration=0.1)
                time.sleep(random.uniform(0.75, 1))
                pyautogui.leftClick()

                # 1 click on "s"
                pyautogui.press('s')
                time.sleep(0.5)

            # click on first result
            time.sleep(random.uniform(0.75, 1))
            pyautogui.moveTo(632, 595, duration=0.1)
            time.sleep(random.uniform(0.75, 1))
            pyautogui.leftClick()
        elif first == "OUI":
            print("Pas encore codé")
    elif gender == "MALE":
        nb_click_male = 3
        if first == "NON":

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
                # click on bot searchbar
                time.sleep(random.uniform(0.75, 1))
                pyautogui.moveTo(515, 629, duration=0.1)
                time.sleep(random.uniform(0.75, 1))
                pyautogui.leftClick()

                nb_click_bot = 2
                # 2 clicks on "e"
                for _ in range(nb_click_bot):
                    pyautogui.press('e')
                    time.sleep(0.5)
            elif type == "LOVE":
                # 1 click on "b"
                pyautogui.press('b')
                time.sleep(0.5)
                # click on bot searchbar
                time.sleep(random.uniform(0.75, 1))
                pyautogui.moveTo(515, 629, duration=0.1)
                time.sleep(random.uniform(0.75, 1))
                pyautogui.leftClick()
                # 1 click on "a"
                pyautogui.press('a')
                time.sleep(0.5)
            elif type == "ENDURANCE":
                nb_click = 2
                # 2 clicks on "b"
                for _ in range(nb_click):
                    pyautogui.press('b')
                    time.sleep(0.5)
                # click on bot searchbar
                time.sleep(random.uniform(0.75, 1))
                pyautogui.moveTo(515, 629, duration=0.1)
                time.sleep(random.uniform(0.75, 1))
                pyautogui.leftClick()
                # click 1 time on "e"
                pyautogui.press('e')
                time.sleep(0.5)
            elif type == "BAFFLE":
                # 1 click on "s"
                pyautogui.press('s')
                time.sleep(0.5)
                # click on bot searchbar
                time.sleep(random.uniform(0.75, 1))
                pyautogui.moveTo(515, 629, duration=0.1)
                time.sleep(random.uniform(0.75, 1))
                pyautogui.leftClick()

                nb_click_bot = 2
                # 2 clicks on "s"
                for _ in range(nb_click_bot):
                    pyautogui.press('s')
                    time.sleep(0.5)
            elif type == "CARESSOR":
                nb_click = 2
                # 2 clicks on "s"
                for _ in range(nb_click):
                    pyautogui.press('s')
                    time.sleep(0.5)
                # click on bot searchbar
                time.sleep(random.uniform(0.75, 1))
                pyautogui.moveTo(515, 629, duration=0.1)
                time.sleep(random.uniform(0.75, 1))
                pyautogui.leftClick()

                # 1 click on "s"
                pyautogui.press('s')
                time.sleep(0.5)

            # click on first result
            time.sleep(random.uniform(0.75, 1))
            pyautogui.moveTo(632, 595, duration=0.1)
            time.sleep(random.uniform(0.75, 1))
            pyautogui.leftClick()
        elif first == "OUI":
            print("Pas encore codé")


if __name__ == "__main__":
    time.sleep(2)
    # add_items("ENERGY")
    # remove_items("ENERGY")
