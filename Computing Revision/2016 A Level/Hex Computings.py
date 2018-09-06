

def hex2den(hexstring):
      denary = 0
      for i in range(len(hexstring)):
            denary += hexdigit2den(hexstring[i]) \
                      * 16 ** (len(hexstring) - 1 - i)
      return denary

def hexdigit2den(digit):
      mapping = '0123456789abcdef'
      return mapping.index(digit.lower())


def hex_validate(hexstring):
      mapping = '0123456789abcdef'
      for i in range(len(hexstring)):
            if str(hexstring[i]) not in mapping:
                  print('Not a valid hexadecimal :P')
                  return False
      return hexstring


def get_input():
      while True:
            hexstring = hex_validate(input('Input hexadecimal number: '))
            if hexstring != False:
                  break
            else:
                  print('Try Again!\n')

      print(hex2den(hexstring))

get_input()

def den2hex(denary):
      mapping = '0123456789abcdef'
      hexstring = ''
      while denary > 0:
            hexstring = mapping[ denary % 16 ] + hexstring
            denary = denary // 16
            
      return hexstring

            
