
# Binary Test 2
import SendKeys
import time
import sys
import random


binary = 0
number = int(str(binary), 2)


def binhack():
        
        global binary
        global number
        binary = bin(number)
        binary = binary[2:]
        print(binary)
        time.sleep(0.3)
        number = number + 1
        binhack()


def bincount():
        
        global binary
        global number

        enter = '{ENTER}'
        binary = bin(number)
        binary = binary[2:]

        
        time.sleep(0.9)
        humandelay = random.uniform(0.5, 0.9) + \
                     random.uniform(0.4, 1.2) + \
                     random.uniform(0.3, 0.9) + \
                     random.uniform(0.2, 1.5)
        time.sleep(int(humandelay))
        SendKeys.SendKeys(str(binary))
        SendKeys.SendKeys(enter)
        
        number = number + 1
        
        bincount()

bincount()
        
