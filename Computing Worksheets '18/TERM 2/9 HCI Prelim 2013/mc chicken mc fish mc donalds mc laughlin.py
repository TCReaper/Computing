

vowels = 'aeiouy'

def SMOG():
      f = open('PAS.txt')
      text = []
      for line in f:
            line = line.strip().split(' ')
            text.append(line)
      f.close()

      mid = len(text) // 2
      measure = text[:10] + text[mid - 5: mid + 5] + text[-10:]

      psw = 0
      for line in measure:
            psw += count_psw(line)

      sqrt = round(psw ** 0.5,3)

      print('Sample text name: PAS.txt')
      print('No. of PSW:  '+str(psw))
      print('Square root of PSW:  '+str(sqrt))
      print('SMOG grade:  '+str(round(sqrt+3,3)))

      
def syllables(word):
      word = str(word)
      syllable_count = 0
      adjacent = False
      for i in range(len(word)):
            letter = word[i].lower()
            if letter == 'e' and i == len(word)-1:
                  pass
            elif letter in vowels and not adjacent:
                  syllable_count += 1
                  adjacent = True
            elif adjacent and letter not in vowels:
                  adjacent = False
      return syllable_count

def count_psw(line):
      psw = 0
      for word in range(len(line)):
            word = line[word]
            if syllables(word) >= 3:
                  psw += 1
      return psw
            
