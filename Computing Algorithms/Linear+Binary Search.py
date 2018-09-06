import random

data = [1,2,3,4,5,6,7,8,9,10]

def binary(data,x):
        middleIndex = len(data)//2
        if data[middleIndex] == x:
                return middleIndex
        elif data[middleIndex] < x:
                return len(data[:middleIndex])+1 + binary(data[middleIndex+1:],x)
        else:
                return binary(data[:middleIndex],x)

def linear(data,x):
        for i in range(len(data)):
                if data[i] == x:
                        return i
        
#Binary search has a complexity of O(log n) while linear search has a complexity of O(n).
#A linear search is better used when there is very few searches needed to be done, 
#or when the data being searched through is not large
#A binary search requires the data to be sorted, but will be more efficient when 
#searching through a lot of data and thus should be used especially if a lot of sorting has to be done