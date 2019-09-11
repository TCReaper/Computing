

def snaketest(coods):
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
                  if coods[1] >= y:
                        y += 1
                        sequence += 'L'
                        direc = 'n'
                  else:
                        y -= 1
                        sequence += 'R'
                        direc = 's'
                        
            elif direc == 'w':
                  if coods[1] < y:
                        y -= 1
                        sequence += 'L'
                        direc = 's'
                  else:
                        y += 1
                        sequence += 'R'
                        direc = 'n'
            
            if [x,y] == coods:
                  #print(sequence)
                  sequence_found = True












for i in range(-5000,5001):
      for e in range(-5000,5001):
            #print(i,e)
            snaketest([i,e])
      #print('$'*50)
