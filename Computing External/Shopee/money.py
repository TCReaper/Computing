a = input('').split() #amt of ppl
dt = {}
for i in range(int(a[0])):
    new = input('').split()
    dt[new[0]] = int(new[1])
#print(dt)
 
# get transactions
 
for i in range(int(a[1])):
    new = input('').split()
    if new[0] == new[1]:
        pass
    elif int(dt[new[0]]) - int(new[2]) < 0:
        pass
    else:
        dt[new[0]] -= int(new[2])
        dt[new[1]] += int(new[2])
ls = []
for i in dt:
    ls.append(i)
 
def qsort(arr):
    if len(arr) <= 1:
            return arr
    else:
            return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])
 
ls = qsort(ls)
 
for i in ls:
    print(i+' '+str(dt[i]))