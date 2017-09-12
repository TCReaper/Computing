

import SendKeys
import time
import sys
import random


textyes = True
enter = '{ENTER}'
def text():
      text = raw_input("Text to convert:  ")
      time.sleep(3)
      for i in text:
            mid = ord(i)
            converted = bin(mid)
            converted = converted[2:]
            SendKeys.SendKeys(str(converted))
            time.sleep(0.75)
            SendKeys.SendKeys(enter)
            time.sleep(0.75)
      
            

      
text()
