import time
import sys
import pyautogui

# brawl bot brute force

def groundpound():
        pyautogui.press('w')
        pyautogui.press('w')
        pyautogui.keyDown('s')
        pyautogui.press('x')
        pyautogui.keyUp('s')
        time.sleep(0.2)
        pyautogui.press('w')
        time.sleep(0.1)
        pyautogui.press('x')
        time.sleep(1.5)
        groundpound()

def sidesig():
        pyautogui.keyDown('a')
        pyautogui.press('x')
        pyautogui.keyUp('a')
        time.sleep(2)
        pyautogui.keyDown('d')
        pyautogui.press('x')
        pyautogui.keyUp('d')
        time.sleep(2)
        sidesig()

def downsig():
        pyautogui.press('d')
        time.sleep(0.5)
        pyautogui.press('c')
        time.sleep(0.75)
        pyautogui.keyDown('s')
        pyautogui.press('t')
        pyautogui.keyUp('s')
        time.sleep(1)
        pyautogui.press('a')
        time.sleep(0.5)
        pyautogui.press('c')
        time.sleep(0.5)
        pyautogui.keyDown('s')
        pyautogui.press('t')
        pyautogui.keyUp('s')
        time.sleep(1)
        downsig()

def phaseddsig():
        pyautogui.press('w')
        time.sleep(0.2)
        pyautogui.press('z')
        pyautogui.keyDown('s')
        time.sleep(0.2)
        pyautogui.press('x')
        pyautogui.keyUp('s')
        
        time.sleep(2)
        phaseddsig()
        
time.sleep(3)
downsig()
