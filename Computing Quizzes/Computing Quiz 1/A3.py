

continute = True
while continute:
        num = input("Number or \"X\" to stop:  ")
        if num.lower() == "x":
                continute = False
        else:
                try:
                        num = float(num)
                except ValueError:
                        print("Rational number only dude..")
                else:
                        f = open("INPUT.txt","a")
                        f.write(num)
                        f.close()
                
