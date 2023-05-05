#!python3
import pyautogui
import time

pyautogui.confirm("run")

while True:
    up = pyautogui.locateOnScreen('3a.png',confidence=0.9)
    u,p=pyautogui.center(up)
    pyautogui.click(u,p)
    pyautogui.mouseDown(u,p)
    time.sleep(0.25)
    pyautogui.mouseUp()