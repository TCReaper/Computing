import time
import pyautogui
from pyautogui import moveTo as m
from pyautogui import click as c

def helper():
    one = (1454,1026)
    two = (1448,945)
    three = (1793,308) #pause before
    four = (1603,957) #repeat twice
    five = (1897,999)

    time.sleep(3)

    m(one)
    c()

    time.sleep(2)
    
    m(two)
    c()

    time.sleep(12.5)

    m(three)
    c()

    time.sleep(4)

    m(four)
    c()

    time.sleep(3)

    m(four)
    c()
    c()

    time.sleep(5)

    m(five)
    c()

    time.sleep(5)

    pyautogui.hotkey('ctrl', 'w')

    time.sleep(5)

    pyautogui.hotkey('ctrl', 'w')

    time.sleep(5)
    
def function():

    episodes = int(input('enter amount of episodes to download: '))
    for i in range(episodes):
        helper()

function()

