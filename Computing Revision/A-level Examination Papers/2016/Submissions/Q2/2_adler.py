##Max = 20
##hash_table = [None for i in range(20)]
##f = open('KEYS2.TXT')
##for line in f:
##    address = int(line.strip()) % Max
##    hash_table[address] = line.strip()
##f.close()
##
##for i in range(len(hash_table)):
##    if hash_table[i] != None:
##        print(hash_table[i])

def search(hash_table):
    for i in range(len(hash_table)):
        if hash_table[i] == None:
            return i
    return -1

Max = 20
hash_table = [None for i in range(20)]
f = open('KEYS2.TXT')
for line in f:
    address = int(line.strip()) % Max
    if hash_table[address] != None:
        address = search(hash_table)
    if address != -1:
        hash_table[address] = line.strip()
    else:
        print("hash_table is full")
f.close()

for i in range(len(hash_table)):
    if hash_table[i] != None:
        print(hash_table[i])

def search(IDNumber, hash_table): #returns index, -1 if not found in hash_table
    for i in range(len(hash_table)):
        if hash_table[i] == IDNumber:
            return i
    return -1

print()
print(search('37', hash_table))
print(search('77', hash_table))
print(search('97', hash_table))


#Time Taken: 14.24.02
#Time Allowed: 24.18.00
