##The grid utilises a 2D list for representation
##The program will use a fixed number sequence: [1,2,3,4]
##The first row reverses the number set
##The second row swaps the last two elements in the number set
##The third row swaps two halves of the number set by column
##The fourth row swaps the first two elements in the number set

def reverse(s):
    a = s[::-1]
    return a

def swap_back_two(s):
    a = s[:-2] + s[-1] + s[-2]
    return a

def swap_column_halves(s):
    a = s[len(s)//2:] + s[:len(s)//2]
    return a

def swap_front_two(s):
    a = s[1] + s[0] + s[2:]
    return a

def display(grid):
    for i in range(len(grid)):
        print(" ".join(grid[i]))
    print()
    
    
grid = []
numset = "1234"
grid.append(list(reverse(numset)))
grid.append(list(swap_back_two(numset)))
grid.append(list(swap_column_halves(numset)))
grid.append(list(swap_front_two(numset)))

display(grid)

from random import randint

def quadrant_row_swap(grid,r1,r2):
    ##Swaps the r1-th element in the grid with the r2-th element;
    ##Each grid element is the row
    grid[r1],grid[r2] = grid[r2],grid[r1]
    return grid

def quadrant_col_swap(grid,c1,c2):
    ##Swaps the c1-th element in the grid with the c2-th element in each row
    for i in range(len(grid)):
        grid[i][c1],grid[i][c2] = grid[i][c2],grid[i][c1]
    return grid

def half_row_swap(grid):
    ##Swaps the first half and the second half of rows
    grid[:len(grid)//2],grid[len(grid)//2:] = grid[len(grid)//2:],grid[:len(grid)//2]
    return grid

def half_col_swap(grid):
    ##Swaps the first half and the second half of columns
    for i in range(len(grid)):
        grid[i][:len(grid[i])//2],grid[i][len(grid[i])//2:] = grid[i][len(grid[i])//2:],grid[i][:len(grid[i])//2]
    return grid

transformations = {quadrant_row_swap : "Swaps two rows in the same quadrants",
                   quadrant_col_swap : "Swaps two columns in the same quadrants",
                   half_row_swap : "Swaps the top and bottom quadrant rows entirely",
                   half_col_swap : "Swaps the left and right quadrant columns entirely"}

for i in range(1,3):
    trans = list(transformations.keys())[randint(0,len(transformations)-1)]
    print("Transformation ",i,": ",transformations[trans],sep="")

    if trans == quadrant_row_swap or trans == quadrant_col_swap:
        a1 = randint(0,len(grid)-1)
        a2 = randint(0,len(grid)-1)
        while a2 == a1:
            a2 = randint(0,len(grid)-1)
        grid = trans(grid,a1,a2)
    else:
        grid = trans(grid)
        
    display(grid)
    
