#sudoku 3

class Cell():
      def __init__(self):
            self._value = 0
      def get_value(self):
            return self._value
      def set_value(self,value):
            self._value = value

class Section():
      def __init__(self):
            self._cells = []

      def get_cells(self):
            return self._cells
      
      def is_legal(self):
            elements = []
            valid = True
            for cell in self._cells:
                  value = cell.get_value()
                  for i in elements:
                        if i == value:
                              valid = False
                              break
                        else:
                              elements.append(value)
                              print(elements)
            return valid

class Grid_Manager():
      def __init__(self):
            self._grid = [Cell() for i in range(81)]
            self._columns = [Section() for i in range(9)]
            self._rows = [Section() for i in range(9)]
            self._subgrids = [Section() for i in range(9)]

            for e in range(9):
                  col = []
                  for index in range(9):
                        col.append(self._grid[(9*index) + e])
                  #col is filled
                  self._columns[e]._cells = col

            for e in range(9):
                  self._rows[e]._cells = self._grid[(e)*9:(e+1)*9]
                  
            for rows in range(3):
                  for cols in range(3):
                        sub = []
                        for group in range(3):
                              sub += self._grid[(cols*3)+(rows*27)+(group*9):(cols*3+3)+(rows*27)+(group*9)]
                        self._subgrids[rows*3 + cols]._cells = sub
                        
      
      def get_cell(self,row,col):
            pass

      def set_cell(self,row,col,data):
            cell = self._grid[(row-1)*9 + col-1]
            cell.set_value(data)
            self.print_grid()
            
      def print_grid(self):
            print('\n'*2)
            counter = 1
            while counter != 10:
                  print(counter,end=' ')
                  counter += 1
            counter = 1
            count = 1
            print('\n')
            for i in self._grid:
                  print(i.get_value(),end=' ')
                  count += 1
                  if count == 10:
                        count = 1
                        print('  ' + str(counter))
                        counter += 1
                        
      def print_columns(self):
            count = 1
            for col in self._columns:
                  col = col.get_cells()
                  for element in col:
                        print(str(element.get_value()),end=' ')
                  print('  '+str(count))
                  count += 1
                  
      def print_rows(self):
            count = 1
            for row in self._rows:
                  row = row.get_cells()
                  for element in row:
                        print(str(element.get_value()),end=' ')
                  print('  '+str(count))
                  count += 1
                  
                        
      def is_legal(self):
            legal = True
      
            for i in self._columns:
                  if i.is_legal() == False:
                        legal = False
                        break
            for i in self._rows:
                  if i.is_legal() == False:
                        legal = False
                        break
            for i in self._subgrids:
                  if i.is_legal() == False:
                        legal = False
                        break
           
            if legal == True:
                  return True
            else:
                  return False
            
x = Grid_Manager()
x.print_grid()
