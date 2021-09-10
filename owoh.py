import random
import time
import keyboard
import pyautogui
from copypasta import copypasta as c


def delayx():
    time = 20.5
    for i in range(12):
        time += random.random()
    time -= random.randint(3,8)
    
    return time

def togira():
    time.sleep(0.25)
    c('!find')
    time.sleep(0.25)
    c('!get')
    
def x(x=''):
    if x == '':
        x = input('input x range:  ')
        
    if x == '':
        x = 75
        
    else:
        x = int(x)
        
    for i in range(x):
        time.sleep( delayx() + delayx()//2 )
        c('owoh')
        time.sleep( delayx()//2 )
        c('owob')
        time.sleep( delayx()//5 )
        c('owo')
        
        #togira()
        
        print(str( x - i ))

    time.sleep(10)
    c('owo')

def delay():
    time = 20
    return time

def keypress():
    if keyboard.is_pressed('ctrl+space'):
        return True

def owo_multi():
    try:
        time.sleep(0.5)
        c('owoh')
        time.sleep(0.25)
        c('owob')
        time.sleep(0.25)
        c('owo')
    except pyautogui.FailSafeException:
        time.sleep(0.1)
    
def bind():
    while True:  
        if keypress():
            owo_multi()

def auto():
    while True:
        x()

def owo():
    while True:
        if keyboard.is_pressed('w'):
            #time.sleep(0.1)
            pyautogui.press('enter')

def multi():
    while True:
        try:
            if keyboard.is_pressed('w'):
                pass
                #pyautogui.press('enter')
            elif keyboard.is_pressed('=+-'):
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                time.sleep(0.5)
                c('.fl n')
                c('.bt')
            elif keypress():
                owo_multi()
                
        except KeyboardInterrupt or FailSafeException:
            break

