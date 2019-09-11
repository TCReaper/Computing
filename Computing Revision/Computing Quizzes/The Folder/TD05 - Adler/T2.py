# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 2

def check_prime(n):
    a = []
    f = open("PRIME_NUMBERS.TXT", "r")
    for i in f:
        a.append(i.strip())
    f.close()
    if str(n) in a:
        print(str(n) + " is prime")
    else:
        print(str(n) + " is not prime")
