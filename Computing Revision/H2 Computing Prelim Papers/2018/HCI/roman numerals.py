

# romano numero

def roman(number):
      one = 'I'
      five = 'V'
      ten = 'X'
      fifty = 'L'
      hundred = 'C'

      roman = ''
      specification = [[100,hundred],[90,ten+hundred],\
                       [50,fifty],[40,ten+fifty],\
                       [10,ten],[9,one+ten],[5,five],\
                       [4,one+five],[1,one]]
      while number != 0:
            for i in specification:
                  digit,string = i
                  if number >= digit:
                        number -= digit
                        roman += string
                        break
      return roman
      
for i in range(200):
     print(roman(i))
