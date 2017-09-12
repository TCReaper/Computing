import time
import pyautogui


##############################################################################


# brawl bot
# by TCReaper


#### please make sure that the module       >> pyautogui <<       is installed


####        you should be on the "READY FOR BATTLE" screen
####        it will start the farming process automatically
####        start this code and switch into game


#### CHANGE USER SETTINGS HERE ###############################################

up_key = 'w'
down_key = 's'
left_key = 'a'
right_key = 'd'

heavy = 'u'
light = 'y'
shift = 'q'

selected_move = 'downsig'  #change this to the attack you want
game_time = 3 #minutes  #change this to duration of game


#### OPTIONS --> groundpound , sidesig , downsig , nsig
#### OPTIONS --> any integer from 1 to 15


#### CODE ####################################################################


def groundpound():
        pyautogui.press(up_key)
        pyautogui.press(up_key)
        pyautogui.keyDown(down_key)
        pyautogui.press(heavy)
        pyautogui.keyUp(down_key)
        time.sleep(0.2)
        pyautogui.press(up_key)
        time.sleep(0.1)
        pyautogui.press(heavy)
        time.sleep(1.5)

def sidesig():
        pyautogui.keyDown(left_key)
        pyautogui.press(heavy)
        pyautogui.keyUp(left_key)
        time.sleep(2)
        pyautogui.keyDown(down_key)
        pyautogui.press(heavy)
        pyautogui.keyUp(down_key)
        time.sleep(2)

def downsig():
        pyautogui.keyDown(down_key)
        time.sleep(0.25)
        pyautogui.press(heavy)
        pyautogui.keyUp(down_key)
        time.sleep(1)

def nsig():
        pyautogui.press(heavy)
        time.sleep(1)


##############################################################################


func_list = {'groundpound':groundpound,'sidesig':sidesig,'downsig':downsig,'nsig':nsig}


farming = True
game_seconds = game_time * 60   #time of game in seconds
time.sleep(5)
for i in range(2):
        pyautogui.press('c')
        time.sleep(1.75)
time.sleep(12.75)
while farming:
        seconds_counter = 0
        while seconds_counter < game_seconds:
                if selected_move == 'nsig':
                        seconds_counter += 1
                if selected_move == 'downsig':
                        seconds_counter += 1.25
                func_list[selected_move]()
        time.sleep(seconds_counter - game_seconds)
        time.sleep(7.5)
        for i in range(6):
                pyautogui.press('c')
                time.sleep(1.75)
        time.sleep(12.75)
                


##############################################################################
