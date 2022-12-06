import time
import pyautogui

def spam(nn=''): 
      spam_msg = "weewooweewoo"+str(nn)
      pyautogui.write(spam_msg)
      pyautogui.press('enter')

time.sleep(3)
while True:
      break
      spam()

for i in range(100):
      spam(i)