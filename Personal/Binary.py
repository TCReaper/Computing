
import sys
import time
import random
import SendKeys

sys.setrecursionlimit(10000)



number = 13867

binarylog=[]



def binarycheats():
        try:
                global number
                binary = bin(number)
                binary = binary[3:]
                enter = '{ENTER}'

                SendKeys.SendKeys(str(binary))
                time.sleep(1)
                humandelay = random.uniform(0.1, 0.9) + \
                             random.uniform(0.2, 0.7) + \
                             random.uniform(0.2, 0.6) + \
                             random.uniform(0, 0.5)
                time.sleep(int(humandelay))
                SendKeys.SendKeys(enter)


                binarylog.append(number)
                number = number + 1



                print(binarylog)
                binarycheats()
                
        except Exception, e:
                print str("oops")

        
binarycheats()
