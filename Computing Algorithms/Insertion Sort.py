
def insertion(arr):
        for i in range(1,len(arr)):
                j = i
                #check for insertion
                while j >0 and arr[j] < arr[j-1]:
                        #swaps numbers
                        arr[j],arr[j-1]=arr[j-1],arr[j]
                        j -= 1
        return arr


	
