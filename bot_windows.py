import pyautogui
import time
import random

# function to open stable window


def open_window():
    # click to open window / position of the door of stable
    time.sleep(random.uniform(1.5, 2.5))
    pyautogui.moveTo(1023, 589, duration=0.1)
    time.sleep(random.uniform(1.5, 2.5))
    pyautogui.leftClick()
    time.sleep(random.uniform(1.5, 2.5))

# function to close stable window


def close_window():

    # click on backspace + "t" to reset filters bot
    time.sleep(random.uniform(0.75, 1))
    pyautogui.moveTo(522, 627, duration=0.1)
    time.sleep(random.uniform(0.75, 1))
    pyautogui.leftClick()
    time.sleep(random.uniform(0.75, 1))
    pyautogui.press('backspace')
    time.sleep(random.uniform(0.75, 1))
    pyautogui.press('t')

    # click on backspace + "t" to reset filters top 2
    time.sleep(random.uniform(0.75, 1))
    pyautogui.moveTo(518, 152, duration=0.1)
    time.sleep(random.uniform(0.75, 1))
    pyautogui.leftClick()
    time.sleep(random.uniform(0.75, 1))
    pyautogui.press('backspace')
    time.sleep(random.uniform(0.75, 1))
    pyautogui.press('t')

    # click on backspace + "t" to reset filters top 1
    time.sleep(random.uniform(0.75, 1))
    pyautogui.moveTo(518, 111, duration=0.1)
    time.sleep(random.uniform(0.75, 1))
    pyautogui.leftClick()
    time.sleep(random.uniform(0.75, 1))
    pyautogui.press('backspace')
    time.sleep(random.uniform(0.75, 1))
    pyautogui.press('t')

    # click on minus button
    time.sleep(random.uniform(0.75, 1))
    pyautogui.moveTo(391, 149, duration=0.1)
    time.sleep(random.uniform(0.75, 1))
    pyautogui.leftClick()

    # click to close window / position of the "x" to close window at the right top
    time.sleep(random.uniform(1.5, 2.5))
    pyautogui.moveTo(1579, 69, duration=0.1)
    time.sleep(random.uniform(1.5, 2.5))
    pyautogui.leftClick()
    time.sleep(random.uniform(1.5, 2.5))

if __name__ == "__main__":
    time.sleep(2)
    open_window()
    close_window()
