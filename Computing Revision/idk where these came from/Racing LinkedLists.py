

class Node():
      def __init__(self,name = None,time = None):
            self._name = name
            self._time = time
            self._next = None
      def set_name(self,new_name):
            self._name = new_name
      def set_time(self,new_time):
            self._time = new_time
      
      

class LinkedList():
      def __init__(self):
            self._first = None
            
      def Display(self):
            current_node = self._first
            while current_node != None:
                  print(current_node._name,current_node._time)
                  current_node = current_node._next
            
      def AddFirst(self,node=Node()):
            new_node = node
            if self._first == None:
                  self._first = new_node
            else:
                  current_node = self._first
                  self._first = new_node
                  self._first._next = current_node
                  
      def RemoveFirst(self):
            current_node = self._first
            new_node = current_node._next
            current_node = new_node

      def AddLast(self):
            if self._first == None:
                  self.AddFirst(Node())
            else:
                  current_node = self._first
                  while not current_node._next == None:
                        current_node = current_node._next
                  current_node._next = Node()

      def RemoveLast(self):
            current_node = self._first
            while not current_node._next == None:
                  prev_node = current_node
                  current_node = current_node._next
            prev_node._next = None

      def Empty(self):
            if self._first == None:
                  return True
            return False

      def AddOrdered(self,node):
            inserted_node = node
            time = node._time
            name = node._name
            cur = self._first
            
            if cur == None:
                  self.AddFirst(node)
                  cur = self._first
                  return 0
            
            if cur._time > time:
                  push = cur
                  self._first = node
                  self._first._next = push
                  return 0
                  
            while cur._next != None and cur._next._time < time:
                  cur = cur._next
            pushed = cur._next
            cur._next = node
            cur._next._next = pushed



def RemoveNode(name):
      FreeList.AddLast()
      
      

                              
                        
                 


           

def AddInOrder(name,time):
      if FreeList.Empty() == True:
            print('You may not pass!')
            return None
      node = Node(name,time)
      FreeList.RemoveFirst()
      RaceList.AddOrdered(node)
      
            




RaceList = LinkedList()
FreeList = LinkedList()

for i in range(20):
      FreeList.AddFirst()




AddInOrder('rahul',5)
AddInOrder('sheem',7)
AddInOrder('haosh',6)
AddInOrder('adler',3)
AddInOrder('feesh',1)
RaceList.Display()










