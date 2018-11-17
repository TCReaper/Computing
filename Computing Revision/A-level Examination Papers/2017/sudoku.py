

def init_grid():
      grid = [['4','3','2','1'],
              ['1','2','4','3'],
              ['3','4','1','2'],
              ['2','1','3','4']]
      return grid

grid = init_grid()

def display(grid):
      for row in range(len(grid)):
            print(' '.join(grid[row]))

display(grid)

import random

def swap_row(grid):
      quadrant = random.randint(0,1)
      if quadrant == 0:
            grid[0],grid[1]=grid[1],grid[0]
      else:
            grid[2],grid[3]=grid[3],grid[2]
      return grid

def swap_col(grid):
      quadrant = random.randint(0,1)
      if quadrant == 0:
            return swap_columns(grid,0,1)
      else:
            return swap_columns(grid,2,3)
      
def swap_columns(grid,col,col2):
      for row in range(len(grid)):
            grid[row][col],grid[row][col2]=grid[row][col2],grid[row][col]
      return grid

def swap_rquad(grid):
      grid[0],grid[1],grid[2],grid[3]=\
      grid[2],grid[3],grid[0],grid[1]

      return grid

def swap_cquad(grid):
      grid = swap_columns(grid,0,2)
      return swap_columns(grid,1,3)

choices = ['Swaps two rows in same quad','Swap two col in same quad',\
           'swap top and bottom rows','swap left and right col']

def action(grid):
      choice = random.randint(1,4)

      if choice == 1:
            grid = swap_row(grid)
      elif choice == 2:
            grid = swap_col(grid)
      elif choice == 3:
            grid = swap_rquad(grid)
      else:
            grid = swap_cquad(grid)
      print('Transformation {0}: {1}'.format(choice,choices[choice-1]))
      return grid

grids = []
repeats = 0
grids.append(grid)
while True:
      temp = action(grid)
      if temp in grids:
            repeats += 1
      else:
            grids.append(temp)
      print('Unique: {0}, Repeats: {1}'.format(len(grids),repeats))
      
      
