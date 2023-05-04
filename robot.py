#!python3
import pyautogui
import time
import random

pyautogui.confirm("run")

while True:
    location2 = pyautogui.locateOnScreen('2a.png',confidence=0.9)
    location = pyautogui.locateOnScreen('1a.png',confidence=0.9)
    if location2 != None:
        w,z=pyautogui.center(location2)
        pyautogui.doubleClick(w,z)
        pyautogui.mouseDown(w,z)
        time.sleep(0.15)
        pyautogui.mouseUp()
        time.sleep(0.1)
    if location != None:
        x,y=pyautogui.center(location)
        pyautogui.click(x,y)
        pyautogui.mouseDown(x,y)
        time.sleep(0.15)
        pyautogui.mouseUp()
        time.sleep(0.1)
    else:
        pyautogui.hscroll(random.randint(-20,20))
        pyautogui.scroll(random.randint(-200,2000))
        loc = pyautogui.locateOnScreen('1b.png',confidence=0.9)
        e,r=pyautogui.center(loc)
        lac = pyautogui.locateOnScreen('2b.png',confidence=0.9)
        l,m=pyautogui.center(lac)
        pyautogui.click(random(loc,lac))
