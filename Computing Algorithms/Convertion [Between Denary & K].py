def den2k(denary,k):
      mapping = '0123456789abcdef'
      string = ''
      while denary > 0:
            string = mapping[ denary % k ] + string
            denary = denary // k
            
      return string

def k2den(string,k):
      mapping = '0123456789abcdef'
      denary = 0
      for i in range(len(string)):
            denary += mapping.index(string[i].lower()) \
                      * k ** (len(string) - 1 - i)
      return denary
