import SendKeys
import time
global counter

counter = 1
spammsg = "i_like_to_farm_xp_"


def spam():
      print(counter)
      try:
            global counter
            global limit
            message = spammsg+str(counter)
            enter = "{ENTER}"
            time.sleep(1)
            SendKeys.SendKeys(message)
            SendKeys.SendKeys(enter)
            counter += 1
            


      except Exception, e:
            print str("oops")

spamming = True
time.sleep(3)
while spamming:
      spam()
      time.sleep(0.9)
