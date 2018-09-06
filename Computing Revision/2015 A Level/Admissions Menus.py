def read():
      f = open('ADMISSIONS-DATA.TXT')
      data = []
      for line in f:
            data.append(line.strip())
      f.close()
      print( '\nData has been read\n')
      return data

def bubble(data):
      checks = 0
      for i in range(len(data)):
            swap = False
            for index in range(len(data)-i-1):
                  checks += 1
                  if data[index] > data[index+1]:
                        data[index],data[index+1] = data[index+1],data[index]
                        swap = True
            if not swap:
                  break
      print(data)
      print(checks)
      return data

def insertion(data):
      checks = 0
      for i in range(len(data)):
            j = i
            while data[j-1] > data[j] and j > 1:
                  checks += 1
                  data[j],data[j-1] = data[j-1],data[j]
                  j -= 1
      print(data)
      print(checks)
      return data




run_menu = True
data = None
while run_menu:
      options = ['Read file data','Bubble sort','Insertion sort','End']
      for i in range(len(options)):
            print('{0:}. {1}'.format(str(i+1),options[i]))
      choice = input('\nChoose an option:  ')
      
      if choice == '1':
            data = read()
            
      if (choice == '2' or choice == '3') and data == None:
            print('\nRead data first\n\n')
            
      elif choice == '2':
            data = bubble(data)
            
      elif choice == '3':
            data = insertion(data)
            
      if choice == '4':
            break
