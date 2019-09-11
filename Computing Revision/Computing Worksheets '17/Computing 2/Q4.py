

def count(positive_integer):
      if len(str(positive_integer))==0:
            return 0
      n = positive_integer
      return 1+count(str(n)[:len(str(n))-1])

