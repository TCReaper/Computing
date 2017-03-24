
#       Bubble Sort

listed = [6,5,4,3,2,1] # List of integers to sort

for e in range(0,len(listed)):
        print(listed)
        for i in range(0, len(listed)-1 ):
                if listed[i] > listed[i+1]:
                        # Switch current index with next index, vice versa
                        listed[i] , listed[i+1] = listed[i+1] , listed[i]
