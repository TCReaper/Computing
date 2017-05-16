
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
punctuation = [' ',':',',','.','/','\'',']','[',';','-','_','=','+','~','`',
               '|','!','@','#','$','%','^','&','*','(',')']

import requests

def body():
      f = open("bdg.txt")
      letters = []
      for line in f:
            for i in line:
                  letters.append(i)
      f.close()

      for index in range(3,len(letters)):
            if letters[index] in alphabet:
                  if letters[index-1] in ALPHABET and letters[index-2] in ALPHABET and letters[index-3] in ALPHABET \
                     and letters[index+1] in ALPHABET and letters[index+2] in ALPHABET and letters[index+3] in ALPHABET:
                        if letters[index-4] in ALPHABET or letters[index+4] in ALPHABET:
                              pass

                        else:
                              print(letters[index-4:index+5])

def linkedlist():
      nextnothing = 80865
      runn = True
      while runn:
            link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
            f = requests.get(link+str(nextnothing))
            print(f.text)
            f.text.split()
            nextnothing = f.text.split()[-1]
