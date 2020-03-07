
import random
import time
import pyautogui
from copypasta import copypasta as c


def delayx():
    time = 17.5
    for i in range(12):
        time += random.random()
    time -= random.randint(3,8)
    
    return time


def functx():
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
        c( str( x - i ))

    c('done')

def delay():
    time = 30
    return time

def memer(i):
    time.sleep( delay() )
    c('pls beg')            
    time.sleep( 2 )
    c('pls search')
    
    if i%10 == 10:
        c('pls deposit all')
            


functx()


def delay():
    time = 30
    return time

def memer(i):
    time.sleep( delay() )
    c('pls beg')            
    time.sleep( 2 )
    c('pls search')
    
    if i%10 == 9:
        c('pls deposit all')

    return None
            
def funct(x='a'):
    
    if x == '':
        x = 9999
        switch = False
        
    else:
        x = 9999
        switch = True
        
    for i in range(x):
        
        memer(i)
        if switch:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            memer(i)
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')

#funct()






































