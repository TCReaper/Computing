def get_freq():
    freq_data = []
    x_value_count = 0
    while True:
        while True:
            x_value = input("Next X value ... <ZZZ to END> ")
            if x_value == 'ZZZ':
                return freq_data
            if x_value_count == 6:
                print("No more than six X values are allowed. 'ZZZ' to END.")
            else:
                break
        while True:
            freq = input("Frequency ... ")
            if freq.isdigit() and int(freq) in range(61):
                freq = int(freq)
                break
            print("Invalid Frequency value! Try again.")
        freq_data.append([x_value, freq])
        x_value_count += 1
    return freq_data



def print_freq(freq_data):
    #freq_data: ARRAY[[X Value, Frequency] for each X Value]
    print("\n\n" + "+" * 40)
    print("Frequency distribution")
    print("+" * 40 + "\n")
    for i in range(len(freq_data)):
        print("  {:<8}{}".format(freq_data[i][0], "@" * freq_data[i][1]))



#max 40 lines
#header takes 4 lines (including the empty line before the first x value
#36 lines allowed for max 6 values
#each line is thus allowed a max of 6 bar width

#'@' is replaced with '#' as it is easier to see
        

def amended_print_freq(freq_data):
    #freq_data: ARRAY[[X Value, Frequency] for each X Value]
    print("\n\n" + "+" * 40)
    print("Frequency distribution")
    print("+" * 40 + "\n")
    for i in range(len(freq_data)):
        print("  {:<8}{}".format(freq_data[i][0], "#" * freq_data[i][1]))
        for j in range(5):
            print("{:<10}{}".format("", "#" * freq_data[i][1]))

def sort_by_freq(freq_data): #insertion sort
    for i in range(len(freq_data)):
        j = i
        while j > 0 and freq_data[j][1] < freq_data[j - 1][1]:
            freq_data[j], freq_data[j - 1] = freq_data[j - 1], freq_data[j]
    return freq_data

def dynamic_scaling_print_freq(freq_data):
    temp_freq_data = freq_data
    highest_freq = sort_by_freq(temp_freq_data)[0][1]
    if higheset_freq < 61: #no need to scale
        amended_print_freq(freq_data)
    else: #requre scaling
        #since 10 are used for x value printing,
        #only 70 are left for freq printing
        scale = highest_freq / 70
        if scale != int(scale):
            scale += 1
        scale = int(scale) ** (-1)
        
        
temp = get_freq()
amended_print_freq(temp)
