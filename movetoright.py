#!python3
import pyautogui
import time

pyautogui.confirm("run")

while True:
    loc = pyautogui.locateOnScreen('1b.png',confidence=0.9)
    e,r=pyautogui.center(loc)
    pyautogui.click(e,r)
    pyautogui.mouseDown(e,r)
    time.sleep(0.25)
    pyautogui.mouseUp()
