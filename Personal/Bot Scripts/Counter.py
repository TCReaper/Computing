import SendKeys
import time
import random
import sys
from msvcrt import getch
import pyperclip

sys.setrecursionlimit(3344)

counter = 239268


def count():

        try:
                global counter
                global limit
                
                enter = "{ENTER}"
                time.sleep(0.8)
                SendKeys.SendKeys(str(counter)[0])
                humandelay = random.uniform(0.4, 1.9) + \
                             random.uniform(0.3, 1.9) + \
                             random.uniform(0.5, 0.9) + \
                             random.uniform(0, 3.5)
                time.sleep(int(humandelay))
                SendKeys.SendKeys(str(counter)[1:])
                SendKeys.SendKeys(enter)
                pyperclip.copy(str(counter))
                counter += 1
                


        except Exception, e:
                print str("oops")



def help():
        while True:
                key = ord(getch())
                if key == 224:
                        return False
                else:
                        count()
       
help()
