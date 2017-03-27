

#       Merge Sort


lists = [18,9,34,26,44,14,83,19,97,75,71,13,76,25,27,64,1,60,68,6]

def mergeSort(lists):
        print(lists)
        a = input("enter to continue")
        if len(lists)<2:
                return lists
        else:
                return merge(mergeSort(lists[:len(lists)//2]),mergeSort(lists[len(lists)//2:]))

def merge(a,b):
        c = []
        while len(a)>0 or len(b)>0:
                if len(a)==0:
                        c += b
                        b = []
                elif len(b)==0:
                        c += a
                        a = []
                else:
                        if a[0] > b[0]:
                                c += [b[0]]
                                del b[0]
                        else:
                                c += [a[0]]
                                del a[0]
        return c

print(mergeSort(lists))
