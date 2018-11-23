
import sys
import pyautogui
import time
import random

sys.setrecursionlimit(99999999)

x = 0

time.sleep(3)

while True:
    ran = ''
    for i in range(44):
        ran += random.choice('qwertyuiopasdfghjklzxcvbnm1234567890')
    pyautogui.typewrite(str(x)+'      '+ran)
    x += 1
    pyautogui.typewrite('\n')

    time.sleep(10)
