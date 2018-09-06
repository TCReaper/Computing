

def Converter(DenaryNumber):
      if DenaryNumber == 0 or DenaryNumber == 1:
            print(DenaryNumber)
      else:
            print(DenaryNumber%2)
            Converter(DenaryNumber//2)

def Converter2(DenaryNumber,output=''):
      if DenaryNumber == 0:
            print('0'+output)
      elif DenaryNumber == 1:
            print('1'+output)
      else:
            output = str(DenaryNumber%2) + output
            Converter2(DenaryNumber//2,output)
