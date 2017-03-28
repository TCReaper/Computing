# Name: Hao Shaun

# 2017 - Term 2 - SH1 Computing Practical Lecture Test 2
# Code for Task 1

import random

makeList = True
data = []
while makeList:
    integer = input("Integer to add to list (x to stop):  ")
    if integer.lower() == "x":
        makeList = False
    else:
        data.append(int(integer))

            
def bubble(data):
    print("bubble sort")
    comparisons = 0
    for x in range(len(data)-1):
        for e in data:
            for i in range(len(data)-1):
                swap = False
                if data[i] > data[i+1]:
                    comparisons += 1
                    data[i],data[i+1]=data[i+1],data[i]
                    swap = True
            if not swap:
                break
    print(data)
    print(comparisons)

def insertion(data):
    print("insertion sort")
    comparisons = 0
    for x in range(len(data)-1):
        for i in range(1,len(data)):
            comparisons += 1
            while len(data)>i>0 and data[i] < data[i-1]:
                data[i],data[i-1]=data[i-1],data[i]
    print(data)
    print(comparisons)

bubble(data)
insertion(data)

f = open("LIST1.TXT","w")
f.close()
rand100 = []
for i in range(101):
    integer = random.randint(1,101)
    rand100.append(integer)
    f = open("LIST1.TXT","a")
    f.write(str(integer)+" ")
    f.close()
f = open("LIST2.TXT","w")
f.close()
rand100000 = []
##for i in range(100001):
##    integer = random.randint(1,101)
##    rand100000.append(integer)
##    f = open("LIST2.TXT","a")
##    f.write(str(integer)+" ")
##    f.close()
##print(rand100000)

rand100v2 = rand100
bubble(rand100)
insertion(rand100v2)


