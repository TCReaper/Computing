

#       Insertion Sort

lt = [18,9,34,26,44,14,83,19,97,75,71,13,76,25,27,64,1,60,68,6] # List of integers to sort

#insertion sort algorithm
for i in range(1,len(lt)+1):
        print(lt)
        # Check where to insert
        while len(lt) > i > 0 and lt[i] < lt[i-1]:
                # Swaps the two numbers
                lt[i], lt[i-1] = lt[i-1], lt[i]
                i -= 1

