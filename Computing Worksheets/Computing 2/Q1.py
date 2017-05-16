import sys
sys.setrecursionlimit(100000)

def multiply(multiplier, multiplicand):

        # base case zero
        if multiplier == 0 or multiplicand == 0:
                return 0
        
        else:
                if multiplier < 0:
                        if multiplicand < 0:
                        # -a * -b
                                multiplier = abs(multiplier)
                                multiplicand = abs(multiplicand)

                        else:
                        # -a * +b
                                temp = multiplier
                                multiplier = multiplicand
                                multiplicand = temp
                                
                else:
                        if multiplicand < 0:
                          # +a * -b
                                pass
                        else:
                          # +a * +b
                                pass

                return multiplicand + multiply(multiplier - 1, multiplicand)

continute_processing = False
while continute_processing:
        print(" ")
        print(" ")
        a = int(input("Multiplier:    "))
        b = int(input("Multiplicand:    "))

        print(str(a) + " times " + str(b) + " equals " + str(multiply(a,b)))
        print(" ")
        c = input("Continue?   Y/N:    ")
        if c.lower() in ["n", "no"]:
                print("End.")
                continute_processing = False
