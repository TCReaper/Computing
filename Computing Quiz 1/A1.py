def factors():
    n = int(input())
    for i in range(1,n+1):
        print(str(i)+":\t",end="")
        for x in range(1,i+1):
            if i%x==0:
                if x==i:
                    print(i)
                else:
                    print(x,end=" ")
factors()
