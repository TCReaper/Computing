import SendKeys
import time
import sys
import ctypes

sys.setrecursionlimit(10000)

def snail():
        
        try:
                farmer = "!s{SPACE}race{SPACE}5"
                enter = "{ENTER}"
                ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
                ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
                time.sleep(18)
                
                SendKeys.SendKeys(farmer)
                SendKeys.SendKeys(enter)
                
                snail()
                
        except Exception, e:
                print str("oops")


time.sleep(3)
farmer = "!sSPACE}race{SPACE}5"
enter = "{ENTER}"
ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
SendKeys.SendKeys(farmer)
SendKeys.SendKeys(enter)
snail()
