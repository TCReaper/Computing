# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Sze Shao Hong's Code for Task 2

def check_prime(n):
    file = open("PRIME_NUMBERS.TXT","r")
    primes = []
    for line in file:
        temp = line.split()
        for num in temp:
            primes.append(int(num))
    file.close()

    #iterative binary search
    while True:
        temp = primes[len(primes)//2]

        if len(primes) == 1 and n != primes[0]:
            print(n,"is not a prime number within 1,000,000")
            break
        if n == temp:
            print(n,"is a prime")
            break
        elif n > temp:
            primes = primes[(len(primes)//2):]
        else:
            primes = primes[:len(primes)//2]
    
check_prime(int(input("Enter a number n: ")))
