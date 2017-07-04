import time
import pyautogui

# brawl bot
# by TCReaper



#### please make sure that the module       >> pyautogui <<       is installed



#### CHANGE USER SETTINGS HERE ###############################################

up_key = 'w'
down_key = 's'
left_key = 'a'
right_key = 'd'

heavy = 'u'
light = 'y'
shift = 'q'

selected_move = 'nsig' #change this to the attack you want

#### OPTIONS --> groundpound , sidesig , downsig , nsig 


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
        groundpound()

def sidesig():
        pyautogui.keyDown(left_key)
        pyautogui.press(heavy)
        pyautogui.keyUp(left_key)
        time.sleep(2)
        pyautogui.keyDown(down_key)
        pyautogui.press(heavy)
        pyautogui.keyUp(down_key)
        time.sleep(2)
        sidesig()

def downsig():
        pyautogui.press(down_key)
        time.sleep(0.5)
        pyautogui.press(light)
        time.sleep(0.75)
        pyautogui.keyDown(down_key)
        pyautogui.press(heavy)
        pyautogui.keyUp(down_key)
        time.sleep(1)
        pyautogui.press(left_key)
        time.sleep(0.5)
        pyautogui.press(light)
        time.sleep(0.5)
        pyautogui.keyDown(down_key)
        pyautogui.press(heavy)
        pyautogui.keyUp(down_key)
        time.sleep(1)
        downsig()

def phaseddsig():
        pyautogui.press(up_key)
        time.sleep(0.2)
        pyautogui.press(shift)
        pyautogui.keyDown(down_key)
        time.sleep(0.2)
        pyautogui.press(heavy)
        pyautogui.keyUp(down_key)
        time.sleep(2)
        phaseddsig()

def nsig():
        pyautogui.press(heavy)
        time.sleep(1)
        nsig()



func_list = {'groundpound':groundpound,'sidesig':sidesig,'downsig':downsig,'nsig':nsig}


time.sleep(3)
func_list[selected_move]()
