
class BSTNode():
      def __init__(self,data):
            self._data = data
            self._left = None
            self._right = None
            self._tombstone = False
            
      def get_data(self):
            return self._data
      def set_data(self,data):
            self._data = data
      def get_right(self):
            return self._right
      def set_right(self,right):
            self._right = right
      def get_left(self):
            return self._left
      def set_left(self,left):
            self._left = left
      def get_tomb(self):
            return self._tombstone
      def set_tomb(self,boolean=True):
            self._tombstone = boolean

      def inorder(self):
            pass

class LLNode(BSTNode):
      def __super__(data):
            __init__(data)
            self._prev = None
            self._next = None
      def get_prev(self):
            return self._prev
      def get_next(self):
            return self._next
      def set_prev(self,data):
            self._prev = data
      def set_next(self,data):
            self._next

class LL():
      def __init__(self):
            self._first = None
      def get_first(self):
            return self._first
      def set_first(self,first):
            self._first = first
      def insert(self,data):
            if self.get_first()== None:
                  self.set_first(LLNode(data))
            else:
                  node = LLNode(data)
                  cur = get_first()
                  while cur.get_next() != None:
                        cur = cur.get_next()
                  cur.set_next(node)
                  node.set_prev(cur)
                  
class BST():
      def __init__(self):
            self._root = None
      def get_root(self):
            return self._root
      def set_root(self,root):
            self._root = root
      def insert(self,data):
            if self.get_root() == None:
                  self.set_root(BSTNode(data))
            else:
                  cur = self.get_root()
                  while True:
                        if data < cur.get_data():
                              if cur.get_left() == None:
                                    cur.set_left( BSTNode(data) ) 
                                    break
                              else:
                                    cur = cur._left
                        else:
                              if cur.get_right() == None:
                                    cur.set_right( BSTNode(data) )
                                    break
                              else:
                                    cur = cur.right
      


class Hybrid():
      def __init__(self,rate_sorted):
            self._unsorted = LL()
            self._sorted = BST()
            self._rate_sorted = rate_sorted
      def insert(self,data):
            pass
      def exists(self,data):
            pass
      def delete(self,data):
            if not self.exists(data):
                  return YOU SUCK!
            else:
                  pass













                                    
                  
            
