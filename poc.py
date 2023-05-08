import pyautogui as p
import time
p.confirm("go")
while True:
    lac = p.locateAllOnScreen('2b.png',confidence=0.9)
    y = list(lac)
    print(y)
    if y != []:
        start = p.position()
        p.moveTo(y[-1])
        time.sleep(0.25)
        p.moveTo(start)
        time.sleep(1)
        p.click(y[-1])
        p.mouseDown(y[-1])
        time.sleep(0.25)
        p.mouseUp()