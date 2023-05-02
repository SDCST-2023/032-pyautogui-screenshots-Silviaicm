#!python3
import pyautogui
import time

pyautogui.confirm("run")

while True:
    location2 = pyautogui.locateOnScreen('2a.png',confidence=0.9)
    w,z=pyautogui.center(location2)
    pyautogui.doubleClick(w,z)
    pyautogui.mouseDown(w,z)
    time.sleep(0.15)
    pyautogui.mouseUp()
    time.sleep(0.1)
    location = pyautogui.locateOnScreen('1a.png',confidence=0.9)
    x,y=pyautogui.center(location)
    pyautogui.click(x,y)
    pyautogui.mouseDown(x,y)
    time.sleep(0.15)
    pyautogui.mouseUp()
    time.sleep(0.1)
