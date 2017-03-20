

# test for a working afk farm bot

# modules to implement attack/pausing

import SendKeys
import time
import random
import sys

# code for the bot (Python)

sys.setrecursionlimit( 9 + 1195 )

def bot():
        n_light = "c"
        l_light = "ac"
        d_light = "sc"
        r_light = "dc"
        moveleft = "a"
        moveright = "d"
        jump = "w"
        dodge = "z"
        n_heavy = "x"
        l_heavy = "ax"
        d_heavy = "sx"
        r_heavy = "dx"
        
        movelist = [n_light , l_light , d_light , r_light , moveleft , moveright , jump , dodge , \
                    n_heavy , l_heavy , d_heavy , r_heavy]  #(163 xp)
        
        siglist = [n_heavy , l_heavy , d_heavy , r_heavy] #(94 xp)

        bruteforce = [n_heavy , dodge , jump ]   #(79 xp)
        
        chosenmove = random.choice(movelist)
        SendKeys.SendKeys(chosenmove)
        #SendKeys.SendKeys(l_heavy)
        #SendKeys.SendKeys(enter)

        time.sleep(1)
        
        bot()


time.sleep(3)
bot()
