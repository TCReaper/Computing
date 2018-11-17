file = open("KEYS2.TXT","r")

hash_table = [False]*20
maxkey = 20

print("{:<10}{:<10}".format("Address","Content"))
for line in file:
    i = int(line) % maxkey
    if hash_table[i] != False:
        count = 0
        while hash_table[i] != False:
            count += 1
            if count > maxkey:
                print("Hash table is full.")
                break
            i += 1
            if i == maxkey:
                i = 0
        if count <= maxkey:
            hash_table[i] = int(line)
    else:
        hash_table[i] = int(line)

for i in range(len(hash_table)):
    if hash_table[i]:
        print("{:<10}{:<10}".format(i, hash_table[i]))


id_no = int(input("Please enter an ID number: "))
i = int(id_no % maxkey)
count = 0
while hash_table[i] != id_no:
    count += 1
    if count > maxkey:
        print("ID number is not found.")
        break
    i += 1
    if i == maxkey:
        i = 1
if count <= maxkey:
    print("The address is " + str(i)) 
