import time
import pyautogui

def spam(): 
      spam_msg = "did u"
      pyautogui.write(spam_msg)
      time.sleep(0.1)
      pyautogui.press('enter')

time.sleep(3)
while True:
      spam()
