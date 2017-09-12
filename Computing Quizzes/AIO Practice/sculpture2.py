

#     blocks

file = open('artin.txt')

blocks = []

for commands in file:
      commands = commands.split(' ')
      array = []
      for i in commands:
            i = i.strip('\n')
            array.append(int(i))
      blocks.append(array)

file.close()

#print(blocks)
N = blocks[0][0]
tower = [0 for i in range(blocks[1][1])]#height x width
lag = blocks[1][0]
del(blocks[:1])
#only left with block details

#print(tower)
for cmd in blocks[:N+1]:
      time = cmd[0] - lag + 1
      width = cmd[1]
      height = cmd[2]
      temptower = tower
      for i in range(time-1,time-1+width):
            if i > len(tower)-1:
                  #print('out of range')
                  break
            else:
                  tower[i] += height
      #print(tower)

#     max height
maxed = max(tower)
print(maxed)

#     write file
finished = open('artout.txt','w')
finished.write(str(maxed))
finished.close()
      
            
