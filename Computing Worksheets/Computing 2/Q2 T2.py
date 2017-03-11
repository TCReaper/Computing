
# alt 4 to uncomment

global myList
myList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

##def fml(n):
##                return myList[int(i)] 

##n = input("Convert any positive integer to words:    ")

##for i in n:
##        print(fml(n) ,end = " ")


def kms(now, index):
        global myList
        
        if index >= len(now):
                return []
        
        else:
                return [myList[int(now[index])]] + kms(now, index+1)



now = input("Positive Integer!    ")
index = 0

res = kms(now, index)
for i in res:
        print (i, end = "  ")
        
