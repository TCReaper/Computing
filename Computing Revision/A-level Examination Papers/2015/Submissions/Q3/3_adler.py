import random

def LicenceKey():
    lic_key = ''
    check_digit = 0
    for i in range(1, 10):
        temp = random.randint(65,90)
        lic_key += chr(temp)
        check_digit += i * temp
    check_digit = str(check_digit % 11)
    if check_digit == '10':
        check_digit = 'X'
    
    return lic_key + check_digit

def content(file):
    f = open(file)
    temp = f.read()
    f.close()
    return temp.split('\n')

def print_content(file):
    for i in content(file):
        print(i)

def check_choice(choice):
    if not choice.isdigit():
        return False
    elif int(choice) not in range(1, 4):
        return False
    return True

def get_index(lic_key, data):
    for i in range(len(data)):
        if len(data[i]) == 14:
            if data[i][:10] == lic_key:
                return i
    return -1

def check_lic_type(lic_type):
    if not lic_type.isdigit():
        return False
    elif int(lic_type) != 1 and int(lic_type) != 3:
        return False
    return True

def menu():
    while True:
        choice = input("1.  Purchase of a new licence for either a single-user"\
                       " or a 3-user licence\n"\
                       "2.  Register an additional user to an active 3-user"\
                       " licence\n"\
                       "3.  End\n")
        if not check_choice(choice):
            print("Invalid input! Enter 1, 2 or 3 corresponding to the desired"\
                  " option. Try again.\n")
        else:
            choice = int(choice)
            if choice == 3:
                #break
                return
            if choice == 1:
                while True:
                    lic_type = input("Licence key type (1 or 3)\n")
                    if not check_lic_type(lic_type):
                        print("Invalid input! Select either 1 or 3! Try again.\n")
                    else:
                        lic_key = LicenceKey()
                        print("Licence key: " + lic_key)
                        f = open("LICENCE-KEYS.TXT", 'a')
                        f.write(lic_key + ' ' + lic_type)
                        if lic_type == '3':
                            f.write(' 0')
                        f.write('\n')
                        f.close()
                        print_content('LICENCE-KEYS.TXT')
                        break
                
            elif choice == 2:
                while True:
                    lic_key = input("Licence key:\n")
                    data = content('LICENCE-KEYS.TXT')
                    index = get_index(lic_key, data) #get_3_user_lic_key_index
                    if index == -1:
                        print("Invalid licence key. Try again.\n")
                    else:
                        if data[index][-1] == '3':
                            print("All 3 users activated already!"\
                                  " Purchase a new licence key with option 1"\
                                  " to proceed with activation.\n")
                        else:
                            data[index] = data[index][:-1]\
                                          + str(int(data[index][-1]) + 1)
                            f = open("LICENCE-KEYS.TXT", 'w')
                            f.write('\n'.join(data))
                            f.close()
                            print_content('LICENCE-KEYS.TXT')
                            break


menu()




class Licence():
    def __init_(self, licence_key, purchase_date, purchaser_name):
        self._licence_key = licence_key
        self._purchase_date = purchase_date
        self._purchaser_name = purchaser_name

class Single_User_Registration(Licence):
    def __init__(self, licence_key, purchase_date, purchaser_name):
        super().__init__(licence_key, purchase_date, purchaser_name)
        self._licence_type = 1

class Three_User_Registration(Licence):
    def __init__(self, licence_key, purchase_date, purchaser_name):
        super().__init__(licence_key, purchase_date, purchaser_name)
        self._licence_type = 3


#Time Taken: 1.00.18.08
#Time Allowed: 54.00.00
