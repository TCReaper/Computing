# Task 2.1

def d2k(denary_value, k):
    values = "0123456789abcdefghijklmnopqrstuvwxyz"
    base_k_value = ""
    while denary_value > 0:
        base_k_value = values[denary_value % k] + \
                       base_k_value
        denary_value = denary_value // k
    return base_k_value

def k2d(base_k_value, k):
    values = "0123456789abcdefghijklmnopqrstuvwxyz"
    denary_value = 0
    base_k_value = base_k_value[::-1]
    for i in range(len(base_k_value)):
        denary_value += values.index(base_k_value[i]) * \
                        k ** i
    return denary_value
        
def universal_base_division(dividend, dividend_base, \
                            divisor, divisor_base, \
                            result_base):
    if dividend_base < 2 or dividend_base > 30 or \
       divisor_base < 2 or divisor_base > 30 or \
       result_base < 2 or result_base > 30:
        print("You must specify a base between 2 and 30.")
    else:
        # determine sign of result
        sign = 1
        if dividend[0] == "-":
            dividend = dividend[1:]
            sign *= -1
        if divisor[0] == "-":
            divisor = divisor[1:]
            sign *= -1
        if sign < 0:
            sign = "-"
        else:
            sign = ""

        # dealing with 0 cases
        if dividend == "0":
            return "0"
        if divisor == "0":
            return "Undefined"

        denary_dividend = k2d(dividend, dividend_base)
        denary_divisor = k2d(divisor, divisor_base)

        # determine value before and after the .
        whole_values = denary_dividend // denary_divisor
        decimal_values = (denary_dividend % \
                          denary_divisor) / denary_divisor
        decimal_values = int(str(decimal_values)[2:])
        base_k_whole_values = d2k(whole_values, result_base)
        base_k_decimal_values = d2k(decimal_values, \
                                    result_base)
        if len(base_k_decimal_values) > 0:
            base_k_decimal_values = "." + \
                                    base_k_decimal_values
            
        return sign + base_k_whole_values + \
               base_k_decimal_values

# Task 2.2
print(universal_base_division("mma01",23,"30501",6,2))
