#

ext = 1
        
def primecheck(n, checker, ext):

        checker = int(n) - int(ext)


        if int(checker) == "0":
                return False
        
        elif int(n) % int(checker) == "0":
                return True
       
        else:
                return primecheck(n, 1, ext + 1)

# blueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

        t
