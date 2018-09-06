
def qsort(arr):
        if len(arr) <= 1:
                return arr
        else:
                #print(arr)
                return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

lt = [5,4,3,2,1]
print(qsort(lt))


def qsorts(arr):
        if len(arr) < 2:
                return arr
        else:
                pivot = arr[0]
                less = []
                more = []
                for i in range(1, len(arr)):
                        if arr[i] < pivot:
                                less.append(arr[i])
                        else:
                                more.append(arr[i])
                return qsorts(less) + [pivot] + qsorts(more)
