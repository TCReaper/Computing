# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 2

def check_prime(n):
    file=open("PRIME_NUMBERS.TXT","r")
    prime=[]
    for line in file:
        i=0
        while i<len(line):
            while line[i]==" " and i<len(line):
                i=i+1
            num=0
            while (line[i]>="0" and line[i]<="9") and i<len(line):
                num=num*10+int(line[i])
                i=i+1
            if num==0:
                break
            else:
                prime.append(num)
    l=0
    r=len(prime)-1
    NotFound=True
    while NotFound and l<=r:
        mid=(l+r)//2
        if prime[mid]>n:
            r=mid-1
        elif prime[mid]<n:
            l=mid+1
        else:
            NotFound=False
    if NotFound:
        return False
    else:
        return True

n=int(input("Please enter the number you want to check: "))        
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")
