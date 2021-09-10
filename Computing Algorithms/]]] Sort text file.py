L = []

def bubble(L,ascend=True):
    for i in range(1,len(L)):
        for e in range(i-1):
            if ascend==True:
                if L[i] < L[e]:
                    L[i],L[e] = L[e],L[i]
            else:
                if L[i] > L[e]:
                    L[i],L[e] = L[e],L[i]
    return(L)

file_data = []
handle = open('sort.txt')
for line in handle:
    line = line.strip()
    # insert contextual modifications
    line = line.split('-')[1].strip().lower()
    # end
    file_data.append(line)

sorted = bubble(file_data)
mod = '\n'
print(mod + mod.join(sorted))





