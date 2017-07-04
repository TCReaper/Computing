import random

#       Insertion Sort

lt = [] # List of integers to sort
for i in range(20):
        integer = random.randint(1,100)
        lt.append(integer)
print(lt)
swap = 0
#insertion sort algorithm
for i in range(1,len(lt)+1):
##        print(lt)
        # Check where to insert
        while len(lt) > i > 0 and lt[i] < lt[i-1]:
                #print(str(swap) + ": swapping " + str(lt[i]) + " and " + str(lt[i-1]))
                swap += 1
                # Swaps the two numbers
                lt[i], lt[i-1] = lt[i-1], lt[i]
                i -= 1
                print(lt)
print(lt)




	
