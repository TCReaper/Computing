
def linear_search(L,n):
      for i in L:
            if i == n:
                  return L.index(i)
      return -1

def binary_search(L,n):
      mid = len(L)//2
      index = mid
      while True:
            if L[mid] == n:
                  return index
            if L[mid] > n:
                  mid = mid//2
                  index += mid
                  L = L[mid//2:]
            else:
                  mid = mid//2
      return -1

######################################################

L = [9,1,2,3,4,5,6]

def bubble(L,ascend=True):
      for i in range(1,len(L)):
            for e in range(i-1):
                  if ascend==True:
                        if L[i] < L[e]:
                              L[i],L[e] = L[e],L[i]
                  else:
                        if L[i] > L[e]:
                              L[i],L[e] = L[e],L[i]

      return(L)

def insertion(L,ascend=True):
      for i in range(len(L)-1):
            if ascend == True:
                  while L[i] > L[i+1]:
                        L[i],L[i+1]=L[i+1],L[i]
                        i+=1
            else:
                  while L[i] < L[i+1]:
                        L[i],L[i+1]=L[i+1],L[i]
                        i+=1

def quicksort(L,ascend=True):
      return qshelper(L)
def qshelper(L):
      pivot = L[len(L)//2]
      
######################################################

class SLL():
      def __init__(self):
            self._root = None
      def insert_back(self,data):
            if self._root == None:
                  self._root == Node(data)
            else:
                  cur = self._root
                  while cur.get_next() != None:
                        cur = cur.get_next()
                  cur.set_next = Node(data)
      def insert_front(self,data):
            if self._root == None:
                  self._root == Node(data)
            else:
                  temp = self._root
                  self._root = Node(data)
                  self._root.set_next(temp)
      def exists(self,data):
            cur = self._root
            while cur.get_next() != None:
                  if cur.get_data == data:
                        return True
                  cur = cur.get_next()
            return False

      def delete(self,data):
            if not exists(data):
                  return False
            else:
                  prev = None
                  cur = self._root
                  while cur.get_data() != data and cur.get_next() != None:
                        prev = cur
                        cur = cur.get_next()
                  if cur.get_data() == data:
                        if prev==None:
                              self._root = cur.get_next()
                        else:
                              prev.set_next(cur.get_next())
                        return True
                  return False
            
      def __str__(self,data):
            return str(data)

                        
            
class NodeSLL():
      def __init__(self,data):
            self._data = data
            self._next = None
      def set_next(self,n_next):
            self._next = n_next
      def get_next(self):
            return self._next
      def set_data(self,n_data):
            self._data = n_data
      def get_data(self):
            return self._data


class NodeDLL():
      def __init__(self,data):
            self._data = data
            self._next = None
            self._prev = None
      def set_next(self,n_next):
            self._next = n_next
      def get_next(self):
            return self._next
      def set_prev(self,n_prev):
            self._prev = n_prev
      def get_prev(self):
            return self._prev
      def set_data(self,n_data):
            self._data = n_data
      def get_data(self):
            return self._data

class CDLL():
      def __init__(self):
            self._root = None
      def insert_back(self,data):
            if self._root == None:
                  self._root == Node(data)
            else:
                  temp_prev = self._root.get_prev()
                  temp_prev.set_next(Node(data))
                  temp_prev.get_next().set_prev(temp_prev)
                  temp_prev.get_next().set_next(self._root)
                  self._root.set_prev(temp_prev.get_next())
                  
      def insert_front(self,data):
            if self._root == None:
                  self._root == Node(data)
            else:
                  temp = self._root
                  temp_prev = temp.get_prev()
                  self._root = Node(data)
                  temp.set_prev(self._root)
                  self._root.set_prev(temp_prev)
                  self._root.set_next(temp)
      
      def exists(self,data):
            cur = self._root
            while cur.get_next() != None:
                  if cur.get_data == data:
                        return True
                  cur = cur.get_next()
            return False

      def delete(self,data):
            if not exists(data):
                  return False
            else:
                  prev = None
                  cur = self._root
                  while cur.get_data() != data and cur.get_next() != None:
                        prev = cur
                        cur = cur.get_next()
                  if cur.get_data() == data:
                        if prev==None:
                              self._root = cur.get_next()
                        else:
                              prev.set_next(cur.get_next())
                        return True
                  return False


class DLL(CDLL):
      def __super__():
            __init__()
            
      def insert_back(self,data):
            if self._root == None:
                  self._root == Node(data)
            else:
                  cur = self._root
                  while cur.get_next() != None:
                        cur = cur.get_next()
                  cur.set_next = Node(data)
                  
      def insert_front(self,data):
            if self._root == None:
                  self._root == Node(data)
            else:
                  temp = self._root
                  temp_prev = temp.get_prev()
                  self._root = Node(data)
                  temp.set_prev(self._root)
                  self._root.set_prev(temp_prev)
                  self._root.set_next(temp)
                  

      def delete(self,data):
            if not exists(data):
                  return False
            if not exists(data):
                  return False
            else:
                  cur = self._root
                  while cur.get_data() != data and cur.get_next() != None:
                        cur = cur.get_next()
                  if cur.get_data() == data:
                        if self._root == cur:
                              self._root = cur.get_next()
                        else:
                              prev.set_next(cur.get_next())
                        return True
                  return False

######################################################


class Bode():
      def __init__(self,data):
            self._data = data
            self._left = None
            self._right = None
      def get_data(self):
            return self._data
      def set_left(self,left):
            self._left = left
      def get_left(self):
            return self._left
      def set_right(self,right):
            self._right = right
      def get_right(self):
            return self._right

class BST():
      def __init__(self):
            self._root = None
      def insert(self,data):
            if self._root == None:
                  self._root = Bode(data)
            else:
                  cur = self._root
                  while True:
                        if data < cur.get_data():
                              if cur.get_left() == None:
                                    cur.set_left(Bode(data))
                                    break
                              else:
                                    cur = cur.get_left()
                        else:
                              if cur.get_right() == None:
                                    cur.set_right(Bode(data))
                                    break
                              else:
                                    cur = cur.get_right()

      def exists(self,data):
            cur = self._root
            if cur == None:
                  return False
            else:
                  while True:
                        if data == cur.get_data():
                              return True
                        if data < cur.get_data():
                              if cur.get_left() == None:
                                    return False
                              else:
                                    cur = cur.get_left()
                        else:
                              if cur.get_right() == None:
                                    return False
                              else:
                                    cur = cur.get_right()

      def __str__(self):
            return str(helpmepls)

      def helpmepls(self):
            pass
            

######################################################

class HashTable():
      def __init__(self,size):
            self._size = size
            self._data = [None for i in range(size)]
      def insert(self,data):
            L = self._data
            hasher = hash(data) % self._size
            index = hasher
            while True:
                  if L[index] == None:
                        L[index] = data
                  else:
                        index += hasher
                        if index > self._size:
                              index -= self._size
                        
      def exists(self,data):
            L = self._data
            index = 0
            while True:
                  if L[index] == data:
                        return True
                  else:
                        index += 1
                        if index > self._size:
                              return False
      def delete(self,data):
            L = self._data
            index = 0
            if exists(data) == False:
                  return False
            else:
                  pass
























































            
            
