def valid_hex(string):
    if string.isalnum():
        for char in string:
            if not ord(char) < 102:
                return False
        return True
    return False

def hex_to_den(string):
    if not type(string) == str:
        print('Invalid input')
        return None

    string = string.lower()
    if not valid_hex(string):
        print('Invalid input')
        return None

    key = '0123456789abcdef'
    den_val = 0
    for i in range(len(string)):
        ind = key.index(string[i])
        den_val += (16 ** (len(string) - i - 1)) * ind

    return den_val

def den_to_hex(num):
    key = '0123456789ABCDEF'

    if num == 0:
        return '0'

    hex_val = ''
    while num > 0:
        mod = num % 16
        hex_val = key[mod] + hex_val
        num = (num - mod) // 16

    return hex_val
