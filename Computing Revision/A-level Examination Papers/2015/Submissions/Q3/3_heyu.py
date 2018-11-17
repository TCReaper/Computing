import random

def LicenseKey():
    licenceKey = ""
    checksum = 0
    for i in range(9):
        letter = random.randint(0,25)+ord('A')
        licenceKey += chr(random.randint(0,25)+ord('A'))
        checksum += letter * (i+1)
    checksum = checksum % 11
    if checksum < 10:
        licenceKey += str(checksum)
    else:
        licenceKey += "X"
    return licenceKey

endProgram = False
three_user_license = [] 
file = open("LICENCE-KEYS.TXT","a+") 
while not endProgram:
    print("1. Purchase of a new license for either a single-user or a 3-user license.")
    print("2. Register an additional user to an active 3-user license.")
    print("3. End.")
    n = int(input("Please enter an option: "))
    if n == 1:
        print("1. single-user")
        print("2. 3-user")
        k = int(input("Please choose an option: "))
        if k == 1:
            newlicense = LicenseKey()
            print("New licensekey is: ", newlicense)
            writeline = newlicense + " 1\n"
            file.write(writeline)
        elif k == 2:
            newlicense = LicenseKey()
            print("New licensekey is: ", newlicense)
            writeline = newlicense + " 3 1\n"
            file.write(writeline)
            three_user_license.append([newlicense,"user1"])
    elif n == 2:
        name = input("Please enter the new user's name: ")
        for i in range(len(three_user_license)):
            if len(three_user_license[i]) < 4:
                three_user_license[i].append(name) 
    else:
        endProgram = True
file.close()
        
            
            
            
    
