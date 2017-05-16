import SendKeys
import time


counter = 1
spammsg = "Spam_"


def spam():
      print(counter)
      try:
            global counter
            global limit
            message = spammsg+str(counter)
            enter = "{ENTER}"
            time.sleep(0.5)
            SendKeys.SendKeys(message)
            SendKeys.SendKeys(enter)
            counter += 1


      except Exception, e:
            print str("oops")

spamming = True
while spamming:
      spam()
