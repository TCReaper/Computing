

class HashTable():
      def __init__(self,size):
            self._array = [Hybrid()] * size
      def insertion(self,data):
            index = hash(data) % 5
            self._array[index].insert(data)

class Hybrid():
      def __init__(self):
            self._bst = BST()
            self._stack = Hash()
      def insert(self,data):
            self._stack.insert( self._bst.insert(data) )
            



class BST():
      def __init__(self):
            self._root = None
      def insert(self,data):
            if self._root == None:
                  self._root = Bode(data)
            else:
                  cur = self._root
                  while True:
                        if data < cur.data():
                              if cur.get_tomb():
                                    cur = cur.get_left()
                              elif cur.get_left() == None:
                                    cur.set_left( NBode(data) ) 
                                    return cur.get_left()
                              else:
                                    cur = cur.get_left()
                        else:
                              if cur.get_tomb():
                                    cur = cur.get_right()
                              elif cur.get_right() == None:
                                    cur.set_right( Bode(data) )
                                    return cur.get_right()
                              else:
                                    cur = cur.get_right()
                              
class Bode():
      def __init__(self,data):
            self._data = data
            self._left = None
            self._right = None
            self._tomb = False
      def get_tomb(self):
            return self._tomb
      def get_data(self):
            return self._data
      def get_left(self):
            return self._left
      def get_right(self):
            return seld._right
      def set_left(self,node):
            self._left = node
      def set_right(self,node):
            self._right = node
      def delete(self):
            self._tomb = True

class Stack():
      def __init__(self):
            self._root = None
      def insert(self,node):
            if self._root == None:
                  self._root = DLLode(node)
            else:
                  cur = self._root
                  while True:
                        if cur.get_next() == None:
                              cur.set_next(DLLode(node))
                        else:
                              cur = cur.get_next()
                        

      

class DLLode():
      def __init__(self,node):
            self._node = node
            self._next = None
            self._prev = None
      def get_node(self):
            return self._node
      def get_next(self):
            return self._next
      def get_prev(self):
            return self._prev
      def set_next(self,node):
            self._next = node
      def set_prev(self,node):
            self._prev = node
            



















            
