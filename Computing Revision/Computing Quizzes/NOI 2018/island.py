[towns,junctions] = raw_input().split() #'6 3'.split() #
towns = int(towns)
junctions = int(junctions)

jt_pairs = ['0' for i in range(junctions)]
jj_connections = 0
for i in range(towns+junctions-1):
      pairs = raw_input().split()
      #check if both
      if int(pairs[0])>towns and int(pairs[1])>towns:
            jj_connections += 1
      elif int(pairs[0])>towns or int(pairs[1])>towns:
            if int(pairs[0])>towns:
                  jt_pairs[int(pairs[0])-towns-1] = int(jt_pairs[int(pairs[0])-towns-1])+1
            else:
                  jt_pairs[int(pairs[1])-towns-1] = int(jt_pairs[int(pairs[1])-towns-1])+1

from math import factorial as fac

pc = 0

for i in jt_pairs:
      pc = pc * fac(int(i))
      if pc == 0:
            pc += fac(int(i))
if jj_connections == 0:
      pc = pc / towns
if jj_connections > 0:
      pc = pc * fac(jj_connections)

print str(pc)+' 1'
