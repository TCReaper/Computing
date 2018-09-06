
import pyautogui
import time

while True:
      break
      time.sleep(5)
      print()
      

x_min = 10
y_min = 140
x_max = 1900
y_max = 602

xx = x_min
yy = y_min

time.sleep(3)

while True:
      pyautogui.click(xx, yy, button='left')
      
      xx += 25
      
      if xx > x_max:
            xx = x_min
            yy += 40
      if yy > y_max:
            pyautogui.dragRel(0, -600, duration=0.5)
            xx = x_min
            yy = y_min
