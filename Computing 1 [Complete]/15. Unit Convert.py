


#       Unit Converter

def converter():
        global n
        global dimension
        global unit
        global convert
        if unit == "mm":
                unit = 0.001
        elif unit == "cm":
                unit = 0.01
        elif unit == "m":
                unit = 1
        elif unit == "km":
                unit = 1000
        if convert == "mm":
                convert = 0.001
        elif convert == "cm":
                convert = 0.01
        elif convert == "m":
                convert = 1
        elif convert == "km":
                convert = 1000
        if dimension == "length":
                power = 1
        elif dimension == "area":
                power = 2
        elif dimension == "volume":
                power = 3
        multiple = unit / convert
        final = float(n) * ( multiple ** power )
        print(final)
        
run = True
while run:
        n = input("Input quantity:    ")
        dimension = input("Is this quantity a LENGTH, AREA or VOLUME?    ").lower()
        unit = input("Select the base unit of measurement ! ( mm, cm, m, km ):    ").lower()
        convert = input("What unit would you like your measurement to be converted to:    ").lower()
        converter()
        print("")
