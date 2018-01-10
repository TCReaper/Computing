import datetime
import SendKeys
import math
import time

betting = True

start = datetime.datetime.now()
while betting:

      timenow = datetime.datetime.now()
      second = (timenow-start).total_seconds()

      second = math.floor(second)
      
      if second%61 == 5:

            SendKeys.SendKeys("!slot{ENTER}")

      elif second%182 == 35:

            SendKeys.SendKeys("!squid{ENTER}")

      time.sleep(1.000001)
