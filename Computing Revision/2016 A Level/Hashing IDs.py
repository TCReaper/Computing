

hash_table = ['' for i in range(20)]
file = open('KEYS2.txt','r')
for line in file:
      id_number = line.strip('\n')
      address = int(id_number) % 20
      not_input = True
      while not_input:
            if hash_table[address-1] == '':
                  hash_table[address-1] = int(id_number)
                  not_input = False
            else:
                  address += 1
                  if address == 20:
                        address = 0
for i in hash_table:
      if i == '':
            pass
      else:
            print(i)
task2point3 = True
while task2point3:
      new_id = int(input('Search for an ID number:  '))
      cur_address = 0
      not_found = True
      for i in hash_table:
            if new_id == i:
                  print(str(new_id)+' found at address '+str(cur_address))
                  not_found = False
            cur_address += 1
      if not_found:
            print('ID number not found! Does this customer exist 0w0')
