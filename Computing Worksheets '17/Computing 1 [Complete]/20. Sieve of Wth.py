import datetime
from math import *

def sieveA(n):
        candidates = []
        for i in range(2, n+1):
                candidates.append(i)
        index = 0
        while index < len(candidates):
                revised = []
                for i in range(index + 1, len(candidates)):
                        if candidates[i] % candidates[index] != 0:
                                revised.append(candidates[i])
                candidates = candidates[:index + 1] + revised
                index += 1
        return candidates

def sieveB(n):
        candidates = [2]
        for i in range(3, n+1, 2):
                candidates.append(i)
        index = 0
        while index <= floor(n**0.5):
                revised = []
                for i in range(index + 1, len(candidates)):
                        if candidates[i] % candidates[index] != 0:
                                revised.append(candidates[i])
                candidates = candidates[:index + 1] + revised
                index += 1
        return candidates

n = int(input("What is n?   "))

startA = datetime.datetime.now()
primesA = sieveA(n)
endA = datetime.datetime.now()
print(len(primesA))
print( (endA-startA).total_seconds() )
startB = datetime.datetime.now()
primesB = sieveB(n)
endB = datetime.datetime.now()
print(len(primesB))
print( (endB-startB).total_seconds() )

