import pyautogui
import time
import math

def translate_pos(pos_x, pos_y):
    # if (SCREEN_SIZE) == (2560, 1440):
    #     return (pos_x, pos_y)
    ratio_x = 1920 / 2560
    ratio_y = 1080 / 1440
    new_x = math.ceil(pos_x * ratio_x)
    new_y = math.ceil(pos_y * ratio_y)
    return (new_x, new_y)

x, y = pyautogui.position()

print(f"Mouse pointer is at (x, y): ({x}, {y})")
pixel_color = pyautogui.pixel(x, y)
print(f"La couleur RGB du pixel est : {pixel_color}")
print(translate_pos(2470, 1322))
# hex_color = "#{:02x}{:02x}{:02x}".format(pixel_color[0], pixel_color[1], pixel_color[2])
# print(f"La couleur HEXA du pixel est : {hex_color}")