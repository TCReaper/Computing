

def check_isbn(number):
      try:
            int(number[:-1])
      except ValueError:
            print('Only numbers are allowed')
            return False
      if len(number)==10:
            if str(number[-1]) == check_10(number):
                  return True
            else:
                  return False
      elif len(number)==13:
            if number[-1] == check_13(number):
                  return True
            else:
                  return False
      else:
            print('Incorrect length')
            return False

def check_10(number):
      s = 0
      for i in range(9):
            s += int(number[i]) * (10-i)
      s = 11 - s%11
      if s == 10:
            s = 'X'
      return str(s)

def check_13(number):
      flip = True
      s = 0
      for i in range(12):
            if flip == True:
                  s += int(number[i]) * 1
                  flip = False
            else:
                  s += int(number[i]) * 3
                  flip = True
      s = (10 - s%10)%10   
      return s

import random

def gen_isbn10(n):
      for i in range(n):
            isbn = ''
            isbn += str(random.randint(0,999999999))
            while len(isbn) < 9:
                  isbn = '0' + isbn
            isbn += check_10(isbn)
            print(isbn)
            
def gen_isbn13(n):
      for i in range(n):
            isbn = '978' + str(random.randint(0,999999999))
            while len(isbn) < 12:
                  isbn = '0' + isbn
            isbn += str(check_13(isbn))
            print(isbn)

#     #     #     #     #     #     #     #     #     #     #     #

class CDLL():
      def __init__(self):
            self._root = None
            
      def insert_front(self,data):
            if self._root == None:
                  self._root = Node(data)
                  self._root.set_next(self._root)
                  self._root.set_prev(self._root)
            else:
                  temp = self._root
                  self._root = Node(data)
                  self._root.set_next(temp)
                  temp.set_prev(self._root)
                  
                  
      def insert_back(self,data):
            if self._root == None:
                  self._root = Node(data)
                  self._root.set_next(self._root)
                  self._root.set_prev(self._root)
            else:
                  temp = self._root
                  self._root = Node(data)
                  self._root.set_prev(temp)
                  temp.set_next(self._root)
                  
      def find(self,data):
            if self._root.get_data() == data:
                  return True
            else:
                  end = self._root
                  current = self._root.get_next()
                  while current != end:
                        if current.get_data() == data:
                              return True
                        else:
                              current = current.get_next()
                  return False
            
      def delete(self,data):
            if find(data) == True:
                  end = self._root
                  current = self._root.get_next()
                  while current != end:
                        if current.get_data() == data:
                              next_node = current.get_next()
                              prev_node = current.get_prev()
                              next_node.set_prev(prev_node)
                              prev_node.set_next(next_node)
                              return True
                        else:
                              current = current.get_next()
            return False
                  
      def print(self):
            end = self._root
            current = self._root.get_next()
            print(end.get_data())
            while current != end:
                  print(current.get_data())
                  current = current.get_next()

class Node():
      def __init__(self,data):
            self._data = data
            self._next = None
            self._prev = None
            
      def get_data(self):
            return self._data
      
      def set_next(self,data):
            self._next = data
      def set_prev(self,data):
            self._prev = data
            
      def get_next(self):
            return self._next
      def get_prev(self):
            return self._prev


#     #     #     #     #     #     #     #     #     #     #     #

class Hash():
      def __init__(self, tablesize=5):
            self._table = [None for i in range(tablesize)]
            self._size = tablesize

      def insert(self,data):
            index = hash(data) % self._size
            if self._table[index] == None:
                  self._table[index] = CDLL()
            self._table[index].insert_front(data)

      def find(self,data):
            index = hash(data) % self._size
            if self._table[index] == None:
                  return False
            else:
                  return self._table[index].find(data)

      def delete(self,data):
            if self.find(data) == True:
                  index = hash(data) % self._size
                  self._table[index].delete(data)
                  return True
            return False

      def print(self):
            for i in self._table:
                  if i == None:
                        print('-')
                  else:
                        i.print()


#     #     #     #     #     #     #     #     #     #     #     #

menu = True
h = Hash()
while menu:
      isbn = input('Input an ISBN number: ')
      if check_isbn(isbn) == True:
            h.insert(isbn)
      else:
            print('Unacceptable ISBN number')
      
