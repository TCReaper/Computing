
#       Bubble Sort

listed = [76,47,6,4,54,34,98,3,5,48,6,5,37,94,24,82,1,3,59,89,4,6] # List of integers to sort

for e in range(len(listed)):  # get max n times, each time excl. last max in A
        print(listed)
        swap = False
        for i in range(len(listed)-e-1):
                if listed[i] > listed[i+1]:
                        # Switch current index with next index, vice versa
                        listed[i] , listed[i+1] = listed[i+1] , listed[i]
                        swap = True
        if not swap:
                break#ng down inside
                      
