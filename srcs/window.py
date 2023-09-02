import time

from srcs.utils import go_and_click
from srcs.utils import press_key
from srcs.utils import translate_pos

def open_window(): # function to open etable window
    go_and_click(translate_pos(1374, 762))
    time.sleep(1)

def close_window(): # function to close etable window
    # click on backspace + "t" to reset filters bot
    # go_and_click((522, 627))
    # press_key('backspace')
    # press_key('t')

    # click on backspace + "t" to reset filters top 2
    # go_and_click((518, 152))
    # press_key('backspace')
    # press_key('t')

    # click on backspace + "t" to reset filters top 1
    # go_and_click((518, 111))
    # press_key('backspace')
    # press_key('t')

    # click on minus button
    # go_and_click((391,149))

    # click to close window / position of the "x" to close window at the right top
    go_and_click(translate_pos(2105, 90))

if __name__ == "__main__":
    time.sleep(2)
    open_window()
    close_window()