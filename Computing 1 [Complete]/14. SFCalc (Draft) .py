
###############################################################

def sfcalctest():
        number = input("Type in a number or integer:     ")
        str(number)
        count = len(str(number))

        if number.count("-") == 1:
                count = count - 1
                if number.count(".") == 1:
                        count = count - 1
                        print( "The number of significant figures in " + str(number) + " is "+ str(count) )
                else:        
                        print( "The number of significant figures in " + str(number) + " is "+ str(count) )

        else:
                if number.count(".") == 1:
                        count = count - 1
                        print( "The number of significant figures in " + str(number) + " is "+ str(count) )
                else:        
                        print( "The number of significant figures in " + str(number) + " is "+ str(count) )

###############################################################

def sfconverttest():
        iniNum = input("Type in a number or integer:     ")
        str( iniNum)
        count = len(str(iniNum))
        str(count)
        convertsf = input("How many significant figures would you like?    ")
        str(convertsf)

        if iniNum.count("-") == 1:
                print("NO NEGATIVES TRY AGAIN")
        elif count > convertsf:
                changesf = count - convertsf
                removesf = convertsf + 1
                iniNum = iniNum[:removesf]
                print( iniNum)

###############################################################

def test():
        zer = str("0") * 5
        print(zer)

###############################################################

def sfcalc():
        import time
        number = input("Type in a number or integer:    ")
        number = str(number)
        count = len(number)

        if number == "0":
                time.sleep(1)
                print("Zero isn't an interesting number...")
        elif number.count("-") == 1:
                if number.count(".") == 0:
                        # checks if it is an integer
                        
                        print("This is an integer.")
                        zero = 1
                        countsf = count -1
                        while  number[countsf] == "0" and countsf>=0:
                                zero += 1
                                countsf = countsf - 1
                        time.sleep(1.25)
                        print("Number of significant figures in " + str(number) + " is calculated to be " + str(count - zero))

                elif  number.count(".") == 1:
                        # checks if it is a float
                        
                        decimal = number.index(".")
                        zero = 2   # start at one to account for decimal point
                        
                        # the last zero (eg in 0.00350) tells us that the measurement was made
                        # accurate to that last digit, which just happened to have a value of zero,
                        # so is the code below needed?
                       
                        #countsf = count -1
                        #while  number[countsf] == "0" and countsf>=decimal:
                        #        zero += 1
                        #        countsf = countsf - 1
                        
                        
                        if "1" in number[0:decimal] or "2" in number[0:decimal] or "3" in number[0:decimal] or \
                           "4" in number[0:decimal] or "5" in number[0:decimal] or "6" in number[0:decimal] or \
                           "7" in number[0:decimal] or "8" in number[0:decimal] or "9" in number[0:decimal]:
                                
                                print("This is a float value.")
                                time.sleep(1.25)
                                print("Number of significant figures in " + str(number) + " is calculated to be " + str(count - zero))
                                
                        else:
                                # calculates significant figure count for non whole number floats
                                zero = 2
                                countsf = decimal + 1
                                while number[countsf] == "0":
                                        zero += 1
                                        countsf = countsf + 1
                                zeros = number[:decimal].count("0")
                                print("This is a float value with a value lower than 1.")
                                time.sleep(1.25)
                                print("Number of significant figures in " + str(number) + " is calculated to be " + str(count - zero - zeros))
                
        elif number.count(".") == 0:
                # checks if it is an integer
                
                print("This is an integer.")
                zero = 0
                countsf = count -1
                while  number[countsf] == "0" and countsf>=0:
                        zero += 1
                        countsf = countsf - 1
                time.sleep(1.25)
                print("Number of significant figures in " + str(number) + " is calculated to be " + str(count - zero))

        elif  number.count(".") == 1:
                # checks if it is a float
                
                decimal = number.index(".")
                zero = 1   # start at one to account for decimal point
                
                # the last zero (eg in 0.00350) tells us that the measurement was made
                # accurate to that last digit, which just happened to have a value of zero,
                # so is the code below needed?
               
                #countsf = count -1
                #while  number[countsf] == "0" and countsf>=decimal:
                #        zero += 1
                #        countsf = countsf - 1
                
                
                if "1" in number[0:decimal] or "2" in number[0:decimal] or "3" in number[0:decimal] or \
                   "4" in number[0:decimal] or "5" in number[0:decimal] or "6" in number[0:decimal] or \
                   "7" in number[0:decimal] or "8" in number[0:decimal] or "9" in number[0:decimal]:
                        
                        print("This is a float value.")
                        time.sleep(1.25)
                        print("Number of significant figures in " + str(number) + " is calculated to be " + str(count - zero))
                        
                else:
                        # calculates significant figure count for non whole number floats
                        
                        countsf = decimal + 1
                        while number[countsf] == "0":
                                zero += 1
                                countsf = countsf + 1
                        zeros = number[:decimal].count("0")
                        print("This is a float value with a value lower than 1.")
                        time.sleep(1.25)
                        print("Number of significant figures in " + str(number) + " is calculated to be " + str(count - zero - zeros))

###############################################################
        
def sfconvert():
        import time
        number = input("Type in a number or integer:    ")
        number = str(number)
        count = len(number)
        time.sleep(0.7)
        change = input("How many significant figures do you want?    ")

        if number == "0":
                time.sleep(1)
                print("Zero isn't an interesting number...")

        elif number.count(".") == 0:
                # checks if it is an integer
                
                print("This is an integer.")
                zero = 0
                countsf = count -1
                
                while  number[countsf] == "0" and countsf>=0:
                        zero += 1
                        countsf = countsf - 1
                time.sleep(1.25)
                
                final = count - zero
                print("Number of significant figures in " + str(number) + " is calculated to be " + str(final))
                final2 = final - zero
                
                if int(final) < int(change):
                        # correction if there is an increase in s.f.
                        tochange = int(change) - int(final)
                        finalnum = ( str(number) + str(".") + (str("0") * tochange) )
                        time.sleep(1.5)
                        print("There is a difference of " + str(tochange) + " significant figures...")
                        time.sleep(0.75)
                        print("Making Changes...")
                        time.sleep(2)
                        print("Adding Zeros...")
                        time.sleep(1)
                        print( str(number) + " with " + str(final) + " s.f. has been corrected to " + str(finalnum) + " with " + str(change) + " s.f. !")

                        
                elif int(final) > int(change):
                        # correction if there is a decrease in s.f.
                        tochange = int(final) - int(change)
                        axis = number[int(change)]
                        nineCheck = (int(change) - 1)
                        nineWatch = number[int(nineCheck)]
                        if int(axis) < 5:
                                # round down
                                number2 = number[:int(change)]
                                finalnum = (number2 + str("0") * int(tochange))
                                time.sleep(1.5)
                                print("There is a difference of " + str(tochange) + " significant figures...")
                                time.sleep(0.75)
                                print("Making Changes...")
                                time.sleep(2)
                                print("Rounding Down...")
                                time.sleep(1)
                                print( str(number) + " with " + str(final) + " s.f. has been corrected to " + str(finalnum) + " with " + str(change) + " s.f. !")
                                
                        elif int(axis) >= 5:
                                # round up
                                if str(nineWatch) == "9":
                                        # check to account for 9 change to 10
                                        beforeNine = (int(change) - 2)
                                        plusOne = number[int(beforeNine)]
                                        plusOne = int(plusOne) + 1
                                        number2 = number[:beforeNine]
                                        addZero = len(number[int(tochange):])
                                        finalnum = str(number2) + str(plusOne) + ("0" * addZero)
                                        time.sleep(1.5)
                                        print("There is a difference of " + str(tochange) + " significant figures...")
                                        time.sleep(0.75)
                                        print("Making Changes...")
                                        time.sleep(2)
                                        print("Rounding Up...")
                                        time.sleep(1)
                                        print( str(number) + " with " + str(final) + " s.f. has been corrected to " + str(finalnum) + " with " + str(change) + " s.f. !")
                                        time.sleep(1.75)
                                        print( "Note: The true s.f. of the result is actually " + str( int(change) - 1 ) + " s.f. ! " )
                                
                                else:
                                        # normal round up
                                        axis = number[int(change) - 1]
                                        axis = int(axis) + 1
                                        change2 = int(change) - 1
                                        number2 = number[:int(change2)]
                                        tochange2 = tochange - zero
                                        finalnum = (number2 + str(axis) + str("0") * ( int(tochange)) )
                                        time.sleep(1.5)
                                        print("There is a difference of " + str(tochange2) + " significant figures...")
                                        time.sleep(0.75)
                                        print("Making Changes...")
                                        time.sleep(2)
                                        print("Rounding Up...")
                                        time.sleep(1)
                                        print( str(number) + " with " + str(final2) + " s.f. has been corrected to " + str(finalnum) + " with " + str(change) + " s.f. !")                                
                                        

                        
                else:
                        time.sleep(3)
                        return "  No change is required :D  "

################################################### INTEGERS WORK #########################
                        
        elif  number.count(".") == 1:
                # checks if it is a float
                # change, tochange
                
                decimal = number.index(".")
                final = count - 1
                
                if "1" in number[0:decimal] or "2" in number[0:decimal] or "3" in number[0:decimal] or \
                   "4" in number[0:decimal] or "5" in number[0:decimal] or "6" in number[0:decimal] or \
                   "7" in number[0:decimal] or "8" in number[0:decimal] or "9" in number[0:decimal]:

                        print("This is a float value.")
                        time.sleep(1.25)
                        print("Number of significant figures in " + str(number) + " is calculated to be " + str(final))
                        ddecimal = decimal + 1
                        dnumber = number[:decimal] + number[ddecimal:]

                        if int(final) < int(change):
                                # correction if there is an increase in s.f.
                                tochange = int(change) - int(final)
                                finalnum = ( str(dnumber) + (str("0") * tochange) )
                                time.sleep(1.5)
                                print("There is a difference of " + str(tochange) + " significant figures...")
                                time.sleep(0.75)
                                print("Making Changes...")
                                time.sleep(2)
                                finalnum = finalnum[:decimal] + finalnum[decimal:]
                                print("Adding zeros...")
                                time.sleep(1)
                                print( str(number) + " with " + str(final) + " s.f. has been corrected to " + str(finalnum) + " with " + str(change) + " s.f. !")

                                
                        elif int(final) > int(change):
                                # correction if there is a decrease in s.f.
                                tochange = int(final) - int(change)
                                axis = number[int(change)]
                                if int(axis) < 5:
                                        # round down
                                        number2 = dnumber[:int(change)]
                                        finalnum = (number2 + str("0") * int(tochange))
                                        time.sleep(1.5)
                                        print("There is a difference of " + str(tochange) + " significant figures...")
                                        time.sleep(0.75)
                                        print("Making Changes...")
                                        time.sleep(2)
                                        zero = 0
                                        countsf = final -1
                                        finalnum = finalnum[:decimal] + "." + finalnum[decimal:]
                                        while  finalnum[countsf] == "0" and countsf>=0:
                                                zero += 1
                                                countsf = countsf - 1
                                        zeroerror = final - zero
                                        finalnum = finalnum[:zeroerror]
                                        print("Rounding Down...")
                                        time.sleep(1)
                                        print( str(number) + " with " + str(final) + " s.f. has been corrected to " + str(finalnum) + " with " + str(change) + " s.f. !")
                                        
                                elif int(axis) >= 5:
                                        # round up
                                        axis = dnumber[int(change) - 1]
                                        axis = int(axis) + 1
                                        change2 = int(change) - 1
                                        number2 = dnumber[:int(change2)]
                                        tochange2 = tochange
                                        finalnum = (number2 + str(axis) + str("0") * ( int(tochange)) )
                                        time.sleep(1.5)
                                        print("There is a difference of " + str(tochange2) + " significant figures...")
                                        time.sleep(0.75)
                                        print("Making Changes...")
                                        time.sleep(2)
                                        zero = 0
                                        countsf = final - 1
                                        finalnum = finalnum[:decimal] + "." + finalnum[decimal:]
                                        while  finalnum[countsf] == "0" and countsf>=0:
                                                zero += 1
                                                countsf = countsf - 1
                                        zeroerror = final - zero
                                        finalnum = finalnum[:zeroerror]
                                        print("Rounding Up...")
                                        time.sleep(1)
                                        print( str(number) + " with " + str(final) + " s.f. has been corrected to " + str(finalnum) + " with " + str(change) + " s.f. !")
                                        
#################################################FLOATS MORE THAN ZERO WORK#############


                elif number[0] == "0":
                        # calculates significant figure count for non whole number floats
                        zero = 1
                        countsf = decimal + 1
                        while number[countsf] == "0":
                                zero += 1
                                countsf = countsf + 1
                        zeros = number[:decimal].count("0")
                        time.sleep(0.75)
                        print("This is a float value with a value lower than 1.")
                        time.sleep(1.25)
                        lastPart = count - zero - zeros
                        print("Number of significant figures in " + str(number) + " is calculated to be " + str(lastPart))
                        
                        if int(lastPart) < int(change):
                                # add zero onli
                                time.sleep(1.5)
                                hearsay = int(change) - int(lastPart)
                                print("There is a difference of " + str(hearsay) + " significant figures...")
                                time.sleep(0.75)
                                print("Making Changes...")
                                time.sleep(2)
                                finalnum = number + ("0" * hearsay)
                                print( str(number) + " with " + str(lastPart) + " s.f. has been corrected to " + str(finalnum) + " with " + str(change) + " s.f. !")

                        elif int(lastPart) > int(change):
                                time.sleep(1.5)
                                hearsay = int(lastPart) - int(change)
                                print("There is a difference of " + str(hearsay) + " significant figures...")
                                time.sleep(0.75)
                                print("Making Changes...")
                                time.sleep(2)
                                deletion = count - hearsay
                                changer = deletion - 1
                                axis = number[int(changer) + 1]
                                if int(axis) < 5:
                                        finalnum = number[:int(deletion)]
                                        print("Rounding Down...")
                                        time.sleep(1)
                                        print(finalnum)

                                if int(axis) >= 5:
                                        finalnum = number[:int(changer)]
                                        exis = int( number[int(changer)] ) + 1
                                        finalnum = str(finalnum) + str(exis)
                                        print("Rounding Up...")
                                        time.sleep(1)
                                        print(finalnum)
                                        

                                
                                        
                                        
        






































        
