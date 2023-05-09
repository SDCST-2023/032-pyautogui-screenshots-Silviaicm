#!python3
import pyautogui
import time
import pyautogui as p

pyautogui.confirm("run")

while True:
    money=pyautogui.locateOnScreen('3a.png',confidence=0.9)
    location2 = pyautogui.locateOnScreen('2a.png',confidence=0.9)
    location = pyautogui.locateOnScreen('1a.png',confidence=0.9)
    if money!=None:
        k,j=pyautogui.center(money)
        pyautogui.doubleClick(k,j)
        pyautogui.mouseDown(k,j)
        time.sleep(0.15)
        pyautogui.mouseUp()
        time.sleep(0.1)
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
        count=1
        while count<15:
            if count<4:
                loc = p.locateAllOnScreen('2a.png',confidence=0.9)
                e = list(loc)
                if e!= []:
                    start = p.position()
                    p.moveTo(e[-1])
                time.sleep(1)
                pyautogui.click(e[-1])
                pyautogui.mouseDown(e[-1])
                time.sleep(0.25)
                pyautogui.mouseUp()
                count=count+1
            if 3<count<8:
                up = pyautogui.locateOnScreen('3a.png',confidence=0.9)
                c,i=pyautogui.center(up)
                pyautogui.click(c,i)
                pyautogui.mouseDown(c,i)
                time.sleep(0.25)
                pyautogui.mouseUp()
                pyautogui.moveTo(2,2)
                count=count+1
            if 7<count<12:
                lac = p.locateAllOnScreen('2b.png',confidence=0.9)
                r = list(lac)
                if r != []:
                    start = p.position()
                    p.moveTo(r[-1])
                time.sleep(1)
                pyautogui.click(r[-1])
                pyautogui.mouseDown(r[-1])
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
                count=count+1
            elif location!=None or location2!=None:
                break
            print(count)
