import random

def is_valid_ISBN10(isbn10):
    digits = []
    for i in range(len(isbn10)):
        digits.append(int((isbn10[i]) if isbn10[i]!= "X" else 10)*(10-i))
    return sum(digits)%11 == 0

print(is_valid_ISBN10("0306406152")) #Valid ISBN-10, True
print(is_valid_ISBN10("0306406153")) #Wrong check digit, False
print(is_valid_ISBN10("030640615X")) #Wrong check digit, False
print(is_valid_ISBN10("9971502100")) #Valid ISBN-10, True
print(is_valid_ISBN10("8175257660")) #Valid ISBN-10, True

def possible_ISBN(isbn):
    mc = [] # md missing digits
    for i in range(len(isbn)):
        if isbn[i] == "?":
            mc.append(i)
    poss_char = ["0","1","2","3","4","5","6","7","8","9"]
    poss_last_char = ["0","1","2","3","4","5","6","7","8","9", "X"]
    #poss_char = ["2","3","8","9"]# For mary case use this

    result = [""]
    for pos in mc:
        temp = []
        for combi in result:
            if pos != 9:
                for char in poss_char:
                    temp.append(combi + isbn[len(combi):pos] + char)
            else:
                for char in poss_last_char:
                    temp.append(combi + isbn[len(combi):pos] + char)                
        result = temp

    temp = []
    for combi in result:
        temp.append(combi + isbn[len(combi):])
    result = temp
    return list(filter(lambda x: is_valid_ISBN10(x), result))
    #return result

print(possible_ISBN("9971222???"))
print()
print(len(possible_ISBN("9971??23?X")))
print()
print(possible_ISBN("8175?5?9?6"))
print()
