#!python3
import pyautogui
import time

pyautogui.confirm("run")

while True:
    down = pyautogui.locateOnScreen('3b.png',confidence=0.9)
    d,o=pyautogui.center(down)
    pyautogui.click(d,o)
    pyautogui.mouseDown(d,o)
    time.sleep(0.25)
    pyautogui.mouseUp()