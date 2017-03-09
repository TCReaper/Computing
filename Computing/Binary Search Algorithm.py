import random

data = []


def generate():
        global n
        global data
        while len(data) < n:
                temp = random.randint(0, n)
                if temp in data:
                        continue
                else:
                        data.append(temp)
n = int(input("What's n:  "))

generate()
print(data)
data.sort()
print(data)


x = int(input("What is the x to search for:  "))

def binary(data):
        global x
        middleIndex = len(data)//2
        if data[middleIndex] == x:
                return middleIndex
        elif data[middleIndex] < x:
                return binary(data[middleIndex+1:])
        else:
                return binary(data[:middleIndex])

print(binary(data))

