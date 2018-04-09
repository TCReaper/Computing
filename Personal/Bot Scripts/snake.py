
import sys
import time
import random
import SendKeys

sys.setrecursionlimit(10000)
enter = '{SPACE}'

def snake_stop():
      x = random.randint(0,5)
      y = random.randint(0,5)
      z = random.randint(0,10)

      if x == y:#and x == z:

            SendKeys.SendKeys(enter)
            time.sleep(random.randint(5,9))
            SendKeys.SendKeys(enter)

while True:
      snake_stop()


