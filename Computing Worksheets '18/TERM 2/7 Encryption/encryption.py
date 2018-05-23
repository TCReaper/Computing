
import random

def menu():
      while True:
            choice = input('Encrypt/Decrypt/Exit [E/D/X]:  ')
            if choice.lower() == 'e':
                  create()
            elif choice.lower() == 'd':
                  destroy()
            elif choice.lower() == 'x':
                  print('Goodbye, Agent')
                  break
            else:
                  print('Didn\t understand that instruction.\n')

                  
def create():
      file_handle = input('File name:  ')
      f = open(file_handle+'.txt')
      raw = []
      for line in f:
            line = line.strip()
            raw.append(line)
      for index in range(len(raw)):
            line = [index+1]
            base = random.randint(1,32)
            line.append(base)
            for letter in raw[index]:
                  line.append(ord(letter))
            raw[index] = line
      #print(raw)
      encrypted = encrypt(raw)
      write_file(encrypted,file_handle)


def encrypt(raw):
      for line in range(len(raw)):
            line = raw[line]
            base = line[1]
            for element in range(2,len(line)):
                  line[element] = denary2k(line[element],base)
      return raw
      
                  
def denary2k(element,k):
      element = int(element)
      #0-9 is 48-57
      #A-Z is 65-90
      string = ''
      while element > 0:
            add = element%k
            if add>9:
                  add -= 10
                  add = chr(65+add)
            string = str(add)+ string
            element = element // k
      return string


def k2denary(element,k):
      #0-9 is 48-57
      #A-Z is 65-90
      output = 0
      element = str(element)
      for i in range(len(element)):
            power = int(len(element) - 1 - i)
            i = element[i]
            if i.isalpha():
                  i = ord(i) - 55
            output += int(i) * (int(k)**power)
      return output
                    

def write_file(encrypted,handle):
      f = open(str(handle)+'_encrypted.txt','w')
      for line in encrypted:
            write = str(line[0])
            for term in range(1,len(line)):
                  write += ','+str(line[term])
            write+='\n'
            f.write(write)
      f.close()


def destroy():
      file_handle = input('File to decrypt:  ')
      f = open(file_handle+'.txt')
      coded = []
      for line in f:
            line = line.strip().split(',')
            coded.append(line)
      #print(coded)
      decrypted = decrypt(coded)


def qsort(arr):
        if len(arr) <= 1:
                return arr
        else:
                #print(arr)
                return qsort([x for x in arr[1:] if x[0]<arr[0][0]]) + [arr[0]] + \
                       qsort([x for x in arr[1:] if x[0]>=arr[0][0]])


def decrypt(coded):
      coded = qsort(coded)
      for line in coded:
            text = ''
            base = line[1]
            for element in range(2,len(line)):
                  #print(k2denary(line[element],base))
                  text += chr(k2denary(line[element],base))
            print(text.strip())













      
menu()
