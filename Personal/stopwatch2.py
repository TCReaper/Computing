import datetime
import SendKeys

timerfunction = True

while timerfunction:

        n = raw_input("Click To Start Timer")
        
        print
        print
        
        SendKeys.SendKeys("{SPACE}Enter{SPACE}To{SPACE}Continue")
        start = datetime.datetime.now()
        n = raw_input("Please Click")
        end = datetime.datetime.now()
        second = (end-start).total_seconds()
        print str(second) + " seconds or ", str((second/60))[:4], " minutes"

        print
