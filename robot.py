#!python3
import pyautogui
import time
import pyautogui as p

pyautogui.confirm("run")

while True:
    mball=pyautogui.locateOnScreen('4b.png',confidence=0.9)
    ball=pyautogui.locateOnScreen('4a.png',confidence=0.9)
    location2 = pyautogui.locateOnScreen('2a.png',confidence=0.9)
    location = pyautogui.locateOnScreen('1a.png',confidence=0.9)
    if mball!=None:
        h,t=pyautogui.center(mball)
        pyautogui.doubleClick(h,t)
        pyautogui.mouseDown(h,t)
        time.sleep(0.15)
        pyautogui.mouseUp()
        time.sleep(0.1)
    if ball!=None:
        k,j=pyautogui.center(ball)
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
    if mball==None and ball==None and location==None and location2==None:
        count=1
        while count<14:
            location2 = pyautogui.locateOnScreen('2a.png',confidence=0.9)
            location = pyautogui.locateOnScreen('1a.png',confidence=0.9)
            if location!=None or location2!=None:
                break
            if count<4:
                location2 = pyautogui.locateOnScreen('2a.png',confidence=0.9)
                location = pyautogui.locateOnScreen('1a.png',confidence=0.9)
                if location!=None or location2!=None:
                    break
                loc = p.locateAllOnScreen('1b.png',confidence=0.9)
                e = list(loc)
                if len(e)==1:
                    v,b=pyautogui.center(e[0])
                    pyautogui.click(v,b)
                    pyautogui.mouseDown(v,b)
                    time.sleep(0.25)
                    pyautogui.mouseUp()
                    pyautogui.moveTo(2,2)
                if len(e)>1:
                    start = p.position()
                    p.moveTo(e[-1])
                    time.sleep(1)
                    pyautogui.click(e[-1])
                    pyautogui.mouseDown(e[-1])
                    time.sleep(0.25)
                    pyautogui.mouseUp()
                count=count+1
            elif 3<count<8:
                location2 = pyautogui.locateOnScreen('2a.png',confidence=0.9)
                location = pyautogui.locateOnScreen('1a.png',confidence=0.9)
                if location!=None or location2!=None:
                    break
                up = pyautogui.locateOnScreen('3a.png',confidence=0.9)
                c,i=pyautogui.center(up)
                pyautogui.click(c,i)
                pyautogui.mouseDown(c,i)
                time.sleep(0.25)
                pyautogui.mouseUp()
                pyautogui.moveTo(2,2)
                count=count+1
            elif 7<count<12:
                location2 = pyautogui.locateOnScreen('2a.png',confidence=0.9)
                location = pyautogui.locateOnScreen('1a.png',confidence=0.9)
                if location!=None or location2!=None:
                    break
                lac = p.locateAllOnScreen('2b.png',confidence=0.9)
                r = list(lac)
                if len(r) == 1:
                    s,a=pyautogui.center(r[0])
                    pyautogui.click(s,a)
                    pyautogui.mouseDown(s,a)
                    time.sleep(0.25)
                    pyautogui.mouseUp()
                    pyautogui.moveTo(2,2)
                if len(r)>1:
                    start = p.position()
                    p.moveTo(r[-1])
                    time.sleep(1)
                    pyautogui.click(r[-1])
                    pyautogui.mouseDown(r[-1])
                    time.sleep(0.25)
                    pyautogui.mouseUp()
                count=count+1
            elif 11<count<16:
                location2 = pyautogui.locateOnScreen('2a.png',confidence=0.9)
                location = pyautogui.locateOnScreen('1a.png',confidence=0.9)
                if location!=None or location2!=None:
                    break
                down = pyautogui.locateOnScreen('3b.png',confidence=0.9)
                d,o=pyautogui.center(down)
                pyautogui.click(d,o)
                pyautogui.mouseDown(d,o)
                time.sleep(0.25)
                pyautogui.mouseUp()
                count=count+1
            print(count)


