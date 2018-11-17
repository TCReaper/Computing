#3.1-3.2
from random import randint
def LicenceKey():
    Total = 0
    Key = ''
    for i in range(1,10):
        value = randint(65,90)
        Key += chr(value)
        Total += value * i
    Check = Total % 11
    Key += str(Check)
    return Key

for j in range(3):
    print(LicenceKey())
    
#3.3
Keys = []
f = open('LICENCE-KEYS.txt')
for i in f:
    i = i.strip()
    Keys.append(i.split(' '))
f.close()
                
Cont = True
while Cont:
    Option = input('1. Purchase of a new licence for either a single-user or a 3-user licence\n2. Register an additional user to an active 3-user licence\n3. End\n')
    if Option == '1':
        LicenceType = input('Enter licence type: ')
        if LicenceType == '1':
            Keys.append([LicenceKey(), 1])
            ToAdd = str(LicenceKey()) + ' 1\n'
        else:
            Keys.append([LicenceKey(), 3, 1])
            ToAdd = str(LicenceKey()) + ' 3 1\n'
        f = open('LICENCE-KEYS.txt', 'a')
        f.write(ToAdd)
        f.close()

        g = open('LICENCE-KEYS.txt')
        for j in g:
            j = j.strip()
            print(j)
        g.close()
        
    elif Option == '2':
        Entry = input('Enter existing Licence: ')
        for k in range(len(Keys)):
            if Entry in Keys[k]:
                Keys[k] = [Keys[k][0], Keys[k][1], int(Keys[k][2]) + 1]
                break
                
        f = open('LICENCE-KEYS.txt', 'w')
        for l in Keys:
            for m in l:
                f.write(str(m) + ' ')
            f.write('\n')
        f.close()

        g = open('LICENCE-KEYS.txt')
        for n in g:
            print(n.strip())
        g.close()
    else:
        Cont = False

#3.5
class Licence():
    def __init__(self, LicenceKey, LicenceType, PurchaseDate, Name):
        self._LicenceKey = LicenceKey
        self._LicenceType = LicenceType
        self._PurchaseDate = PuchaseDate
        self._Name = Name

class SingleUser(Licence):
    def __init__(self, MACAddress, RegistrationDate):
        super.__init__()
        self._MACAddress = MACAddress
        self._RegistrationDate = RegistrationDate

class ThreeUser(Licence):
    def __init__(self, MACAddress, RegistrationDate):
        super.__init__()
        self._MACAddress1 = MACAddress
        self._MACAddress2 = None
        self._MACAddress3 = None
        slef._RegistrationDate1 = RegistrationDate
        self._RegistrationDate2 = None
        self._RegistrationDate3 = None

#50



                

    
        
