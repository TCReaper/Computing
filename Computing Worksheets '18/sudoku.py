#sudoku

#1a


class Cell():
      def __init__(self,row,col):
            self._row = row
            self._col = col
            self._data = 0
            
      def set_data(self,data):
            self._data = data
      def get_data(self):
            return self._data
      
      def get_row(self):
            return self._row
      def get_col(self):
            return self._col

      
class Sudoku():
      def __init__(self):
            self._Board = []
            for row in range(1,10):
                  for col in range(1,10):
                        self._Board.append(Cell(row,col))
      def initialise(self):
            self._Board = []
            for row in range(1,10):
                  for col in range(1,10):
                        self._Board.append(Cell(row,col))
                        
      def print(self):
            print('\n'*3)
            counter = 1
            while counter != 10:
                  print(counter,end=' ')
                  counter += 1
            counter = 1
            count = 1
            print('\n')
            for i in self._Board:
                  print(i.get_data(),end=' ')
                  count += 1
                  if count == 10:
                        count = 1
                        print('  ' + str(counter))
                        counter += 1
      
      def sub(self,data):
            import math
            data = math.ceil(data/3)
            if data == 3:
                  return [7,8,9]
            elif data == 2:
                  return [4,5,6]
            else:
                  return [1,2,3]

      def validity(self,row,col,data):
            subrow = self.sub(row)
            subcol = self.sub(col)
            subgrid = []
            column = []
            rowrow = []
            for i in self._Board:
                  #print(data,i.get_data(),row,i.get_row(),col,i.get_col())
                  if i.get_col() == col:
                        column.append(i.get_data())
                        if i.get_row() == row:
                              mark = i
                              if mark.get_data() != 0:
                                    return mark
                  if i.get_row() == row:
                        rowrow.append(i.get_data())
                  if i.get_col() in subcol:
                        if i.get_row() in subrow:
                              subgrid.append(i.get_data())
                  if data in subgrid or data in rowrow or data in column:
                        return None
            return mark
      
      def insert(self,row,col,data):
            check = self.validity(row,col,data)
            if not check == None and check.get_data() == 0:
                  #print(row,col,mark.get_row(),mark.get_col())
                  check.set_data(data)
                  
      def modify(self,row,col,data):
            check = self.validity()
            if not check == None:
                  #print(row,col,mark.get_row(),mark.get_col())
                  check.set_data(data)
                  
      def delete(self,row,col):
            check = self.validity()
            if not check == None:
                  #print(row,col,mark.get_row(),mark.get_col())
                  check.set_data(0)
            
      def check_full(self):
            for i in self._Board:
                  if i.get_data() == 0:
                        return None
            return True

      def check_none(self):
            count = 0
            for i in self._Board:
                  if i.get_data() == 0:
                        count += 1
            return count



##############    SUDOKU STARTER ############################

def try_solve():  
      x = Sudoku()
      x.print()
      from random import randint as ri
      count = 1
      tried = 1
      ones = 0
      twos = 0
      threes = 0
      fours = 0
      while x.check_full() != True:
            #x.insert(ri(1,9),ri(1,9),ri(1,9))
            for i in range(5):
                  for row in range(1,10):
                        row += ri(1,9)
                        if row > 9:
                              row -= 9
                        #print("row:           "+str(row))
                        #x.print()
                        for col in range(1,10):
                              col += ri(1,9)
                              if col > 9:
                                    col -= 9
                              #print(x.check_none())
                              for data in range(1,10):
                                    x.insert(row,col,data)
                                    
                              #x.insert(row,col,ri(1,9))

            nones = x.check_none()         
            if nones != None and nones < 5:
                  x.print()
                  if nones == 1:
                        ones += 1
                  elif nones == 2:
                        twos += 1
                  elif nones == 3:
                        threes += 1
                  elif nones == 4:
                        fours += 1
                        
                  print('\nblanks:'+str(nones)+'\ntries:'+str(tried)+' ')
                  print('ones:'+str(ones)+'  twos:'+str(twos)+'  threes:'+str(threes)+'  fours:'+str(fours)+'\n')
            
            else:
                  #print(x.check_none())
                  pass
            tried += 1
            x.initialise()
                        #x.print()
      ##                  
      ##                  count += 1
      ##                  if count % 10000 == 0:
      ##                        print('\n'*4)
      ##                        x.print()
      ##                        x.check_none()

            
      x.print()
