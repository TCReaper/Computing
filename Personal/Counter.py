import SendKeys
import time
import random
import sys
from msvcrt import getch
import pygame

sys.setrecursionlimit(3344)

counter = 202281


def count():

        try:
                global counter
                global limit
                
                enter = "{ENTER}"
                time.sleep(0.8)
                humandelay = random.uniform(0.1, 0.9) + \
                             random.uniform(0.2, 0.7) + \
                             random.uniform(0.2, 0.6) + \
                             random.uniform(0, 0.5)
                time.sleep(int(humandelay))
                SendKeys.SendKeys(str(counter))
                SendKeys.SendKeys(enter)
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
