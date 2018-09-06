

def backpack():
      f = open('INVENTORY.txt')
      item_list = []
      for line in f:
            item = line.strip()
            exists = False
            for index in range(len(item_list)):
                  if item_list[index][0] == item:
                        item_list[index] = (item_list[index][0],item_list[index][1]+1)
                        #print(item_list)
                        exists = True
                        
            if not exists:
                  item_list.append( (item,1) )
            
      f.close()

      for item_type in item_list:
            print('{0:18}{1}'.format(item_type[0],item_type[1]))
