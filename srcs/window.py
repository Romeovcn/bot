import time

from srcs.utils import go_and_click
from srcs.utils import press_key
from srcs.utils import translate_pos

def open_window(): # function to open etable window
    go_and_click(translate_pos(1374, 762))
    time.sleep(1)

def close_window(): # function to close etable window
    go_and_click(translate_pos(2105, 90))
    time.sleep(1)

if __name__ == "__main__":
    time.sleep(2)
    open_window()
    close_window()