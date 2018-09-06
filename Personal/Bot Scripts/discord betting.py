import SendKeys
import time
                
enter = "{ENTER}"

while True:
        length = int(input('How many attempts:  '))
        amount = int(input('Amount to gamble:  '))
        time.sleep(5)
        SendKeys.SendKeys('t!credits')
        SendKeys.SendKeys(enter)
        SendKeys.SendKeys('I will be gambling an amount of {0} credits {1} times'\
                          .format(str(amount),str(length))\
                          .replace(' ','{SPACE}'))
        SendKeys.SendKeys(enter)
        SendKeys.SendKeys('{0} credits will be used'.format(length*amount)\
                          .replace(' ','{SPACE}'))
        SendKeys.SendKeys(enter)
        time.sleep(3)
        for i in range(length):
                SendKeys.SendKeys('t!slots {0} --- {1} of {2}'.format(amount,i+1,length)\
                                  .replace(' ','{SPACE}'))
                SendKeys.SendKeys(enter)
                time.sleep(10)
        SendKeys.SendKeys('t!credits')
        SendKeys.SendKeys(enter)
        
