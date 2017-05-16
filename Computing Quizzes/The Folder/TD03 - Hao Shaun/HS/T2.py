# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 2

def check_prime(n):
    primes = []
    f = open("PRIME_NUMBERS.TXT")
    g = f.read().split("\n")
    for o in g:
        i = o.split()
        for u in i:
            if int(n) == int(u):
                print( "n is a prime" )
            elif int(n) % int(u) == 0:
                print( "n is not a prime" )

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

