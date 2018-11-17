def input_validate():
    validated = False
    hexDigit = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    while not validated:
        hexNumber = input("Please enter a hexadecimal number: ")
        valid = True
        for i in range(len(hexNumber)):
            if hexNumber[i] not in hexDigit:
                print("The input is not a valid hexadecimal number.")
                valid = False
                break
        if valid:
            validated = True
    return hexNumber 

def hex2den_digit(hexDigit):
    if hexDigit.isdigit():
        return int(hexDigit)
    else:
        return ord(hexDigit) - ord('A') + 10

def hex2den(hexNumber):
    denValue = 0
    for i in range(len(hexNumber)):
        denValueDigit = hex2den_digit(hexNumber[i])
        print(denValueDigit)
        denValue = denValue * 16 + denValueDigit
    return denValue 

print(hex2den(input_validate()))

def den2hex(denNumber):
    hexNumber = "" 
    while denNumber != 0:
        digit = denNumber % 16
        if digit < 10:
            hexNumber = str(digit)+hexNumber
        else:
            hexNumber = chr(ord("A")+digit-10)+hexNumber
        denNumber //= 16
    return hexNumber

print(den2hex(int(input("Please enter a denary number: "))))
