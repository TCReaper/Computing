Max = 20

def hash_val(id):
    return id % Max

hash_table = [None for i in range(Max)]

def add_to_table(table, value):
    ind = hash_val(value)
    if table[ind] == None:
        table[ind] = value
    else:
        temp = ind + 1
        while temp != ind:
            if table[temp] == None:  
                table[temp] = value
                return
            temp += 1
            if temp == Max:
                temp = 0

        print('Table is full')

filename = 'KEYS2.TXT'
file_handle = open(filename)

for line in file_handle:
    line = int(line.strip())
    add_to_table(hash_table, line)
file_handle.close()

keep_asking = True
while keep_asking:
    while True:
        id_in = input('Enter ID (X to stop): ')
        try:
            id_in = int(id_in)
        except:
            if id_in.lower() == 'x':
                keep_asking = False
                break
            print('Invalid input. Enter a positive integer as the ID')
        else:
            break
    if not keep_asking:
        break
    
    found = False
    for i in range(len(hash_table)):
        if hash_table[i] == id_in:
            found = True
            print(i)

    if not found:
        print('Not in table')
