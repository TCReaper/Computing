def menu():
    while True:
        choice = input("1.  Read file data\n2.  Bubble sort\n"\
              "3.  Quick sort / Insertion sort\n4.  End\n\n")
        #assuming choice is 1,2,3 or 4:
        if not check(choice):
            print("Invalid input! Enter either 1, 2, 3 or 4 corresponding to"\
                  " the desired option. Try again.")
        else:
            choice = int(choice)
            if choice == 4:
                #break
                return
            if choice == 1:
                data = [int(i) for i in read('ADMISSIONS-DATA.TXT')]
            elif choice == 2:
                try:
                    temp = data
                except UnboundLocalError:
                    print("Choose option 1 first!\n")
                else:
                    print_array(bubble(temp))
            elif choice == 3:
                try:
                    temp = data
                except UnboundLocalError:
                    print("Choose option 1 first!\n")
                else:
                    print("Insertion Sort is used.\n")
                    print_array(insertion(temp))
def check(choice):
    if not choice.isdigit():
        return False
    elif int(choice) not in range(1, 5):
        return False
    return True

def print_array(array):
    print("Number of Comparisons: {}\nSorted data:{}\n"\
                      .format(array[0], array[1]))
    
def read(file): #1
    f = open(file)
    temp = f.read()
    f.close()
    return temp.split('\n')

def bubble(array): #2
    count = 0
    for i in range(len(array)):
        swapped = False
        for j in range(len(array) - i - 1):
            count += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

    return count, array

def insertion(array):
    count = 0
    for i in range(1, len(array)):
        j = i
        while j > 0:
            count += 1
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return count, array

menu()

#Time Taken: 25.11.26 + 4.36.66 (for check choice parts)
#Time Allowed: 1.35min/mark * 14min = 18.9min = 18.54.00
