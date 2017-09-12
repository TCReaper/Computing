
# Task 3.1

def LicenseKey():
      ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
      new_key = ''
      import random
      for i in range(9):
            choice = random.choice(ALPHABET)
            new_key += choice
      new_key += str(find_check(new_key))
      return new_key

def find_check(key):
      multiplier = 1
      total = 0
      for i in key:
            asc_code = ord(i)
            total += asc_code * multiplier
      total = total % 11
      if total == 10:
            total = 'X'
      return total

# Task 3.2

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

# Task 3.3

def purchase():
      new_key_type = input('TYPE OF YOUR LICENSE\n1. Single-User\n2. 3-User')
      new_key = LicenseKey()
      new_key_type_established = False
      while not new_key_type_established:
            if new_key_type == '1':
                  new_key += ' 1'
                  new_key_type_established = True
            elif new_key_type == '2':
                  new_key += ' 3 1'
                  new_key_type_established = True
            else:
                  print('Input valid option :)')
      
      
            
            
            
      
      

