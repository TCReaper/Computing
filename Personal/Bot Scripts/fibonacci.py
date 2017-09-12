
import sys
import time
import random
import SendKeys

sys.setrecursionlimit(10000)

fibonacci = 239820118265953088038145437511237497044699584020285287192916468822142124682166269777110003547171459506578561471840683878010615797658560919027914703304747784934322068108673344179645
388037102540331590842728511723032382131228894634160078174151915758186246746316504855676632271220045232721318561132067113541847197950188735686803230319347190365607190275898427760386

fibo = []
for i in f.strip:
        fibo.append(i)

first = fibo[0]
second = fibo[1]

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
