
#       Bubble Sort

listed = [12,45,1,62,3,62,51,4,152,36,24,3,47,5,5,45,253,523,52,1] # List of integers to sort

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
                      
