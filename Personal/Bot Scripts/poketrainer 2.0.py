

# POKEMON ON DISCORD

#################### READ BEFORE USE

#################### when run, console will ask for input


#################### input ENTER to run spam message
#################### xp generation is around 80-120k an hour
#################### go to text field and leave it
#################### TO CANCEL:
####################      MOVE YOUR MOUSE TO EXTREME TOP LEFT 


#################### input 'smartspam' and ENTER to copy paste
#################### xp generation scales to the length of your msg
#################### comes at no lag/cost of writing so it is
#################### very preferable
#################### TO CANCEL:
####################      MOVE YOUR MOUSE TO EXTREME TOP LEFT    


#################### to input moves, type anything else and ENTER
#################### console will ask for 4 inputs
#################### input ONLY the names of the moves
#################### go to text field and it will auto do everything




import sys
import pyautogui
import time
import random

sys.setrecursionlimit(99999999)


def spam():
    x = 0
    time.sleep(5)
    ran = 'experience'
    spam = ''
    for i in range(15):
        spam += ran
    spam = spam[:-2]

    while True:
        x+=1
        pyautogui.typewrite(spam)
        pyautogui.typewrite('\n')
        if x == 100000:
            return None
        time.sleep(1)

        
def smart():
    x = 0
    time.sleep(4)
    while True:
        time.sleep(2)
        pyautogui.keyDown('ctrl')
        pyautogui.typewrite('v')
        pyautogui.keyUp('ctrl')
        pyautogui.typewrite('\n')
        x += 1
        if x == 2500:
            pyautogui.keyDown('ctrl')
            pyautogui.typewrite('r')
            pyautogui.keyUp('ctrl')
            x = 0

    
def moves():
    data = []
    for i in range(4):
        data.append(input('move: '))
    time.sleep(4)
    for i in range(len(data)):
        pyautogui.typewrite('p!learn '+data[i])
        pyautogui.typewrite('\n')
        time.sleep(1)
        pyautogui.typewrite('p!replace '+str(i+1))
        pyautogui.typewrite('\n')
        time.sleep(1)

def start():
    choice = input('enter to spam, smartspam for paste, anything else to moves: ')
    if choice == '':
        spam()
    elif choice == 'smartspam':
        smart()
    else:
        moves()

def pokemon():
    start()

start()

