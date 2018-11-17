
import pyautogui
import random
import time

while True:
      time.sleep(5)
      break
      print(pyautogui.position())

x_min = 1150
x_max = 1800

y_min = 455
y_max = 930

while True:
      y = random.randint(y_min,y_max)
      pyautogui.moveTo(x_min,y)
      pyautogui.dragRel(x_max-x_min,0,0.15,button='left')
      
      x = random.randint(x_min,x_max)
      pyautogui.moveTo(x,y_min)
      pyautogui.dragRel(0,y_max-y_min,0.15,button='left')
