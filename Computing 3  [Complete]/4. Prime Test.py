
import time

# test if integer is a prime number


f = open("4. alistofprimes.txt")


def check(n):
        if n>=999984:
                for number in f:
                        i = len(number)-2
                        num = ""
                        while number[i] != "\n":
                                num = number[i] + num
                                i -= 1
                        if int(n) % int(num) == 0:
                                return False
                        elif int(n)/2==int(num):
                                return True

        else:
                for number in f:
                        i = len(number)-2
                        num = ""
                        while number[i] != "\n":
                                num = number[i] + num
                                i -= 1
                        if str(num) == str(n):
                                return True
                        else:
                                if int(num)>int(n):
                                        return False

continute_processing = True
while continute_processing:
        print(" ")
        print(" ")
        n = int(input("Input integer to test:    "))
        print(check(n))
        print(" ")
        c = input("Continue?   Y/N:    ")
        if str("n") in c.lower():
                continute_processing = False
