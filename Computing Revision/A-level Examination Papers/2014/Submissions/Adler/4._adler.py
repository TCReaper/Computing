#4.1
#grid will be an class (class Grid) using an array of rows,
#which is represented by a class data structure (class Row),
#which takes in parameter of its row number,
#and is an array consisting of nodes (class Node),
#that has parameters: data (ascii code); x-coordinate(int); y-coordinate(int),
#with get, set, and print methods

import random

class Grid():
    def __init__(self):
        self._grid = [None] + [Row(i) for i in range(1, 9)]
        self._fish_count = 0

    def display(self):
        for i in range(1, len(self._grid)):
            self._grid[i].display()
            print()

    def reset(self):
        self.__init__()

    def _get_coordinates(self):
        while True:
            x = input('X coordinate <1 to 15>? ')
            if x.isdigit():
                x = int(x)
                if x in range(1, 16):
                    break
            print("Invalid input! Enter a valid X coordinate.")
        while True:
            y = input('y coordinate <1 to 8>? ')
            if y.isdigit():
                y = int(y)
                if y in range(1, 9):
                    break
            print("Invalid input! Enter a valid Y coordinate.")
        return x, y
    
##    def throw_stone(self):
##        x, y = self._get_coordinates()
##        self._grid[y].get_node(x).set_data(83)
##        self.display()
    
    def throw_stone(self): #killing fish lmaooo
        x, y = self._get_coordinates()
        temp_node = self._grid[y].get_node(x)
        if temp_node.get_data() == 70 or 72:
            temp_node.set_data(88)
        else:
            temp_node.set_data(83)
        self.display()
        
    def add_three_fish(self):
        while self._fish_count != 3:
            self.add_fish()
        self.display()
            
    def add_fish(self):
        if self._fish_count < 3:
            x = random.randint(1, 15)
            y = random.randint(1, 8)
            self._grid[y].get_node(x).set_data(70)
            self._fish_count += 1

    def throw_pellet(self):
        x, y = self._get_coordinates()
        temp_node = self._grid[y].get_node(x)
        if temp_node.get_data() == 70:
            temp_node.set_data(72)
        elif temp_node.get_data() == 46:
            temp_node.set_data(80)
        #else:
            #raise IndexError
        self.display()

class Row():
    def __init__(self, row_num):
        self._row_num = row_num
        self._row = [None] + [Node(i, self._row_num) for i in range(1, 16)]

    def display(self):
        for i in range(1, len(self._row)):
            self._row[i].display()

    def reset(self):
        self.__init__(row_num)

    def get_node(self, x): #where x is the node's x-coordinate
        return self._row[x]
        
class Node():
    #node's data is represented by ascii code values of:
    #. for one sq m of water (i.e.: nothing there)
    #S for stone impact position;
    #F for fish
    #P for pellet
    #H for happy (fed) fish
    #X for dead fish LOL
    def __init__(self, x, y, data = 46):
        #where x is the x-coordinate and y is the y-coordinate
        self._data = data
        self._x = x
        self._y = y

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data

    def get_x(self):
        return self._x

    def set_x(self, new_x):
        self._x = new_x

    def get_y(self):
        return self._y

    def set_y(self, new_y):
        self._y = new_y

    def display(self):
        print(chr(self._data), end = '')

grid = Grid()
grid.add_three_fish()

#53:35.15, excluding dead fish lol
