#TASK 4.1 - Evidence 18
def initiate_board(size):
    pass

#TASK 4.2 - Evidence 19
def display_board(board):
    pass

def test_initate_display():
    for i in range(1, 11):
        b = initiate_board(i)
        display_board(b)
test_initate_display()

#TASK 4.3 - Evidence 20
def reverse(board, row, col, disc):
    pass

def reverse_recursive(board, row, col, disc):
    pass

def test():
    b1 = [[" "," "," "," "," "," "," "," "],
          [" "," "," "," "," "," "," "," "],
          [" "," "," "," "," "," "," "," "],
          [" "," "," ","X","O"," "," "," "],
          [" "," "," ","O","X"," "," "," "],
          [" "," "," "," "," "," "," "," "],
          [" "," "," "," "," "," "," "," "],
          [" "," "," "," "," "," "," "," "]]
    display_board(b1)    
    reverse(b1, 2,3,"O")
    display_board(b1)
    reverse(b1, 2,2,"X")
    display_board(b1)
    reverse(b1, 3,2,"O")
    display_board(b1)
    reverse(b1, 4,2,"X")
    display_board(b1)
    reverse(b1, 3,1,"O")
    display_board(b1)
    reverse(b1, 2,0,"X")
    display_board(b1)
    reverse(b1, 2,1,"O")
    display_board(b1)
    reverse(b1, 1,0,"X")
    display_board(b1)
    reverse(b1, 3,0,"O")
    display_board(b1)
    reverse(b1, 4,0,"X")
    display_board(b1)
    reverse(b1, 1,1,"O")
    display_board(b1)
    reverse(b1, 0,0,"X")
    display_board(b1)
    reverse(b1, 5,4,"O")
    display_board(b1)
    reverse(b1, 6,5,"X")
    display_board(b1)
print("test")
test()
    
def test1():
    b1 = initiate_board()
    b1[3][3]="X"
    b1[2][3]="X"
    b1[1][3]="X"
    b1[0][3]="O"
    display_board(b1)    
    reverse(b1, 4,3,"O")
    display_board(b1)


def test2():
    b1 = initiate_board()
    b1[0][3]="X"
    b1[1][3]="O"
    b1[2][3]="O"
    b1[3][3]="O"
    b1[3][4]="O"
    b1[2][5]="O"
    b1[1][6]="O"
    b1[0][7]="O"
    b1[4][4]="O"
    b1[4][5]="O"
    b1[4][6]="X"
    b1[4][2]="O"
    b1[4][1]="O"
    b1[4][0]="X"
    b1[5][4]="O"
    b1[6][5]="O"
    b1[7][6]="X"
    b1[5][3]="O"
    b1[6][3]="O"
    b1[7][3]="X"
    b1[5][2]="O"
    b1[6][1]="O"
    b1[7][0]="X"
    b1[3][2]="O"
    b1[2][1]="O"
    b1[1][0]="X"
    display_board(b1)    
    reverse(b1, 4,3,"X")
    display_board(b1)


def test3():
    b1 = initiate_board()
    b1[0][3]="X"
    b1[1][3]="O"
    b1[2][3]="O"
    b1[3][3]="O"
    b1[2][5]="O"
    b1[1][6]="O"
    b1[0][7]="X"
    b1[4][4]="O"
    b1[4][5]="O"
    b1[4][6]="X"
    b1[4][3]="O"
    b1[4][2]="O"
    b1[4][1]="O"
    b1[4][0]="X"
    b1[5][4]="O"
    b1[6][5]="O"
    b1[7][6]="X"
    b1[5][3]="O"
    b1[6][3]="O"
    b1[7][3]="X"
    b1[5][2]="O"
    b1[6][1]="O"
    b1[7][0]="X"
    b1[3][2]="O"
    b1[2][1]="O"
    b1[1][0]="X"
    display_board(b1)    
    reverse(b1, 3,4,"X")
    display_board(b1)


def test4():
    b1 = initiate_board()
    b1[0][3]="X"
    b1[1][3]="O"
    b1[2][3]="O"
    b1[3][3]="O"
    b1[3][4]="O"
    b1[2][5]="O"
    b1[1][6]="O"
    b1[0][7]="X"
    b1[4][4]="O"
    b1[4][5]="O"
    b1[4][6]="X"
    b1[4][2]="O"
    b1[4][1]="O"
    b1[4][0]="X"
    b1[5][4]="O"
    b1[6][5]="O"
    b1[7][6]="X"
    b1[5][3]="O"
    b1[6][3]="O"
    b1[7][3]="X"
    b1[5][2]="O"
    b1[6][1]="O"
    b1[7][0]="X"
    b1[3][2]="O"
    b1[2][1]="O"
    b1[1][0]="X"
    display_board(b1)    
    reverse(b1, 4,3,"O")
    display_board(b1)
#print("test1")
#test1()
#print("test2")
#test2()
#print("test3")
#test3()
#print("test4")
#test4()
