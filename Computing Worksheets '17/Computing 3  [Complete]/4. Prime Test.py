
import time

# test if integer is a prime number





def check(n):
        f = open("4. alistofprimes.txt")
        if n>=999984:
                for i in range(2,500001):
                        if int(n) % i == 0:
                                f.close()
                                return False
                f.close()
                return True
        
##                for number in f:
##                        i = len(number)-2
##                        num = ""
##                        while number[i] != "\n":
##                                num = number[i] + num
##                                i -= 1
##                        if int(n) % int(num) == 0:
##                                f.close()
##                                return False
##                        elif int(n)/2==int(num):
##                                f.close()
##                                return True

        else:
                for number in f:
                        i = len(number)-2
                        num = ""
                        while number[i] != "\n":
                                num = number[i] + num
                                i -= 1
                        if str(num) == str(n):
                                f.close()
                                return True
                        else:
                                if int(num)>int(n):
                                        f.close()
                                        return False

continute_processing = True
while continute_processing:
        print(" ")
        print(" ")
        c = ""
        try:
                n = int(input("Input integer to test:    "))
                print(check(n))
                c = input("Continue?   Y/N:    ")
        except:
                print("Not an integer!")
        print(" ")
        if str("n") in c.lower():
                continute_processing = False
