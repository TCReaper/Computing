

# task 1.1

global lists
lists = []

def menu():

      global lists
      
      option_list = [None,'Read file data','Bubble sort','Quick sort / Insertion sort','End']

      for i in range(1,5):
            print(str(i)+'.  '+option_list[i])
      choice = input('wthek do you want to do now...?   ')
      if choice == '1':
            read()
      elif choice == '2':
            bubblesort(lists)
      elif choice == '3':
            qisort()
      elif choice == '4':
            return None
      else:
            print('Choose a valid option lol')
      menu()


# task 1.2

def read():
      file_to_read = open('ADMISSIONS-DATA.txt','r')
      for line in file_to_read:
            line = line.strip('\n')
            #print(line)  stub test
            lists.append(int(line))
            
            
def bubblesort(lists):
      no_swaps = False
      while not no_swaps:
            no_swaps = True
            for i in range(len(lists)-1):
                  if lists[i] > lists[i+1]:
                        no_swaps = False
                        lists[i],lists[i+1]=lists[i+1],lists[i]
      print(lists)



            
menu()
