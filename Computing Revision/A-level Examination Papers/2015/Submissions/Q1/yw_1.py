def read():
    store = []
    f = open('ADMISSIONS-DATA.txt')
    for i in f:
        i = i.strip()
        store.append(int(i))
    f.close()
    return store

def bubble_sort(l):
    count = 0
    for i in range(len(l)):
        for j in range(len(l) - i -1):
            count += 1
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l, count

def insertion_sort(l):
    count = 0
    for i in range(len(l)):
        j = i
        count += 1
        while l[j-1] > l[j] and j > 1:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1
    return l, count

cont = True
while cont:
    option = input('1. Read file data\n2. Bubble sort\n3. Quick sort/ Insertion sort\n4. End')
    if option == '1':
        data = read()
    elif option == '2':
        print(bubble_sort(data))
    elif option == '3':
        print(insertion_sort(data))
    else:
        cont = False

#10

        

    
