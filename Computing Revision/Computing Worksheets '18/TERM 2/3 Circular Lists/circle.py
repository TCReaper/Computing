


class Circle():
      def __init__(self,size):
            self._root = None
            self._size = 0
            self._maxsize = size
            
      def insert(self,element):
            if self._root == None:
                  self._root = Node(element)
                  self._root.set_rear(True)
                  self._root.set_next(self._root)
                  self._size = 1
            elif self._size == self._maxsize:
                  print('Queue is maxed out bro')
            else:
                  current = self._root
                  while True:
                        if current.get_rear():
                              current.set_next(Node(element))
                              current.set_rear(False)
                              nextnode = current.get_next()
                              nextnode.set_rear(True)
                              nextnode.set_next(self._root)
                              self._size += 1
                              break
                        else:
                              current = current.get_next()

      def delet(self):
            root = self._root
            if root.get_rear():
                  self._root = None
            else:
                  current = root
                  while not current.get_rear():
                        current = current.get_next()
                  current.set_next(root.get_next())
                  self._root = root.get_next()
            
      def print(self):
            count = 2
            current = self._root
            print('{0:3}{1:^8}{2:5}{3:5}'.format('|',current.get_data(),'|','<- Front pointer'))
            current = current.get_next()   
            while not current.get_rear():
                  prev = current
                  current = current.get_next()    
                  print('{0:3}{1:^8}{2:5}'.format('|',prev.get_data(),'|'))
                  count += 1
            print('{0:3}{1:^8}{2:5}{3:5}'.format('|',current.get_data(),'|','<- Back pointer'))
            while count < self._maxsize:
                  print('{0:3}{1:^8}{2:5}'.format('|','','|'))
                  count += 1
            

                  
class Node():
      def __init__(self,data):
            self._data = data
            self._next = None
            self._rear = False
            
      def set_next(self,node):
            self._next = node
      def set_rear(self,boolean):
            self._rear = boolean
            
      def get_next(self):
            return self._next
      def get_data(self):
            return self._data
      def get_rear(self):
            return self._rear


def setup_queue(n):
      return Circle(n)
def enqueue(element):   
      pass
def dequeue(element):
      pass



x = Circle(5)
x.insert('Hello')
x.insert('My')
x.insert('Name')
x.insert('Joe')

x.print()



















      
