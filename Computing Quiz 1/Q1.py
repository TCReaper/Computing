# 2017 - Term 1 - SH1 Computing Practical Quiz
# Code for Q1


##    index = n - 1'
##    while n > 0:
##        num.append(n)
##        n -= 1
##    print(num)
##
##
##    while n > 0:
##        print(str(step),":",end="     ")
##        opn = n
##        while opn > 1:
##            print(str(opn)+",",end=" ")
##            opn -= 1
##        print(str(opn))
##        
##
##
##
##        n -= 1
##        step += 1

n = int(input("Integer:  "))
step = 1
change = 1

while step<=n:
    print(str(step),":\t",end="")
    div = 1
    while div<change:
        if change % div == 0:
            print(str(div)+",",end=" ")
        div += 1
    print(str(div))
    change += 1
    step += 1
