f = open('txt.txt')
names = []
splits = 4
groups = [ [] for i in range(splits) ]

for i in f:
      names.append(i.strip())
f.close()

for i in range(len(names)):
      groups[i%splits].append(names[i])

for group in groups:
      for i in group:
            print(i)
      print('-'*50)
