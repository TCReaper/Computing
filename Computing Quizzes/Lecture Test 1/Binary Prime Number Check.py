# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 2

def check_prime(n):
    primes = []
    f = open("PRIME_NUMBERS.TXT")
    g = f.read().split("\n")
    f.close()
    for o in g:
        i = o.split()
        for u in i:
            if int(n) == int(u):
                return True
            elif int(n) % int(u) == 0:
                return False
                

    for o in g:
        i = o.split()
        for u in i:
            primes.append(u)
            # but crashes python?!
            # help
    storedlen = 0

    binarysearch = True
    while binarysearch:
        listlen = len(primes)
        midlen = listlen//2
        if primes[midlen] == n:
            print( "n is a prime" )
            binarysearch = False
        elif listlen < 2:
            print( "n is not a prime" )
            binarysearch = False
        elif int(primes[midlen]) < n:
            primes = primes[:midlen]
        elif int(primes[midlen]) > n:
            primes = primes[midlen:]


def b_search(l,key):
    start_i = 0
    end_i = len(l) - 1
    while (start_i < end_i):
        mid_i = ( start_i + end_i )//2
        if key > l[mid_i]:
            start_i = mid_i + 1
        elif key < l[mid_i]:
            end_i = mid_i - 1
        else:
            return True
    return False
