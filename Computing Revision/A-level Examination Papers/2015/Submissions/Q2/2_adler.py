##def Converter(DenNum):
##    if DenNum == 0 or DenNum == 1:
##        print(DenNum)
##    else:
##        print(DenNum % 2)
##        Converter(DenNum // 2)


#error is with printing, it should be backwards, so it should add to the result
#to print instead of actually printing

def Converter(DenNum, result = ''):
    if DenNum == 0 or DenNum == 1:
        return str(DenNum) + result
    else:
        result = str(DenNum % 2) + result
        return Converter(DenNum // 2, result)
        

#(Excluding test cases)       
#Time Taken: 7.10.74
#Time Allowed: 13.30.00 (assuming total of 10 marks)
