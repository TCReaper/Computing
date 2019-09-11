# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 2
#GIDIJALA SAI RAHUL

def b_search(primes, num):
    length = len(primes)
    
    if length == 1:
        if primes[0] == num:
            return True
        else:
            return False

    if (length % 2) == 1:
        m = (length+1)//2
    else:
        m = (length)//2

    if num == primes[m]:
        return True
    elif num < primes[m]:
        return b_search(primes[:m], num)
    else:
        return b_search(primes[m:], num)

def check_prime(n):
    file_handle = open("PRIME_NUMBERS.TXT", "r")
    primes = []
    for line in file_handle.readlines():
        primes.extend([int(x) for x in line.strip().split()])

    file_handle.close()
        
    return b_search(primes, n)

print(check_prime(137))
    
