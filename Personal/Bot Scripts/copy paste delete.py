
import time
import pyautogui
import pyperclip

time.sleep(3) #5 second delay to get to text field

counter = 90
while counter>0:
    
    time.sleep(0.5)
    pyautogui.typewrite('a')
    pyautogui.press('enter')
    time.sleep(0.5)
    
    pyautogui.press('enter')
    pyautogui.press('up')

    pyautogui.press('backspace')

    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')

    counter -= 1
    
      
