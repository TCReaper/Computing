

def DecimalToBinary(DecimalNumber):
      BinaryString = ''
      while DecimalNumber>0:
            remainder = DecimalNumber % 2
            DecimalNumber = DecimalNumber // 2
            BinaryString = str(remainder) + BinaryString
      return BinaryString.zfill(8)


def runDec2Bin():
      f = open('DECIMAL.txt')
      for line in f:
            line = line.strip()
            print(DecimalToBinary(int(line)))


def BitShift(binaryString):
      binarycheck = True
      if type(binaryString) is int:
            return 'Invalid 8-bit binary string!'
      for i in binaryString:
            if i not in ['0','1']:
                  binarycheck = False
      if len(binaryString) == 8 and binarycheck:
            binaryString = binaryString[1:] + binaryString[0]
            return binaryString
      else:
            return 'Invalid 8-bit binary string!'

      
def Encrypt(word):
      encrypted = ''
      for letter in word:
            encrypted += BitShift(DecimalToBinary(ord(letter)+1))+' '
      return encrypted.strip()
      
def Decrypt(bin_string):
      word = ''
      bin_string = bin_string.split(' ')
      for i in bin_string:
            for times in range(7):
                  i = BitShift(i)
            word += str(chr(int(i,2)-1))
      return word
            
