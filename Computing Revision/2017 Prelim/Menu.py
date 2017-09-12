

#menu

#task2.1

def menu():
      menu = True
      data_read = False
      while menu:
            option = input('#'*30+'\n1.Read menu data\n2.Take order\n3.Quit\n>>>  ')
            if option == '1':
                  file = open('MENU.TXT')
                  menu_unsort = []
                  for line in file:
                        line = line.strip('\n')
                        line = line.split(' ')
                        index = line[0]
                        price = line[-1]
                        name = ''
                        for i in line[1:-2]:
                              name += i + ' '
                        name.strip()
                        array = [index,name,price]
                        menu_unsort.append(array)
                  file.close()
                  menu = []
                  for i in range(int(menu_unsort[-1][0])):
                        for array in menu_unsort:
                              if i == int(array[0]):
                                    menu.append(array)
                  data_read = True
                  
            elif option == '2' and data_read == False:
                  print('Please read menu data first!')
                  
            elif option == '2' and data_read == True:
                  pass
                  
            elif option == '3':
                  print('System Shutdown Initiated. Have a good day.')
                  return 
            else:
                  print('#'*30+'\nInvalid Input!\n')
