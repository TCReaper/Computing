

# i am gonna use a list of 8 lists

import random

fish_pond = [ ['.' for x in range(15)] for i in range(8)  ] 

def init():
      global fish_pond
      fish_pond = [ ['.' for x in range(15)] for i in range(8)  ]
      
def inputs():
      x = input('X coordinate <1 to 15>? ')
      y = input('Y coordinate <1 to 8>? ')

      return [x,y]

def stone():
      init()
      coordinates = inputs()
      x = coordinates[0]
      y = coordinates[1]
      fish_pond[int(y)-1][int(x)-1] = 'S'

      #printlist(fish_pond)

def printlist(liSt):
      for List in liSt:
            for element in List:
                  print(element,end='')
            print('')
      
def fishies():
      init()
      for i in range(1):
            new_cood = cood_gen()
            x = new_cood[0]
            y = new_cood[1]
            fish_pond[int(y)-1][int(x)-1] = 'F'
      #printlist(fish_pond)
      
def cood_gen():
      gen = True
      while gen:
            x = random.randint(0,14)
            y = random.randint(0,7)

            if fish_pond[int(y)-1][int(x)-1] == '.':
                  return [x,y]
            else:
                  pass

def feed_fishies():
      init()
      fishies()
      pellet = inputs()
      x = pellet[0]
      y = pellet[1]
      if fish_pond[int(y)-1][int(x)-1] == 'F':
            fish_pond[int(y)-1][int(x)-1] = 'X'
            printlist(fish_pond)
            return 1
      else:
            fish_pond[int(y)-1][int(x)-1] = 'S'
            printlist(fish_pond)
            return 0

def test():
      init()
      x = random.randint(1,15)
      y = random.randint(1,8)
      fishies()
      if fish_pond[int(y)-1][int(x)-1] == 'F':
            fish_pond[int(y)-1][int(x)-1] = 'X'
            #printlist(fish_pond)
            return 1
      else:
            fish_pond[int(y)-1][int(x)-1] = 'S'
            #printlist(fish_pond)
            return 0
      
      
      


##trying = True
##while trying:
##      feed_fishies()

counter = 0
for i in range(100000):
      counter += test()
      #print('\n')
print(counter)
      


























