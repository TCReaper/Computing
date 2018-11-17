def get_choice():
    while True:
        choice = input("\n1. Read file\n"\
                       "2. Linear Search\n"\
                       "3. Binary Search\n"\
                       "4. End\n")
        if choice.isdigit():
            if int(choice) in range(1, 5):
                return int(choice)
        print("\nInvalid input. Please select an option from 1 to 4"\
              ", corresponding to the desired option.")

def menu():
    while True:
        choice = get_choice()
        if choice == 4:
            break
        elif choice == 1:
            x = 2
            file_data = read_file(x)
        else:
            try:
                file_data
            except NameError:
                print("\nPlease read file data using option 1 first!")
            else:
                sales_figure = input("\nSales figure to find: ")
                if choice == 2: #linear search
                    found, count = LinearSearch(file_data, sales_figure)
                    if found == 0:
                        print("\nNumber of day(s) with this sales"\
                              " figure reported: ", count)
                else: #choice = 3 #binary search
                    try:
                        sorted_file_data
                    except NameError:
                        sorted_file_data = quick_sort(file_data)
                        found = BinarySearch(sorted_file_data, \
                                             sales_figure)
                print("Sales figure " + sales_figure + " was ", \
                      end = '')
                if found == -1:
                    print("not ", end = '')
                print("found in the file ", end = '')
                if x == 1:
                    print("CUPS-SOLD1.txt")
                else: #x = 2
                    print("CUPS-SOLD2.txt")
                    

def read_file(x): 
    #x is either 1 or 2 and represents which file is to be opened
    #i.e.: x = 1 for CUPS-SOLD1.txt; x = 2 for CUPS-SOLD2.txt
    if x == 1:
       file_handle = open("CUPS-SOLD1.txt")
    elif x == 2:
        file_handle = open("CUPS-SOLD2.txt")
    else:
        raise ValueError
    file_data = file_handle.read().strip().split("\n")
    file_handle.close()
    return file_data

def LinearSearch(array, target):
    count = 0
    for i in range(len(array)):
        if array[i] == target:
            count += 1
    if count == 0:
        found = -1
    else:
        found = 0
    return found, count

def BinarySearch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = (low + high) // 2
        if target == array[middle]:
            return 0
        elif target < array[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1

def quick_sort(array):
    if len(array) < 2:
        return array
    left = []
    right = []
    pivot = array[0]
    for i in range(1, len(array)):
        if array[i] < pivot:
            left.append(array[i])
        else:
            right.append(array[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
