

file = open('lscin.txt')
deets = []
for line in file:
      line = line.strip('\n')
      line = line.split(' ')
      array = []
      for i in line:
            array.append(int(i))
      deets.append(array)
file.close()

shop_pos = deets[1]
shop_order = deets[2]
shops = []
for i in shop_order:
      i -= 1
      pos = shop_pos[i]
      shops.append(pos)
#     shops is a list of nearest positions in ascending order

pos_found = False
potential = ((shops[0]+shops[1])//2)
if potential % 2 == 1:
      pass
else:
      potential -= 1
while not pos_found:
      untrue = False
      for i in range(1,len(shops)):
            j = i-1
            pd = abs(   potential - shops[j] )
            pd2 = abs(  potential - shops[i] )
            if pd <= pd2:
                  continue
            else:
                  potential += 2
                  untrue = True
                  break
            
      if untrue == False:
            pos_found = True
      if potential > deets[0][1]:
            break

out = open('lscout.txt','w')
if not pos_found:
      out.write('-1')
else:
      out.write(str(potential))
out.close()

