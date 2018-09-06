
import random

def LicenseKey():
      mapping = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
      key = ''
      for i in range(9):
            choice = random.choice(ALPHABET)
            key += choice
      key += str(find_check(key))
      return key

def find_check(key):
      total = 0
      for i in range(len(key)):
            asc = ord(key[i])
            total += asc * (i+1)
      total = total % 11
      if total == 10:
            total = 'X'
      return total

def menu():
      options = [None,'Purchase of a new license for either a single-user or a 3-user license'
                 ,'Register an additional user to an active 3-user license','End']
      for i in range(1,4):
            print(str(i)+'. '+options[i])
      user = input('Wthek do you want to do now...? ')
      if user == '1':
            purchase()
      elif user == '2':
            register()
      elif user == '3':
            return None
      else:
            print('Input valid option ty')

def purchase():
      key_type = input('TYPE OF YOUR LICENSE\n1. Single-User\n2. 3-User')
      key = LicenseKey()
      key_type_established = False
      while not key_type_established:
            if key_type == '1':
                  key += ' 1'
                  key_type_established = True
            elif key_type == '2':
                  key += ' 3 1'
                  key_type_established = True
            else:
                  print('Input valid option :)')
      
      
            
            
            
      
      

