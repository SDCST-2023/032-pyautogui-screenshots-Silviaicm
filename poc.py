import pyautogui as p
import time
p.confirm("go")
while True:
    x = p.locateAllOnScreen('2b.png',confidence=0.9)
    y = list(x)
    print(y)
    if y != []:
        start = p.position()
        p.moveTo(y[-1])
        time.sleep(0.25)
        p.moveTo(start)
    time.sleep(1)
