

# power to power

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
                                
                                multiplier,multiplicand = multiplicand,multiplier

                                
                else:
                        if multiplicand < 0:
                          # +a * -b
                                pass
                        else:
                          # +a * +b
                                pass

                return multiplicand + multiply(multiplier - 1, multiplicand)

def power(x,n):
      answer = x
      if x == 0:
            return 0
      elif n == 0 or x == 1:
            return 1
      
##      elif n == 1:
##            return x
##      elif n == 2:
##            return multiply(answer,answer)
##      elif n == 3:
##            return multiply(answer,multiply(answer,answer))

      return multiply(answer,power(x,n-1))
