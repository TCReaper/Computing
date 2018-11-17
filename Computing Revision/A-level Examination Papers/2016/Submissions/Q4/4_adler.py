def input_hex_value():
    get_input = True
    while get_input:
        hex_value = input("Hexadecimal value: ")
        if valid_hex(hex_value):
            return hex_value
        print("Invalid hexadecimal value! Try again.")
            
def valid_hex(hex_value):
    if len(hex_value) == 0:
        return False
    for hex_digit in hex_value:
        try:
            den_digit_val(hex_digit)
        except ValueError:
            return False
    return True

def den_digit_val(hex_digit): #returns denary value of input hexadecimal digit
    hex_digit = hex_digit.lower()
    mapping = '0123456789abcdef'
    return mapping.index(hex_digit)

def den_val(hex_value):
    result = 0
    hex_value = hex_value[::-1]
    for i in range(len(hex_value)):
        result += den_digit_val(hex_value[i]) * (16 ** i)
    if int(hex_value[::-1], 16) != result:
        raise ArithmeticError
    return result

hex_value = input_hex_value()
print(den_val(hex_value))


def hex_val(den_value):
    mapping = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while den_value > 0:
        result = mapping[den_value % 16] + result
        den_value = den_value // 16
    return result

#Time Taken: 27.05.21
#Time Allowed: 27.00.00 (excluding test cases)
