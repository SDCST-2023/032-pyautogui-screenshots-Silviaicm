#!python3
import pyautogui
import time

pyautogui.confirm("run")

while True:
    loc = pyautogui.locateOnScreen('b.png',confidence=0.9)
    e,r=pyautogui.center(loc)
    pyautogui.click(e,r)
    pyautogui.mouseDown(e,r)
    time.sleep(2)
    while pyautogui.mouseDown:
        pyautogui.moveTo(e+100)