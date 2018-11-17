#2.1
ids = []
f = open('KEYS1.txt')
for i in f:
    i = i.strip()
    ids.append(i)
f.close()

def hash(data):
    hash_value = int(data)%20 - 1
    return hash_value
    
hash_table = ['' for j in range(20)]
for k in ids:
    hash_table[hash(k)] = i
print(hash_table)

#2.2
new_ids = []
f = open('KEYS2.txt')
for i in f:
    i = i.strip()
    new_ides.append(i)
f.close()

hash_table = ['' for j in range(20)]
for k in new_ids:
    if hash_table[hash(k)] == '':
        hash_table[hash(k)] = i
    else:
        current = hash(k)
        while hash_table[current] != '':
            if current == len(hash_table):
                current = 0
            else:
                current += 1
        hash_table[current] = k
print(hash_table)

#2.3
id_number = input('Please enter ID number: ')
for i in range(len(hash_table)):
    if hash_table[i] == id_number:
        print('Address: ' + str(i))
