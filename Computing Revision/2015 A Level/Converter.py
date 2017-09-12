
# Task 2.1

def Converter(DenaryNumber):
      if DenaryNumber == 0 or DenaryNumber == 1:
            print(DenaryNumber)
      else:
            print(DenaryNumber%2,end='')
            Converter(DenaryNumber//2)

# Task 2.2

# It prints out the binary value of the denary integer in reverse order
# 111000 prints out as 000111

# Task 2.3

global output
output = ''
def Converter2(DenaryNumber):
      global output
      if DenaryNumber == 0:
            print('0'+output)
      elif DenaryNumber == 1:
            print('1'+output)
      else:
            output = str(DenaryNumber%2) + output
            Converter2(DenaryNumber//2)

def Converter3(DenaryNumber):
      if DenaryNumber == 0 or DenaryNumber == 1:
            print(DenaryNumber,end='')
      else:
            Converter(DenaryNumber//2)
            print(DenaryNumber%2,end='')
