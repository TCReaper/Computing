# This Python script is an implementation of the game Connect-N.
# It is based on the game: Connect-4, but with an arbitrary number of rows,
# columns, and with n instead of 4 cells required for a win.

# Game parameters
cols = 7   # do not use values over 25 (else it will not fit in default window)
rows = 6   # do not use values over 26 (due to row indexing)
n = 4       # ensure that n <= (rows**2 + cols**2)**0.5
if n > (rows**2 + cols**2)**0.5:
  print("Warning: this game cannot be won!")





################################################################################
# Initialises the board
#
# Input:
#     1. cols: the number of cols
#     2. rows: the number of rows
# 
# Output:
#     1. board: which is represented via
#           - a list of strings (the list has length rows)
#             i.e., each string represents a row
#           - each character in the string to a column
#             (each string has length cols)
#
# Note that the bottom (first) row of the game corresponds to the first element
# of the list, and the top (last) row of the game corresponds to the last
# The columns go from left to right; i.e., the left-most (first) column in the
# game corresponds to the first element of the string (representing that row),
# and the right-most (last) column in the game corresponds to the last element
# of the string (representing that row)
################################################################################
def initialise_board(cols, rows):
  return ["0" * cols] * rows
################################################################################





################################################################################
# Prints the board
#
# Input:
#     1. board: the list of strings representing the board
#
# Refer to the function "initialise_board" for the representation of the board
################################################################################
def print_board(board):
  # the board must be printed in reverse, since we need to print the last
  # (i.e., the top row) first
  for i in range(rows - 1, -1, -1):
    # print the row index (for user to reference during input)
    print(str(chr(64 + rows - i)) + "   "),  # ASCII 65 is "A", 66 is "B", ...
    for j in range(0, cols):
      print(board[i][j] + " "),
    print("\n"),
  # print the column index for users to reference (used for input)
  print("\n    "), # row index whitespace filler
  for i in range(0, cols):
    print(str(i + 1) + (" " * max(0, 2 - len(str(i + 1))))),
  print("\n\n"),
################################################################################





################################################################################
# Requests user input for a move
#
# Input:
#     1. board: the list of strings representing the board
#     2. current_player: refers to the current player's move (i.e., 1 or 2) 
# 
# Refer to the function "initialise_board" for the representation of the board
#
# Output:
#     1. move_col: the column (i.e., move) selected by the current player
################################################################################
def get_user_move(board, current_player):
  valid_selection = False
  print("\n"),
  while not valid_selection:
    # assumes the following user input will be an integer
    move_col = int(input("Player " + str(current_player) + ", please select a column (referring to the board above): ")) - 1
    # repeat until an "empty" column is selected
    if move_col not in range(0, cols):
      print("Invalid column index specified; please input a column from 1 to " + str(cols))
    elif not board[rows - 1][move_col] == "0":
      print("Invalid column index specified; please select a column with an empty cell")
    else:
      valid_selection = True
  return move_col
################################################################################





################################################################################
# Updates the board with the current move
#
# Input:
#     1. board: the list of strings representing the board
#     2. current_player: refers to the current player's move (i.e., 1 or 2)
#     3. move_col: the column (i.e., move) selected by player
#
# Refer to the function "initialise_board" for the representation of the board
# Note that it is assumed that the move_col column in board is not filled
# 
# Output:
#     1. board: the list of strings representing the board (updated)
#     2. move_row: the row index where the current player move is played
################################################################################
def move_update(board, current_player, move_col, rows, cols):
  # traverse rows and find the first empty cell (closest to the bottom row) for
  # the specified column
  move_row = None
  for i in range(0, rows):
    if board[i][move_col] == "0":
      board[i] = board[i][:move_col] + str(current_player) + board[i][move_col + 1:]
      move_row = int(i)
      break
  return board, move_row
################################################################################





################################################################################
# Checks if the game has been won (by either player) or drawn
#
# Input: 
#     1. board: the list of strings representing the board
#     2. player: refers to the current player's move (i.e., 1 or 2)
#     3. move_col: the column (i.e., move) selected by player
#
# Refer to the function "initialise_board" for the representation of the board
# Note that it is assumed that the move_col column in board is already filled
#
# Output:
#     1. game_state:
#           - "0" -> game still ongoing
#           - "1" -> player 1 has won
#           - "2" -> player 2 has won
#           - "3" -> game is a draw
#
################################################################################
def get_game_state(board, current_player, move_col, move_row):
  # check if the game is a draw
  draw = True
  for i in range(0, cols):
    if board[rows - 1][i] == "0":
      draw = False
      break
  if draw:
    return 3
  # get the relevant sub-row where current_player played
  current_row_string = board[move_row][max(0, move_col - (n - 1)):min(cols, move_col + n)]
  # get the relevant sub-column where current_player played
  current_col_string = ""
  for i in range(max(0,move_row - (n - 1)), min(move_row + n, rows)):
    current_col_string = current_col_string + board[i][move_col]
  # get the relevant sub-primary-diagonal where current_player played
  # see notes below for details on finding the diagonal string
  current_pri_diag_string = ""
  top_offset = min(min(rows - 1 - move_row, move_col), (n - 1))
  bottom_offset = min(min(cols - 1 - move_col, move_row), (n - 1))
  current_row = move_row + top_offset
  current_col = move_col - top_offset
  for i in range(0, top_offset + bottom_offset + 1):
    current_pri_diag_string = current_pri_diag_string + board[current_row][current_col]
    current_row = current_row - 1
    current_col = current_col + 1
  # get the relevant sub-secondary-diagonal where current_player played
  # see notes below for details on finding the diagonal string
  current_sec_diag_string = ""
  top_offset = min(min(cols - 1 - move_col, rows - 1 - move_row), (n - 1))
  bottom_offset = min(min(move_col, move_row), (n - 1))
  current_row = move_row - bottom_offset
  current_col = move_col - bottom_offset
  for i in range(0, bottom_offset + top_offset + 1):
    current_sec_diag_string = current_sec_diag_string + board[current_row][current_col]
    current_row = current_row + 1
    current_col = current_col + 1
  # check all the strings to above to see if the current_player has won
  winning_string = str(current_player) * n
  if winning_string in current_row_string or winning_string in current_col_string or winning_string in current_pri_diag_string or winning_string in current_sec_diag_string:
    return current_player
  else:
    return 0
################################################################################
#
# example board (primary diagonal) - current move by P1 at column 3
# A   - - - - - - -
# B   * - - - - - -  1. Find top_offset; number of * cells:
# C   - * - - - - -       min(rows - 1 - move_row, move_col)
# D   - - 1 - - - -  2. Find bottom_offset: number of + cells:
# E   - - 2 + - - -       min(cols - 1 - move_col, move_row)
# F   - - 1 - + - -  3. Check all * and + cells including current move:
#                         rows: move_row + top_offset to
#     1 2 3 4 5 6 7             move_row - bottom_offset
#                         cols: move_col - top_offset to
#                               move_col + bottom_offset
#
# example board (secondary diagonal) - current move by P1 at column 3
# A   - - - - - * -
# B   - - - - * - -  1. Find top_offset; number of * cells:
# C   - - - * - - -       min(cols - 1 - move_col, rows - 1 - move_row)
# D   - - 1 - - - -  2. Find bottom_offset: number of + cells:
# E   - + 2 - - - -       min(move_col, move_row)
# F   + - 1 - - - -  3. Check all * and + cells including current move:
#                         rows: move_row - bottom_offset to
#     1 2 3 4 5 6 7             move_row + top_offset
#                         cols: move_col - bottom_offset to
#                               move_col + top_offset
#
################################################################################





################################################################################
# AI Scripts
################################################################################
def optimal_first_move(turn, rows, cols):
  if turn < 3:
    return 3
  else:
    return None

def random_move(board, rows, cols):
  has_empty_column = False
  for test_col in range(cols):
    if board[rows - 1][test_col] == "0":
      has_empty_column = True
      break
  if not has_empty_column:
    return None
  else:
    import random
    valid_move = False
    rand_col = -1
    while not valid_move:
      rand_col = random.randint(0, cols - 1)
      if board[-1][rand_col] not in ["1", "2"]:
        valid_move = True
        break
    return rand_col

def check_can_win_in_one_move(board, player, rows, cols):
  can_win_in_one_move = False
  for sim_col_move in range(cols):
    if board[-1][sim_col_move] == "0":
      temp_board = board[:]
      temp_board, sim_move_row = move_update(temp_board, player, sim_col_move, rows, cols)
      game_state = get_game_state(temp_board, player, sim_col_move, sim_move_row)
      if game_state == player:
        can_win_in_one_move = True
        return sim_col_move
  if not can_win_in_one_move:
    return None

def check_must_block_in_one_move(board, player, rows, cols):
  must_block_in_one_move = False
  player = player % 2 + 1 # check other player's move - to see if we must block
  for sim_col_move in range(cols):
    if board[-1][sim_col_move] == "0":
      temp_board = board[:]
      temp_board, sim_move_row = move_update(temp_board, player, sim_col_move, rows, cols)
      game_state = get_game_state(temp_board, player, sim_col_move, sim_move_row)
      if game_state == player:
        must_block_in_one_move = True
        return sim_col_move   # blocking move for current player
  if not must_block_in_one_move:
    return None  # no threat; no need to block

def check_can_win_in_two_moves(board, player, rows, cols):
  can_win_in_two_moves = False
  for sim_col_move1 in range(cols):
    if board[-1][sim_col_move1] == "0":
      temp_board = board[:]
      temp_board, sim_move_row1 = move_update(temp_board, player, sim_col_move1, rows, cols)
      game_state1 = get_game_state(temp_board, player, sim_col_move1, sim_move_row1)
      for sim_col_move2 in range(cols):
        if temp_board[-1][sim_col_move2] == "0":
          temp_board, sim_move_row2 = move_update(temp_board, player, sim_col_move2, rows, cols)
          game_state2 = get_game_state(temp_board, player, sim_col_move2, sim_move_row2)   
          if game_state2 == player:
            can_win_in_two_moves = True
            return sim_col_move1
  if not can_win_in_two_moves:
    return None

def check_must_block_in_two_moves(board, player, rows, cols):
  must_block_in_two_moves = False
  player = player % 2 + 1 # check other player's move - to see if we must block
  for sim_col_move1 in range(cols):
    if board[-1][sim_col_move1] == "0":
      temp_board = board[:]
      temp_board, sim_move_row1 = move_update(temp_board, player, sim_col_move1, rows, cols)
      game_state1 = get_game_state(temp_board, player, sim_col_move1, sim_move_row1)
      for sim_col_move2 in range(cols):
        if temp_board[-1][sim_col_move2] == "0":
          temp_board, sim_move_row2 = move_update(temp_board, player, sim_col_move2, rows, cols)
          game_state2 = get_game_state(temp_board, player, sim_col_move2, sim_move_row2)
          if game_state2 == player:
            must_block_in_two_moves = True
            return sim_col_move1   # blocking move for current player
  if not must_block_in_two_moves:
    return None  # no threat (over 2 moves); no need to block

def AI_random_move(board, rows, cols):
  return random_move(board, rows, cols)

def AI_middle_first_then_random_move(board, turn, rows, cols):
  move = optimal_first_move(turn, rows, cols)
  if move != None:
    return move
  move = random_move(board, rows, cols)
  if move != None:
    return move
  print("No valid moves left.")

def AI_try_winblock_then_random_move(board, player, rows, cols):
  move = check_can_win_in_one_move(board, player, rows, cols)
  if move != None:
    return move
  move = check_must_block_in_one_move(board, player, rows, cols)
  if move != None:
    return move
  move = random_move(board, rows, cols)
  if move != None:
    return move
  print("No valid moves left.")

def AI_try_dominate_offensive_then_winblock_then_random_move(board, player, rows, cols):
  move = check_can_win_in_one_move(board, player, rows, cols)
  if move != None:
    return move
  move = check_must_block_in_one_move(board, player, rows, cols)
  if move != None:
    return move
  move = check_can_win_in_two_moves(board, player, rows, cols)
  if move != None:
    return move
  move = random_move(board, rows, cols)
  if move != None:
    return move
  print("No valid moves left.")

def AI_try_dominate_defensive_then_winblock_then_random_move(board, player, rows, cols):
  move = check_can_win_in_one_move(board, player, rows, cols)
  if move != None:
    return move
  move = check_must_block_in_one_move(board, player, rows, cols)
  if move != None:
    return move
  move = check_must_block_in_two_moves(board, player, rows, cols)
  if move != None:
    return move
  move = random_move(board, rows, cols)
  if move != None:
    return move
  print("No valid moves left.")  
################################################################################










################################################################################
exit_game_menu = False
player1 = None
player2 = None
while not exit_game_menu:
  print("\n\nPlease select Player 1 mode: ")
  print("(1) Human")
  print("(2) AI - makes random moves")
  print("(3) AI - optimal first move then makes random moves")
  print("(4) AI - tries to win/block before making random move")
  print("(5) AI - tries to win/block/form-3 before making random move")
  print("(6) AI - tries to win/block/stop-3 before making random move")
  print("(7) Exit\n")

  need_input = True
  while need_input:
    choice = int(input("Please select an option: "))
    if choice in range(1, 8):
      need_input = False
      if choice == 7:
        exit_game_menu = True
        break
      else:
        player1 = choice
      print("Player 1 mode: " + str(choice) + ".\n")
    else:
      print("Invalid option entered.\n")

  if exit_game_menu:
    break

  print("\n\nPlease select Player 2 mode: ")
  print("(1) Human")
  print("(2) AI - makes random moves")
  print("(3) AI - optimal first move then makes random moves")
  print("(4) AI - tries to win/block before making random move")
  print("(5) AI - tries to win/block/form-3 before making random move")
  print("(6) AI - tries to win/block/stop-3 before making random move")
  print("(7) Exit\n")

  need_input = True
  while need_input:
    choice = int(input("Please select an option: "))
    if choice in range(1, 8):
      need_input = False
      if choice == 7:
        exit_game_menu = True
        break
      else:
        player2 = choice
      print("Player 2 mode: " + str(choice) + ".\n")
    else:
      print("Invalid option entered.\n")

  if exit_game_menu:
    break

  turn = 1
  board = initialise_board(cols, rows)
  game_over = False
  current_player = 2  # starts at 2 as player is switched at the start of the loop
  print("Turn: 0")
  print_board(board)
  while not game_over:
    if current_player == 1:
      current_player = 2
      if player2 == 1:
        move_col = get_user_move(board, current_player)
      elif player2 == 2:
        move_col = AI_random_move(board, rows, cols)
      elif player2 == 3:
        move_col = AI_middle_first_then_random_move(board, turn, rows, cols)
      elif player2 == 4:
        move_col = AI_try_winblock_then_random_move(board, current_player, rows, cols)
      elif player2 == 5:
        move_col = AI_try_dominate_offensive_then_winblock_then_random_move(board, current_player, rows, cols)
      elif player2 == 6:
        move_col = AI_try_dominate_defensive_then_winblock_then_random_move(board, current_player, rows, cols)        
    elif current_player == 2:
      current_player = 1
      if player1 == 1:
        move_col = get_user_move(board, current_player)
      elif player1 == 2:
        move_col = AI_random_move(board, rows, cols)
      elif player1 == 3:
        move_col = AI_middle_first_then_random_move(board, turn, rows, cols)
      elif player1 == 4:
        move_col = AI_try_winblock_then_random_move(board, current_player, rows, cols)
      elif player1 == 5:
        move_col = AI_try_dominate_offensive_then_winblock_then_random_move(board, current_player, rows, cols)
      elif player1 == 6:
        move_col = AI_try_dominate_defensive_then_winblock_then_random_move(board, current_player, rows, cols)
    board, move_row = move_update(board, current_player, move_col, rows, cols)
    print("Turn: " + str(turn))
    print_board(board)
    game_state = get_game_state(board, current_player, move_col, move_row)
    if game_state > 0:
      if game_state == 3:
        print("\nDraw!")
      elif game_state == 1 or game_state == 2:
        print("\nPlayer " + str(current_player) + " has won! (col: " + str(move_col + 1) + ")\n\n")
      game_over = True
    turn += 1

  need_input = True
  while need_input:
    choice = input("\n\nPlay another game? [Y/N] ").lower()
    if choice in ["y", "ye", "yes", "n", "no"]:
      need_input = False
      if choice in ["n", "no"]:
        exit_game_menu = True
        break
    else:
      print("Invalid option entered.\n")  
################################################################################
