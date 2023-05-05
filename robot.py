#!python3
import pyautogui
import time
import random

pyautogui.confirm("run")

while True:
    location2 = pyautogui.locateOnScreen('2a.png',confidence=0.9)
    location = pyautogui.locateOnScreen('1a.png',confidence=0.9)
    if location2 != None:
        print('found 2 block')
        w,z=pyautogui.center(location2)
        pyautogui.doubleClick(w,z)
        pyautogui.mouseDown(w,z)
        time.sleep(0.15)
        pyautogui.mouseUp()
        time.sleep(0.1)
    if location != None:
        print('found 1 block')
        x,y=pyautogui.center(location)
        pyautogui.click(x,y)
        pyautogui.mouseDown(x,y)
        time.sleep(0.15)
        pyautogui.mouseUp()
        time.sleep(0.1)
    else:
        count=1
        while count<15:
            if count<4:
                loc = pyautogui.locateOnScreen('1b.png',confidence=0.9)
                e,r=pyautogui.center(loc)            
                pyautogui.click(e,r)
                pyautogui.mouseDown(e,r)
                time.sleep(0.25)
                pyautogui.mouseUp()
                count=count+1
            if 3<count<8:
                up = pyautogui.locateOnScreen('3a.png',confidence=0.9)
                u,p=pyautogui.center(up)
                pyautogui.click(u,p)
                pyautogui.mouseDown(u,p)
                time.sleep(0.25)
                pyautogui.mouseUp()
            if 7<count<12:
                lac = pyautogui.locateOnScreen('2b.png',confidence=0.9)
                l,m=pyautogui.center(lac)
                pyautogui.click(l,m)
                pyautogui.mouseDown(l,m)
                time.sleep(0.25)
                pyautogui.mouseUp()
                count=count+1
            if 11<count<16:
                down = pyautogui.locateOnScreen('3b.png',confidence=0.9)
                d,o=pyautogui.center(down)
                pyautogui.click(d,o)
                pyautogui.mouseDown(d,o)
                time.sleep(0.25)
                pyautogui.mouseUp()
            print(count)
