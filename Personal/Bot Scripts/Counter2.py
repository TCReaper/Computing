import SendKeys
import time
import random
import sys
from msvcrt import getch
import pygame

sys.setrecursionlimit(3011)

counter = 231250

def count():
        try:
                global counter
                global limit
                
                enter = "{ENTER}"
                SendKeys.SendKeys(str(counter))
                time.sleep(0.8)
                humandelay = random.uniform(0.1, 0.9) + \
                             random.uniform(0.2, 0.7) + \
                             random.uniform(0.2, 0.6) + \
                             random.uniform(0, 0.5)
                #time.sleep(int(humandelay))
                SendKeys.SendKeys(enter)
                counter += 1
        except Exception, e:
                print str("oops")

run = 1

while run:
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONUP:
                run = 0
        else:
                count()
