#4.1
#16min
mapping = '0123456789abcdef'
hexadecimal = input('Please enter Hexadecimal: ')
for i in hexadecimal:
    if i not in mapping:
        print('Error, invalid input.')

def hexadecimal_to_denary(hexadecimal):
    mapping = '0123456789abcdef'
    denary = 0
    reverse = hexadecimal[::-1]
    for i in range(len(reverse)):
        for j in range(len(mapping)):
            if reverse[i] == mapping[j]:
                value = j
        denary += value * 16 ** i
    return denary

print('The denary value for ' + str(hexadecimal) + ' is ' + str(hexadecimal_to_denary(hexadecimal)))

#4.3
def denary_to_hexadecimal(denary):
    mapping = '0123456789abcdef'
    hexadecimal = ''
    power = 0
    while denary > 0:
        hexadecimal = mapping[denary % 16] + hexadecimal
        denary = denary // 16
    return hexadecimal

