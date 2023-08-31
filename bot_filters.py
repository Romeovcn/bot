import pyautogui
import time
import random

# order to up DD : female -----> energy -> caressor -> love -> baffle -> endurance /// male -----> energy -> baffle -> endurance -> caressor -> love
# always keep a special dd in stable for male / female


def filters(type, first, gender):
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
        elif first == "YES":
            print("Pas encore codé")


if __name__ == "__main__":
    time.sleep(2)
    filters("ENERGY", "NO", "MALE")
