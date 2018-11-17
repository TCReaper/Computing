def Converter(DenaryNumber):
    if DenaryNumber == 0 or DenaryNumber == 1:
        print(str(DenaryNumber))
    else:
        print(str(DenaryNumber % 2), end = '')
        Converter(DenaryNumber // 2)

Converter(56)

#order is reversed, converting output back to denary will not give 56

def Converter(DenaryNumber):
    BinaryNumber = ''
    convert = True
    while convert:
        if DenaryNumber > 1:
            BinaryNumber = str(DenaryNumber % 2) + BinaryNumber
            DenaryNumber = DenaryNumber // 2
        else:
            BinaryNumber = str(DenaryNumber) + BinaryNumber
            convert = False
    return BinaryNumber

print(Converter(56))
        
#10

    
