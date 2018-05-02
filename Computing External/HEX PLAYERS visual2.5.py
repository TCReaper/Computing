import random, timeit, time, winsound
from math import floor, ceil
red_delta, blue_delta = ((1,0),(1,-1),(0,1),(0,-1)), ((-1,0),(-1,1),(0,1),(1,0))
delta_board = ((1,0),(1,-1),(-1,1),(-1,0),(0,1),(0,-1))
red_one_change = ((1,0),(1,-1),(0,-1),(0,1),(-1,1))
blue_one_changeR, blue_one_changeL = ((0,1),(-1,1),(1,0),(1,-1),(-1,0)), ((0,-1),(-1,0),(1,-1),(1,0),(-1,1))
blue_bridge_delta, red_bridge_delta = ((-1,2),(1,1),(2,-1),(-2,1)), ((2,-1),(1,1),(1,-2))
red_row, red_col = None, None
red_first_row, red_first_col = None, None

def calculate_mean(sample_data):
    s = sum(sample_data)
    N = len(sample_data)
    mean = s / N
    return mean

def calculate_median(sample_data):
    sample_data = sorted(sample_data)
    N = len(sample_data)
    if N % 2 == 0:
        x1 = int(N/2)
        x2 = int(N/2)-1
        median = (sample_data[x1]+sample_data[x2])/2
    else:
        x = int((N-1)/2)
        median = sample_data[x]
    return median

class Hex(object):
    def __init__(self, board_size, if_win):
        self.board_size = board_size
        self.if_win = if_win
        self._board = [[' O ' for col in range(bs)] for row in range(bs)]
        
    def print_board(self):
        spacing = 0
        print('\n')
        for row in self._board:
            board_circles =''.join(row)
            print('  '*spacing + board_circles)
            spacing += 1
            
    def start_play(self):
        global board, win, colour, moveCounter, user_row, user_col, red_row, red_col, blue_row, blue_col, red_first_row, red_first_col
        win = self.if_win
        moveCounter = 0
        while win != True:
            if moveCounter%2 == 0:
                colour, colour_list, playing_type = 'Red', red_cells, Rplay
            else:
                colour, colour_list, playing_type = 'Blue', blue_cells, Bplay
            if moveCounter == 0:
                user_row = 0
                user_col = random.randint(0,bs-1)
                #user_col = 0
                red_row, red_col = user_row, user_col
                red_first_row, red_first_col = user_row, user_col
            elif moveCounter == 1:
                while True:
                    user_row = random.randint(0,bs-1)
                    #user_row = 1
                    if red_first_col > (bs/2)-1:
                        user_col = bs-1
                    else:
                        user_col = 0
                    if self._board[user_row][user_col] == ' O ':
                        break
                blue_row, blue_col = user_row, user_col
            else:
                user_row, user_col = self.choose_move(playing_type, colour)
            if colour == 'Red':
                self._board[user_row][user_col] = ' R '
            else:
                self._board[user_row][user_col] = ' B '
            colour_list.append((user_row,user_col))
            moveCounter += 1
            self.print_board()
            if (red_checked and blue_checked) == False and win != True:
                self.start_checking()
                
    def choose_move(self, play, colour):
        global red_row, red_col, blue_row, blue_col
        print("red row: {0}, red col: {1}".format(red_row, red_col))
        if colour == 'Red':
            colour_row, colour_col = red_row, red_col
        else:
            colour_row, colour_col = blue_row, blue_col
        get_input, flag = True, True
        if play == 'Human': #HUMAN PLAYER
            while get_input:
                row = int(input("\n{0},please choose a row to place your stone : ".format(colour)))-1
                col = int(input("{0},please choose a column to place your stone : ".format(colour)))-1
                if self._board[row][col] == ' O ':
                    get_input = False 
                else:
                    print("Please input appropriate values!\n")
        elif play == 'Random': #RANDOM PLAYER
            while get_input:
                randrow = random.randint(0,bs-1)
                randcol = random.randint(0,bs-1)
                if self._board[randrow][randcol] == ' O ':
                    row, col = randrow, randcol
                    get_input = False
        elif play == 'OneMove': #ONE MOVE PLAYER
            if red_first_col > (bs/2)-1:
                blue_one_change = blue_one_changeL
            else:
                blue_one_change = blue_one_changeR
            while get_input:
                for i in blue_one_change:
                    new_row, new_col = blue_row+i[0], blue_col+i[1]
                    if (new_row in range(bs)) and (new_col in range(bs)):
                        if self._board[new_row][new_col] == ' O ':
                            row, col = new_row, new_col
                            flag = False
                    if flag == False:
                        get_input = False
                        break
                if flag:
                    k = len(red_cells)
                    for i in range(2,k+1):
                        temp_row, temp_col = blue_cells[k-i][0], blue_cells[k-i][1]
                        for j in blue_one_change:
                            new_row, new_col = temp_row+j[0], temp_col+j[1]
                            if (new_row in range(bs)) and (new_col in range(bs)):
                                if self._board[new_row][new_col] == ' O ':
                                    row, col = new_row, new_col
                                    flag = False
                            if flag == False:
                                break
                        if flag or flag == False:
                            get_input = False
                            break
                if flag:
                    while True:
                        new_row = random.randint(0,bs-1)
                        if red_first_col > (bs/2)-1:
                            new_col = bs-1
                        else:
                            new_col = 0
                        if self._board[new_row][new_col] == ' O ':
                            row, col = new_row, new_col
                            flag == False
                            break
                    if flag == False:
                        get_input = False
            print("1mp before return row {0} col {1}".format(row, col))
            blue_row, blue_col = row, col
        elif play == 'TwoBridge': #TWO BRIDGE PLAYER
            bridge_found, connect_found, stopper = False, False, False
            while get_input:
                for j in two_bridges:
                    x = two_bridges.index(j)
                    start_row, start_col = connects[x][0][0], connects[x][0][1]
                    end_row, end_col = connects[x][1][0], connects[x][1][1]
                    if self._board[j[0][0]][j[0][1]] == " R " and self._board[j[1][0]][j[1][1]] == " R ":
                        if self._board[start_row][start_col] == " R " or self._board[end_row][end_col] == " R ":
                            del two_bridges[two_bridges.index(j)]
                for i in red_bridge_delta:
                    new_row, new_col = red_row+i[0], red_col+i[1]
                    if new_row in range(bs) and new_col in range(bs):
                        if self._board[new_row][new_col] == ' O ':
                            row_avg, col_avg = (red_row+new_row)/2, (red_col+new_col)/2
                            if self._board[floor(row_avg)][ceil(col_avg)] == ' O ' and self._board[ceil(row_avg)][floor(col_avg)] == ' O ':
                                two_bridges.append(((red_row, red_col),(new_row, new_col)))
                                connects.append(((floor(row_avg),ceil(col_avg)),(ceil(row_avg),floor(col_avg))))
                                bridge_found = True
                    if bridge_found:
                        row, col = new_row, new_col
                        get_input = False
                        break
                print("two bridges: {0}".format(two_bridges))
                print("connects {0}".format(connects))
                for cell in red_cells:
                    if cell[0] == bs-1:
                        stopper = True
                        break
                for j in connects:
                    x = connects.index(j)
                    start_row, start_col = two_bridges[x][0][0], two_bridges[x][0][1]
                    end_row, end_col = two_bridges[x][1][0], two_bridges[x][1][1]
                    if self._board[start_row][start_col] == " R " and self._board[end_row][end_col] == " R ":
                        R1, C1, R2, C2 = j[0][0], j[0][1], j[1][0], j[1][1]
                        if connect_found == False:
                            if self._board[R1][C1] == ' B ' and self._board[R2][C2] == ' O ':
                                row, col = R2, C2
                                connect_found = True
                        if connect_found == False:
                            if self._board[R2][C2] == ' B ' and self._board[R1][C1] == ' O ':
                                row, col = R1, C1
                                connect_found = True
                        if connect_found:
                            del connects[connects.index(j)]
                            get_input = False
                            break
                if stopper and connect_found == False:
                    for j in connects:
                        x = connects.index(j)
                        start_row, start_col = two_bridges[x][0][0], two_bridges[x][0][1]
                        end_row, end_col = two_bridges[x][1][0], two_bridges[x][1][1]
                        if self._board[start_row][start_col] == " R " and self._board[end_row][end_col] == " R ":
                            R1, C1, R2, C2 = j[0][0], j[0][1], j[1][0], j[1][1]
                            if self._board[R1][C1] == ' O ':
                                row, col = R1, C1
                                connect_found = True
                            if connect_found == False:
                                if self._board[R2][C2] == ' O ':
                                    row, col = R2, C2
                                    connect_found = True
                            if connect_found:
                                del connects[connects.index(j)]
                                get_input = False
                                break
                if (bridge_found == False) and (connect_found == False):
                    for g in red_one_change:
                        new_row, new_col = red_row+g[0], red_col+g[1]
                        if new_row in range(bs) and new_col in range(bs):
                            if self._board[new_row][new_col] == ' O ':
                                row, col = new_row, new_col
                                flag = False
                        if flag == False:
                            get_input = False
                            break
                    if flag:
                        k = len(red_cells)
                        for i in range(2,k+1):
                            temp_row, temp_col = red_cells[k-i][0], red_cells[k-i][1]
                            for j in red_one_change:
                                new_row, new_col = temp_row+j[0], temp_col+j[1]
                                if new_row in range(bs) and new_col in range(bs):
                                    if self._board[new_row][new_col] == ' O ':
                                        row, col = new_row, new_col
                                        flag = False
                                if flag == False:
                                    break
                            if flag == False:
                                get_input = False
                                break
            print("2bp before return row {0} col {1}".format(row, col))
            if connect_found == False:
                red_row, red_col = row, col
        return row, col
    
    def start_checking(self):
        R1, R2, B1, B2 = False, False, False, False 
        for cell in red_cells:
            for x in range(bs):
                if cell == (0,x):
                    R1 = True
                    if cell not in top_cells:
                        top_cells.append(cell)
                elif cell == (bs-1,x):
                    R2 = True
        if R1 and R2:
            self.connection_checker('Red')
            red_checked = True
        for cell in blue_cells:
            for x in range(bs):
                if cell == (x,0):
                    B1 = True
                    if cell not in left_cells:
                        left_cells.append(cell)
                elif cell == (x, bs-1):
                    B2 = True
        if B1 and B2:
            self.connection_checker('Blue')
            blue_checked = True
            
    def connection_checker(self, colour_choice): 
        global win, red_win, blue_win
        if colour_choice == 'Red':
            colour_delta, colour_conn, start_cells, part = red_delta, Rconn, top_cells, ' R '
        elif colour_choice == 'Blue':
            colour_delta, colour_conn, start_cells, part = blue_delta, Bconn, left_cells, ' B '
        for cell in start_cells:
            for index, x in enumerate(colour_delta):
                new_r, new_c = cell[0]+x[0], cell[1]+x[1]
                if (new_r in range(bs)) and (new_c in range(bs)) and ((new_r,new_c) not in colour_conn) and ((new_r,new_c) not in start_cells) and self._board[new_r][new_c] == part:
                    colour_conn.append((new_r,new_c))
        for cell in colour_conn:
            for index, y in enumerate(delta_board):
                new_r, new_c = cell[0]+y[0], cell[1]+y[1]
                if (new_r in range(bs)) and (new_c in range(bs)) and ((new_r,new_c) not in colour_conn) and ((new_r,new_c) not in start_cells) and self._board[new_r][new_c] == part:
                    colour_conn.append((new_r,new_c))
            if win == False:
                if colour_choice == 'Red':
                    if cell[0] == self.board_size-1:
                        print("RED WIN")
                        red_win += 1
                        win = True
                elif colour_choice == 'Blue':
                    if cell[1] == self.board_size-1:
                        print("BLUE WIN")
                        blue_win += 1
                        win = True
            if win:
                break
                
                                          
global  red_win, blue_win, red_cells
Rplay, Bplay = 'TwoBridge', 'OneMove'
played, red_win, blue_win, timings = 0, 0, 0, []
bs = int(input("Choose a board size : "))
repeat = int(input("Number of games to be played: "))
while played<repeat:
    red_cells, blue_cells, top_cells, left_cells, Rconn, Bconn, red_checked, blue_checked, two_bridges, connects = [], [], [], [], [], [], False, False, [], []
    game = Hex(bs, False)
    game.print_board()
    start_time = timeit.default_timer()
    game.start_play()
    stop_time = timeit.default_timer()
    print("Time taken for game : {0} seconds".format(str(round(stop_time-start_time, 6))))
    timings.append(stop_time-start_time)
    played += 1
    #time.sleep(2)
red_win_rate = round((red_win/played)*100, 4)
blue_win_rate = round((blue_win/played)*100, 4)
print("\nOut of {0} games played on a {1}x{1} board, {2} won {3}% of the games & {4} won {5}% of the games".format(played, bs, Rplay, red_win_rate, Bplay, blue_win_rate))
print("Mean time for a game: {0} s; Median time for a game : {1} s".format(round(calculate_mean(timings), 6), round(calculate_median(timings), 6)))
winsound.Beep(2500, 2000)
    

