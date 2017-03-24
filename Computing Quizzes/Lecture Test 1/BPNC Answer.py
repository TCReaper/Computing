# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 2

def check_prime(n):
    r = open("PRIME_NUMBERS.TXT","r")
    primes=[]
    for line in r:
        primes = primes + line.strip().split()
    r.close()

    check = int(n)

    search_ded = True
    current_list = primes
    while search_ded:
        if len(current_list) == 0:
            search_ded = False
        else:
            if int(current_list[len(current_list)//2]) == check:
        
