

import time
import pyperclip
import pyautogui





def typer(msg):
    
    pyperclip.copy(msg)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    
    pyautogui.press('enter')
    pyautogui.press('enter')
    
    time.sleep(1)

def dataFromText():
    file = open('trade.txt')
    data = []
    for line in file:
        line = line.strip().split('p!p add ')[1].split(' ')
        for ID in line:
            try:
                tester = int(ID)
            except Exception:
                break
            else:
                data.append(ID)
    return data
    

def trade(user=None,text=False,amt=225):
    if text:
        data = dataFromText()
    else:
        data = [str(x+1) for x in range(amt)]
    sets = []
    while len(data)>0:
        trader = 'p!p add '+' '.join(data[:25])
        sets.append(trader)
        data = data[25:]
    time.sleep(2)
    for trade in sets:
        typer(trade)

    time.sleep(3)
    
    typer('p!confirm')
    if user != None:
        typer('p!trade '+user)

def amounttrade(amount):
    trade(amt=amount)

def texttrade():
    trade(text=True)


def multitrade(user,timer=2.5):
    while True:
        trade('@'+user)
        time.sleep(int(timer))
    

def pokemon():
    pages = int(input('number of pages?  '))
    name = input('pokemon?  ')
    if name == '':
        text = ' '+input('p!pokemon ')
    else:
        text = ' --name '+name
    
    time.sleep(5)
    for x in range(pages):
        typer('p!pokemon '+str(x)+text)
        time.sleep(0.25)


def prune(pages):
    time.sleep(2.5)
    typer('t@prune '+str(pages*3)+' @Pokécord#4503')
    time.sleep(5)
    typer('t@prune '+str(pages*3)+' "p!market search"')


def market():
    pages = int(input('number of pages?  '))
    name = input('pokemon?  ')
    text = ' --order price a'
    if name != '':
        text = ' --order price a --name '+name

    time.sleep(5)
    for x in range(pages):
        typer('p!market search '+str(x+1)+text)
        time.sleep(0.25)
        
    prune(pages)

def file_count():
    file = open('market.txt')
    count = 0
    for line in file:
        count+=1
    print('poke IDs - '+str(count))

    
def inputting():
    file = open('market.txt','w')
    data = []
    while True:
        dataset = input('market IDs:  ')
        if dataset.lower() == 'none':
            break
        else:
            data += dataset.split(' ')
    for i in data:
        file.write(i+'\n')
    file.close()
    file_count()


def outputting():
    file = open('market.txt')
    data = []
    for line in file:
        data.append(line.strip())
    file.close()
    file_count()
    time.sleep(3)
    for ID in range(len(data)):
        try:
            typer('p!market buy '+data[ID])
            time.sleep(0.2)
            if ID%6 == 0:
                typer('p!confirmbuy')
        except pyautogui.FailSafeException:
            file = open('market.txt','w')
            data = data[data.index(data[ID]):]
            for i in data:
                file.write(i+'\n')
            file.close()
            file_count()
            return None
    typer('p!confirmbuy')
    typer('p!confirmbuy')
    typer('done')


def logger():
    file = open('log.txt')
    data = []
    for line in file:
        line = line.strip()
        if '/' in line or line == '' or ' at ' in line:
            pass
        else:
            data.append(line)
    file.close()
    count = 0
    for amt in data:
        count += int(amt.split(':')[1].strip().split(' ')[0])
    mapper = ['zero','one','two','three','four','five','six','seven','eight','nine']
    text = ''
    gen = str(count)
    for i in gen:
        text += ':'+i+'_cute:'
        #text += ':'+mapper[int(i)]+':'
    print(count)
    print(text)
    file = open('log.txt','w')
    for line in data:
        file.write(line+'\n')
    file.close()

def helpcuteness(text):
	new = ''
	for i in text:
		if i.isalpha():
			new += (':'+i.upper()+'_cute:')
		elif i == ' ':
			new += '        '
	return new

def cuteify():
    while True:
        new = input('')
        pyperclip.copy(helpcuteness(new))
	



functions = {
        't': trade,
        'tt': texttrade,
        'at': amounttrade,
        'mt': multitrade,
        'p': pokemon,
        'm': market,
        'i': inputting,
        'o': outputting,
        'l': logger
        
}


def menu():
    while True:
        try:
            print(' '.join(functions.keys()))
            choice = input('choice:  ')
            if choice == 'at':
                amt = input('amount:  ')
                functions[choice](int(amt))
            elif choice == 'mt':
                user = input('user:  ')
                functions[choice](user)
            else:
                functions[choice]()
        except KeyError:
            print('\ninvalid, try again\n')
        except pyautogui.FailSafeException:
            print('\nfailsafe raised\n')
menu()







        
    












    
    

    
