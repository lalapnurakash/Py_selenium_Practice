import random
import time

import pyautogui as pyautogui

while True:
 x=random.randint(600,700)
 y=random.randint(600,700)
 pyautogui.moveTo(x,y,0.5)
 time.sleep(5)

