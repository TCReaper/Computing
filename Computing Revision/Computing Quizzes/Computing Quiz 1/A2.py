f = open("NUMBERS.txt","r")
data = {}
for i in f:
        current = int(i.strip())
        if current in data.keys():
                data[current]+= 1
        else:
                data[current] = 1
f.close()
sorting = list(data.keys())
sorting.sort()
print("{0:15}{1:15}".format("Number","Frequency"))
for k in sorting:
        print("{0:^19}{1:^1}".format(str(k),str(data[k])))
