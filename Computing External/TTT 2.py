
class TTT():
      def __init__(self):
            self._size = int(input('How big do you want your board to be:  '))
            self._board = []
            for i in range(self._size):
                  for x in range(self._size):
                        self._board.append(Node(i,x))
            self._p1 =input('Player 1, what is your name?  ')
            self._p2 =input('Player 2, what is your name?  ')
            
      def print(self):
            nodes = []
            print()
            for i in self._board:
                  nodes.append(i.get_logo())
            i=0
            while i < self._size **2:
                  for row in range(self._size):
                        print(nodes[i],end=' ')
                        i+=1
                  print()
            print()
      
      def play_move(self,team):
            if team == 1:
                  print(self._p1+', it is your turn to play')
            else:
                  print(self._p2+', it is your turn to play')
            while True:
                  row = self.get_coods('row')
                  col = self.get_coods('col')
                  for i in self._board:
                        if i.get_row() == row and i.get_col() == col:
                              if i.is_empty():
                                    i.change_team(team)
                                    return None
                              else:
                                    print('Choose a position that isn\'t filled')
            
                        
      def get_coods(self,dimension):
            while True:
                  try:
                        row = int(input('Choose '+dimension+' [1-'+str(self._size)+']'))
                  except:
                        print('Input valid '+dimension+'!')
                  else:
                        if row < 1 or row > self._size:
                              print('Input valid '+dimension+'!')
                        else:
                              return row-1
      def game_end(self):
            pass

      def check_win(self):
            pass
      def play_game(self):
            round_no = 1
            self.print()
            while not self.game_end():
                  team = round_no % 2
                  self.play_move(team)
                  self.print()
                  round_no += 1


class Node():
      def __init__(self,row,col):
            self._row = row
            self._col = col
            self._team = '='
      def get_row(self):
            return self._row
      def get_col(self):
            return self._col
      def get_logo(self):
            return self._team
      def change_team(self,team):
            self._team = team
      def is_empty(self):
            if self._team == '=':
                  return True
            else:
                  return False

print('\n'*80)
x = TTT()
x.play_game()
