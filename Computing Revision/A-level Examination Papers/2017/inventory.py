

file_handle = open('INVENTORY.txt')

Inventory = []
for line in file_handle:
      line = line.strip()
      Inventory.append(line)
file_handle.close()

ItemType = []
for item in range(len(Inventory)):
      item = Inventory[item]
      if item not in ItemType:
            ItemType.append(item)

ItemCounts = [0 for i in range(len(ItemType))]
for item in range(len(Inventory)):
      item = Inventory[item]
      index = ItemType.index(item)
      ItemCounts[index] += 1


print('{0:18}{1}\n'.format('ItemType','Count'))
for i in range(len(ItemCounts)):
      print('{0:18}{1}'.format(ItemType[i],ItemCounts[i]))
      
