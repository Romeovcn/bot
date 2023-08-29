import pyautogui
import time

x, y = pyautogui.position()

# print(f"Mouse pointer is at (x, y): ({x}, {y})")
# pixel_color = pyautogui.pixel(510, 933) # ccf600
# pixel_color = pyautogui.pixel(x, y)
# print(f"La couleur RGB du pixel est : {pixel_color}")
# hex_color = "#{:02x}{:02x}{:02x}".format(pixel_color[0], pixel_color[1], pixel_color[2])
# print(f"La couleur HEXA du pixel est : {hex_color}")

# pyautogui.pixel(509, 252) #1
# pyautogui.pixel(509, 300) #2 +48
# pyautogui.pixel(509, 349) #3 +49
# pyautogui.pixel(509, 397) #4 +48
# pyautogui.pixel(509, 446) #5 +49
# pyautogui.pixel(509, 494) #6 +48
# pyautogui.pixel(509, 543) #7 +49
# pyautogui.pixel(509, 591) #8 +48
# pyautogui.pixel(509, 640) #9 +49

# print(pyautogui.pixel(509, 252)) #1
# print(pyautogui.pixel(509, 300)) #2 +48
# print(pyautogui.pixel(509, 349)) #3 +49
# print(pyautogui.pixel(509, 397)) #4 +48
# print(pyautogui.pixel(509, 446)) #5 +49
# print(pyautogui.pixel(509, 494)) #6 +48
# print(pyautogui.pixel(509, 543)) #7 +49
# print(pyautogui.pixel(509, 591)) #8 +48
# print(pyautogui.pixel(509, 640)) #9 +49

# if pyautogui.pixel(509, 640) > (255, 255, 254):
#     print("ok")
pyautogui.moveTo(509, 640, duration=2)
print("ok")