def exists(l,a):
    for i in range(len(l)):
        if l[i] == a:
            return True
    return False

file = open("INVENTORY.TXT")

Inventory = []
for line in file:
    Inventory.append(line.strip())
file.close()

ItemTypes = []
for i in range(len(Inventory)):
    if not exists(ItemTypes,Inventory[i]):
        ItemTypes.append(Inventory[i])

ItemCounts = []
for i in range(len(ItemTypes)):
    ItemCounts.append(0)
    for j in range(len(Inventory)):
        if Inventory[j] == ItemTypes[i]:
            ItemCounts[i] += 1

print("{:<20}{:<3}".format("ItemType","Count"))
for i in range(len(ItemTypes)):
    print("{:<20}{:<3}".format(ItemTypes[i],ItemCounts[i]))
