

# Positive Integers

kai = open("2. n.txt", "r")
n = int(kai.read())
kai.close()

m = int(input("Gimme another integer:    "))
o = n+m
current = n+1

numList = []

while current <= o:
        numList.append(current)
        current += 1

ded = open("1. PosiSquares.txt", "a")
for i in numList:
        ded.write("\n" + str(i))
ded.close()
