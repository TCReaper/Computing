

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
        ta = 0
        tb = 0
        while ta<len(a) or tb<len(b):
                if ta == len(a):
                        c += b
                        tb = len(b)
                elif tb == len(b):
                        c += a
                        ta = len(a)
                else:
                        if a[ta] > b[tb]:
                                c += [b[tb]]
                                tb += 1
                        else:
                                c += [a[tb]]
                                ta += 1
        return c

print(mergeSort(lists))
