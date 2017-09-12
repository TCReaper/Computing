

file = open('cocoin.txt')
xycoods = []
for line in file:
      line = line.strip('\n')
      line = line.split(' ')
      coods = []
      for cood in line:
            coods.append(cood)
      xycoods.append(coods)

xyz1 = xycoods[0]
xyz2 = xycoods[1]

x1 = xyz1[0]
x2 = xyz2[0]
y1 = xyz1[1]
y2 = xyz2[1]

