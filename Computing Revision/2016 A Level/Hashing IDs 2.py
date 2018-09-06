


hash_table = [None for i in range(20)]
file = open('KEYS2.txt','r')
keys = []
for line in file:
      keys.append(line.strip())
file.close()
for key in keys:
      address = int(key) % 20
      not_input = True
      while not_input:
            if hash_table[address-1] == None:
                  hash_table[address-1] = int(key)
                  not_input = False
            else:
                  address += 1
                  if address == 20:
                        address = 0
for i in hash_table:
      if i == None:
            pass
      else:
            print(i)

search_hash = True           
while search_hash:
      new_id = int(input('Search for an ID number:  '))
      cur_address = 0
      not_found = True
      for i in hash_table:
            if new_id == i:
                  print(str(new_id)+' found at address '+str(cur_address))
                  not_found = False
            cur_address += 1
      if not_found:
            print('ID number not found! NotExistError uwu')
