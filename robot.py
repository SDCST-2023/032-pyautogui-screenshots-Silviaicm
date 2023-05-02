#!python3
import pyautogui
import time

pyautogui.confirm("run")

while True:
    location = pyautogui.locateOnScreen('1a.png',confidence=0.9)
    x,y=pyautogui.center(location)
    pyautogui.click(x,y)
    pyautogui.mouseDown(x,y)
    time.sleep(0.15)
    pyautogui.mouseUp()
    time.sleep(0.1)
    