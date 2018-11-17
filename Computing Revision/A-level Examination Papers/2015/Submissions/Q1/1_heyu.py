def quickSort_helper(data):
    pivot = data[0]
    left = []
    right = [] 
    for i in range(1, len(data)):
        if data[i]<pivot:
            left.append(data[i])
        else:
            right.append(data[j])
    return quickSort_helper(left)+pivot+quickSort_helper(right) 

def quickSort(data):
    return quickSort_helper(data)

def insertionSort(data):
    count = 0 
    for i in range(1,len(data)):
        j = i-1
        temp = data[i] 
        while j>=0 and temp < data[j]:
            count += 1
            data[j+1] = data[j] 
            j -= 1
        data[j+1] = temp
    return data, count 

endProgram = False
while not endProgram:
    print("1. Read file data")
    print("2. Bubble Sort")
    print("3. Quick sort/Insertion sort")
    print("4. End")
    n = int(input("Please enter the option: "))
    if n == 1:
        data = [] 
        file = open("ADMISSIONS-DATA.TXT","r")
        for line in file:
            data.append(int(line))
    elif n == 2:
        count = 0 
        for i in range(len(data)):
            for j in range(len(data)-i-1):
                if data[j]>data[j+1]:
                    count += 1
                    temp = data[j]
                    data[j] = data[j+1]
                    data[j+1] = temp
            if count == 0:
                break
        print(data, count) 
    elif n == 3:
        #data, count = quickSort(data)
        data, count = insertionSort(data)
        print(data, count)
    else:
        endProgram = True 
