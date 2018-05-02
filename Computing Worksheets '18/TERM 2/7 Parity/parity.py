def count_ones(string):
    ones = 0
    for i in range(len(string)):
        if string[i] == "1":
            ones += 1
    return ones

def get_string_parity(string, odd = True):
    is_odd = count_ones(string) % 2 == 1
    return int(not (is_odd == odd))

# write a function to calculate and update the parity bit (most significant bit)
def add_byte_parity(byte, odd = True):
    return str(get_string_parity(byte, odd)) + byte[1:]

def check_string_parity(string, odd = True):
    return (count_ones(string) % 2 == 1) == odd

# write a function check the parity bit (most significant bit)
def check_byte_parity(byte, odd = True):
    return check_string_parity(byte, odd)

def get_column(block, col):
    col_string = ""
    for i in range(len(block)):
        col_string += block[i][col]
    return col_string

# write a function to calculate and add the parity block
def add_block_parity(block, odd = True):
    # assumes each byte has parity bit defined
    parity_byte = ""
    for i in range(len(block[0])):
        parity_byte = parity_byte + \
                      str(get_string_parity(get_column(block, i), odd))
    return block + [parity_byte]

# write a function to check the parity block
def check_block_parity(block, odd = True):
    for i in range(len(block[0])):
        if (count_ones(get_column(block, i)) % 2 == 1) != odd:
            return False
    return True

################################################################################
# WRITE THE FOLLOWING FUNCTION
################################################################################

def find_parity_block_error(block, odd = True):
    for i in range(len(block[0])):
        if (count_ones(get_column(block, i)) % 2 == 1) != odd:
            error_bit = i
    for i in range(len(block)):
        if check_byte_parity(block[i]) == False:
            error_byte = i

    print( error_byte,error_bit)
    
    #return (error_byte, error_bit)

# write a function to add an error into the original block (not parity byte)
def add_error(block):
    from random import randint
    err_row = randint(0, len(block) - 2) # exclude parity byte in choice
    err_col = randint(0, len(block[err_row]) - 1)
    new_bit_val = str(int(not (int(block[err_row][err_col]))))
    block[err_row] = block[err_row][:err_col] + new_bit_val + \
                     block[err_row][err_col + 1:]
    print("Added error in BYTE " + str(err_row +1) + " BIT " + str(err_col +1))
    return block

# main
from random import randint

def print_block(block):
    for i in range(len(block)):
        print(" ".join(list(block[i])))

def parity_test():
    block = []
    for i in range(randint(2,2)):
        current_byte = "."
        for i in range(7):
            current_byte = current_byte + str(randint(0,1))
        block.append(current_byte)
    #print("Original Block:")
    #print_block(block)

    for i in range(len(block)):
        block[i] = add_byte_parity(block[i])
    print("\nBlock with Parity Bits:")
    print_block(block)

    print("\nChecking Parity Bits:")
    for i in range(len(block)):
        print("Byte " + str(i) + ": " + \
              ("Passed" if check_byte_parity(block[i]) else "Failed"))


    block = add_block_parity(block)
    print("\nBlock with Parity Byte:")
    print_block(block)
    print("Parity Byte Parity Bit Check: " + \
              ("Passed" if check_byte_parity(block[-1]) else "Failed"))

    ##print("\nBlock with 1 Error:")
    ##block = add_error(block)
    ##print_block(block)
    ##
    ##print("\nBlock parity check: " + str(check_block_parity(block)))
    ##################################################################################
    ### WRITE THE FOLLOWING FUNCTION
    ##################################################################################
    ##error_location = find_parity_block_error(block)
    ###print("Error found in BYTE " + str(error_location[0]) + " BIT " + \
    ###      str(error_location[1]))
    ##################################################################################

while True:
    parity_test()
    input()
    input()
