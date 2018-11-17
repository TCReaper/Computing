##2.1
##A: CheckDigit <- CalCheckDigit(NewNumber, Total)
##B: RETURN STRING(X)
##C: RETURN STRING(Number + CheckDigit)

def CalCheckDigit(Number, Total): #returns STR
    if len(Number) > 1:
        Digit = int(Number[0])
        Total += Digit * (len(Number) + 1)
        NewNumber = Number[1:]
        CheckDigit = CalCheckDigit(NewNumber, Total)
        
    else:
        Digit = int(Number[0])
        Total += Digit * (len(Number) + 1)
        CalcModulus = Total % 11
        CheckValue = 11 - CalcModulus
        if CheckValue == 11:
            return '0'
        else:
            if CheckValue == 10:
                return 'X'
            else:
                return str(CheckValue)
    
    if len(Number) == 9:
        return str(Number) + CheckDigit
    
    else:
        return CheckDigit
    
f = open("ISBNPRE.txt")
for line in f:
    print(CalCheckDigit(line.strip(), 0))
f.close()


#Time Taken: 20.18.60
#Time Allowed: 20.25.00
