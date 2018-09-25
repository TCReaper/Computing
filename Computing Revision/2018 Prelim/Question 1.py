# Task 1.1

import datetime

baseDate = datetime.datetime(1965, 8, 9)
data = []

fileHandle = open("DATA.TXT")
for line in fileHandle:
    line = line.strip()
    line = line[1:] # ignore the "D" on each line
    line = line.split("V1")
    line = [int(line[0])] + line[1].split("V2")
    line = [line[0]] + [line[1]] + line[2].split("V3")
    date = baseDate + datetime.timedelta(line[0])
    ddmmyyyy = "{0:>02}".format(str(date.day)) + \
               "{0:>02}".format(str(date.month)) + \
               "{0:>04}".format(str(date.year))
    data.append((ddmmyyyy, float(line[1]), \
                 float(line[2]), float(line[3])))
fileHandle.close()

# Task 1.2

# calculate/store means for each 4-tuple in data
for i in range(len(data)):
    current_mean = (data[i][1] + data[i][2] + data[i][3]) / 3
    data[i] = (data[i][0], data[i][1], data[i][2], \
               data[i][3], current_mean)

def bubble_sort_means(L):
    n = len(L)
    swapped = True
    while swapped and n > 0:
        swapped = False
        for i in range(1, n):
            if L[i - 1][4] < L[i][4]: # descending (means)
                L[i - 1], L[i] = L[i], L[i - 1]
                swapped = True
        n -= 1
    return L

# Task 1.3

sorted_means = bubble_sort_means(data)
num_elements = len(sorted_means)
mid = num_elements // 2
if num_elements % 2 == 0:
    median = (sorted_means[mid - 1][4] + sorted_means[mid][4])
    median /= 2
else:
    median = sorted_means[mid][4]
print("The median value is: " + str(median))

# Task 1.4

def insertion_sort_dates(L):
    i = 1
    while i < len(L):
        j = i
        while j > 0 and L[j - 1][0] > L[j][0]: # dates
            L[j - 1], L[j] = L[j], L[j - 1]
            j -= 1
        i += 1
    return L

# Task 1.5

def binary_search_dates(L, target):
    start = 0
    end = len(L)
    while start <= end:
        mid = (start + end) // 2
        if target == L[mid][0]:
            return mid
        elif target < L[mid][0]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

sorted_dates = insertion_sort_dates(data)
while True:
    try:
        print("")
        input_year = input("Please enter a valid YEAR: ")
        input_year = int(input_year)
        input_month = input("Please enter a valid MONTH: ")
        input_month = int(input_month)
        input_day = input("Please enter a valid DAY: ")
        input_day = int(input_day)
        target_date = "{0:>02}".format(input_day)
        target_date += "{0:>02}".format(input_month)
        target_date += str(input_year)
        index = binary_search_dates(sorted_dates, \
                                    target_date)
        if index == -1:
            raise ValueError
        print("\nThe values on", end = " ")
        print("{0}".format(input_year), end = "-")
        print("{0:>02}".format(input_month), end = "-")
        print("{0:>02}".format(input_day), end = " ")
        print("are:", end = " ")
        print("{0:.2f}".format(sorted_dates[index][1]), \
              end = ", ")
        print("{0:.2f}".format(sorted_dates[index][2]), \
              end = ", ")
        print("{0:.2f}".format(sorted_dates[index][3]))
        stop = ""
        while stop not in ["Y", "N"]:
            print("")
            stop = input("Do you wish to continue? (Y/N): ")
            if stop not in ["Y", "N"]:
                print("Invalid input. \"Y\" or \"N\" only.")
        if stop == "N":
            break
    except:
        current_year = datetime.datetime.today().year
        print("\nInvalid date specified. Please ensure:")
        print("\tYEAR between 1965 and " + str(current_year))
        print("\tMONTH between 1 and 12")
        print("\tDAY between 1 and 31")
