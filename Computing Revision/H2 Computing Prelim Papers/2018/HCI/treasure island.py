
# treasure island

import random

class IslandClass():
      def __init__(self,grid_length=30,grid_height=10):
            self._length = grid_length
            self._height = grid_height
            self._grid = [['.' for i in range(self._length)] \
                          for i in range(self._height)]

      def HideTreasure(self):
            x = random.randint(0,self._length-1)
            y = random.randint(0,self._height-1)

            if self._grid[y][x] != 'T':
                  self._grid[y][x] = 'T'
            else:
                  return 'Already a special tile!'

      def DigHole(self,row,column):
            if self._grid[column][row] == 'T':
                  self._grid[column][row] = 'X'
            elif self._grid[column][row] == '.':
                  self._grid[column][row] = 'O'
            else:
                  return 'Already dug!'

      def GetSquare(self,row,column):
            return self._grid[column][row]

      def DisplayGrid(self):
            for row in self._grid:
                  print(''.join(row))


island = IslandClass()
for i in range(3):
      island.HideTreasure()
island.DisplayGrid()

def validation(value,min_val,max_val):
      query = input('Input value for {0} between {1} & {2}]:  '.format( \
            value,min_val,max_val))
      query = int(query)
      if query <= max_val and query >= min_val:
            return query
      else:
            return validation(value,min_val,max_val)

while True:
      x = validation('x-value',0,29)
      y = validation('y-value',0,9)
      
      island.DigHole(x,y)
      island.DisplayGrid()
      
