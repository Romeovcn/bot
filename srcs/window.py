import time

from srcs.utils import go_and_click
from srcs.utils import press_key
from srcs.utils import translate_pos

def open_window(): # function to open etable window
    if STOP_THREAD.is_set(): return True
    go_and_click(translate_pos(1351, 786))
    time.sleep(1)
    return False

def close_window(): # function to close etable window
    if STOP_THREAD.is_set(): return True
    go_and_click(translate_pos(2105, 90))
    time.sleep(1)
    return False