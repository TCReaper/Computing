def converter(denaryNum, binaryNum):
    if denaryNum == 0 or denaryNum == 1:
        return str(denaryNum) + binaryNum
    else:
        binaryNum = str(denaryNum%2) + binaryNum
        return converter(denaryNum // 2, binaryNum)

def converter_helper(denaryNum):
    for i in range(len(denaryNum)):
        if not (denaryNum[i].isdigit() or denaryNum[i]=='-' and i==0):
            print("The enetered value is not a denary number.")
            return
    if denaryNum[0] == '-':
        print("-"+converter(-int(denaryNum),""))
    else:
        print(converter(int(denaryNum),""))

n = input("Please enter a denary number: ")
converter_helper(n)

"""
normal case: 56
boundary case: 0
erroneous case:"abc" 

"""
