import SendKeys
import random
import time

keys = 'wasd'
typed = {}
for i in keys:
        typed[i] = 1

while True:
        chosen = random.choice(keys)
        SendKeys.SendKeys(chosen)
        typed[chosen] += 1
        time.sleep(0.01)
        print '\n'*50
        print typed

        
        
