import pyautogui
import time

x, y = pyautogui.position()

print(f"Mouse pointer is at (x, y): ({x}, {y})")
pixel_color = pyautogui.pixel(x, y)
print(f"La couleur RGB du pixel est : {pixel_color}")
# hex_color = "#{:02x}{:02x}{:02x}".format(pixel_color[0], pixel_color[1], pixel_color[2])
# print(f"La couleur HEXA du pixel est : {hex_color}")