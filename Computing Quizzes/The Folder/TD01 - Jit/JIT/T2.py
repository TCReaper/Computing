# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 2
n_int  = int(input("Please enter a number:"))

def check_prime(n):
    file = open("PRIME_NUMBERS.TXT", "r")
    data = file.read()
    primes = data.split()

    l = len(primes)
    l1 = int(l/2)
    if data[l1] > n:
        primes = primes[]

#I'm sorry halp file i/o :(
check_prime(n_int)
