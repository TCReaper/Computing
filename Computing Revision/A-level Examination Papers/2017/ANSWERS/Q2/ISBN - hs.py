def CalCheckDigit(Number,Total):
      if len(Number) > 1:
            Digit = int(Number[0])
            Total += (Digit * (len(Number) + 1))
            #print(str(Digit),str(len(Number)+1),str(Total))
            NewNumber = Number[1:]
            CheckDigit = CalCheckDigit(NewNumber,Total)
            
      else: #if len(Number) == 1 or 0
            Digit = int(Number[0])
            Total += Digit * (len(Number)+1)
            CalcModulus = Total % 11
            CheckValue = 11 - CalcModulus
            if CheckValue == 11:
                  return '0'
            elif CheckValue == 10:
                  return 'X'
            else:
                  return str(CheckValue)

      if len(Number) == 9:
            return str(CheckDigit)
      else:
            return CheckDigit

def ISBN():
      query = input('What is the text file handle:  ')
      f = open(query+'.txt')
      isbns = []
      for line in f:
            line = line.strip()
            isbns.append(line)
      f.close()

      for isbn in isbns:
            print(isbn+CalCheckDigit(isbn,0))
