

# pacman

# generation of maze

inputs = False
if inputs:
      height = int(input('Height Of Maze:    '))
      width = int(input('Width Of Maze:    '))
else:
      height = 30
      width = 50

maze = [  ]

lines = [['3' for x in range(width)]]

maze += lines
middle = [[['3'],'0' for i in range(width-2),['3']]]
for i in range(height-2):
      maze += middle
maze += lines

# print maze

def printmaze():
      for line in maze:
            for tile in line:
                  print(tile,end='')
            print('')

