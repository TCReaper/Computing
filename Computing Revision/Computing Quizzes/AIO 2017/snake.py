
import sys
sys.setrecursionlimit(1000000000)

file = open('snakein.txt')
coods = []
for i in file:
      i = i.strip('\n')
      i = i.split(' ')
      for cood in i:
            cood = cood.strip('\t')
            cood = cood.strip()
            cood = cood.strip('\n')
            coods.append(int(cood))
file.close()

sequence = ''
sequence_found = False
x = 0
y = 0
direc = 'n'
while not sequence_found:
      if direc == 'n':
            if coods[0] <= x:
                  x -= 1
                  sequence += 'L'
                  direc = 'w'
            else:
                  x += 1
                  sequence += 'R'
                  direc = 'e'
                  
      elif direc == 's':
            if coods[0] > x:
                  x += 1
                  sequence += 'L'
                  direc = 'e'
            else:
                  x -= 1
                  sequence += 'R'
                  direc = 'w'
                  
      elif direc == 'e':
            if coods[1] > y:
                  y += 1
                  sequence += 'L'
                  direc = 'n'
            else:
                  y -= 1
                  sequence += 'R'
                  direc = 's'
                  
      elif direc == 'w':
            if coods[1] <= y:
                  y -= 1
                  sequence += 'L'
                  direc = 's'
            else:
                  y += 1
                  sequence += 'R'
                  direc = 'n'

      if [x,y] == coods:
            sequence_found = True
            
final = open('snakeout.txt','w')
final.write(str(sequence))
final.close()
