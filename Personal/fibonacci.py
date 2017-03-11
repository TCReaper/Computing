
import sys
import time
import random
import SendKeys

sys.setrecursionlimit(10000)

first = 3254830071569718737604135765141440985245996862858900395844371829572479434062128681271684515666943918276960875482517915520246056253019766319301321652047243019401297415371
second = 5266425683405057731495444092244174522861452105372257554189984579279362348691671275244047446224217175749585504549914494508130592637252870325717753776846061280936139129709


def fibonacci():

        global first
        global second
        enter = '{ENTER}'
        output = str(first+second)
        time.sleep(1)
        humandelay = random.uniform(1.1, 2.9) + \
                     random.uniform(0.4, 1.7) + \
                     random.uniform(1.2, 0.6) + \
                     random.uniform(0, 1.5)
        time.sleep(int(humandelay))
        
        SendKeys.SendKeys(output)
        SendKeys.SendKeys(enter)

        first = int(second)
        second = int(output)

        fibonacci()


fibonacci()
