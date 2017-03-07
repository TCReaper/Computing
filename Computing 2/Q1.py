def multiply(a,b):
        
        if str(a) == "1":
                return b
        else:
                return b + multiply((int(a) - 1), b)
