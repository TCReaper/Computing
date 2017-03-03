

#               Vending Machine

inputting = True
while inputting:
        try:
                tenC = int(input("How many 10 cent coins do you insert:    "))*10
                twentyC = int(input("How many 20 cent coins do you insert:    "))*20
                fiftyC = int(input("How many 50 cent coins do you insert:    "))*50
                dollar = int(input("How many 1 dollar coins do you insert:    "))*100
                print("")
                drink = int(float(input("What is the price of the drink? [0.80, 1.20]:     $"))*100)
                inputting = False
        except ValueError:
                print("Please only input integers !")
                print("")


##        tenC = 10 * tenC
##        twentyC = 20 * twentyC
##        fiftyC = 50 * fiftyC
##        dollar = 100 * dollar
##        drink = int(100 * drink)


total = tenC + twentyC + fiftyC + dollar
optotal = total / 100
change = total - drink
opchange = change / 100
print("Total cash inserted:   $" + str(optotal)+"0" )
print("Returning $" + str(opchange)+"0" + " of change, in the form of:")
