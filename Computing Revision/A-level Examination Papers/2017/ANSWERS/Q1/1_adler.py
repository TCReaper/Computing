Inventory = []
f = open("INVENTORY.txt")
for line in f:
    for i in range(len(Inventory)):
        if Inventory[i][0] == line.strip():
            Inventory[i][1] += 1
            break
    else:
        Inventory.append([line.strip(), 1])
f.close()

ItemTypes = [Inventory[i][0] for i in range(len(Inventory))]
ItemCounts = [Inventory[i][1] for i in range(len(Inventory))]

print("{:<20}{}".format("ItemType", "Count"), end = '\n\n')
for i in range(len(ItemTypes)):
    print("{:<20}{}".format(ItemTypes[i], ItemCounts[i]))

#Time Taken: 9.26.05
#Time Allowed: 20.25.00
