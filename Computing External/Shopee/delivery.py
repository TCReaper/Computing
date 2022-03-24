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

for i in dt:
    print(i+' '+str(dt[i]))
