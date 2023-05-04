#!python3
import pyautogui
import time

pyautogui.confirm("run")

while True:
    lac = pyautogui.locateOnScreen('2b.png',confidence=0.9)
    l,m=pyautogui.center(lac)
    pyautogui.click(l,m)
    pyautogui.mouseDown(l,m)
    time.sleep(0.25)
    pyautogui.mouseUp()