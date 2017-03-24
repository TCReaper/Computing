import datetime

#       Insertion Sort

lt = [18,49,34,26,44,14,83,19,97,75,71,13,76,25,27,64,1,60,68,6,
      41,58,65,54,11,16,81,32,55,82,100,98,66,53,22,92,8,45,91,36,
      7,5,28,35,33,86,24,69,89,57,2,12,63,40,94,43,73,4,17,93,
      67,21,56,20,79,3,72,61,95,29,30,50,78,9,42,99,37,87,62,48,
      85,59,15,47,23,84,77,46,52,10,80,70,74,88,96,38,90,31,51,39] # List of integers to sort


n = 10000000
timeavg=0
for i in range(n):
        start = datetime.datetime.now()
        #insertion sort algorithm
        i = 1
        for i in range(len(lt)):
                # Check where to insert
                while i > 0 and lt[i] < lt[i-1]:
                        # Swaps the two numbers
                        lt[i], lt[i-1] = lt[i-1], lt[i]
                        i -= 1
        end = datetime.datetime.now()
        seconds = (end-start).total_seconds()
        timeavg += seconds
print(timeavg/n)
