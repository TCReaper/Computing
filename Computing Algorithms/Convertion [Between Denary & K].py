

# base converters

def d2k(denary,k):
      mapping = '0123456789abcdefghijklmnopqrstuvwxyz'
      string = ''
      while denary > 0:
            string = mapping [ denary%k ] + string
            denary = denary // k
      return string

def k2d(string,k):
      mapping = '0123456789abcdefghijklmnopqrstuvwxyz'
      denary = 0
      for i in range(len(string)):
            denary += mapping.index(string[i]) * k ** (len(string)-1-i)
      return denary
