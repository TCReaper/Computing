class BST():
      def __init__(self):
            self._array = [None for i in range(100)]
      def insert(self,data):
            if self._array[0] == None:
                  self._array[0] = data
            else:
                  cur_index = 0
                  while True:
                        #print(cur_index)
                        if data < self._array[cur_index]:
                              cur_index = 2*cur_index + 1
                              if self._array[cur_index] == None:
                                    self._array[cur_index] = data
                                    break
                              else:
                                    pass
                        else:
                              cur_index = 2*cur_index + 2
                              if self._array[cur_index] == None:
                                    self._array[cur_index] = data
                                    break
                              else:
                                    pass
                              
      def find(self,data):
            if self._array[0] == None:
                  return False
            else:
                  cur_index = 0
                  while True:
                        if data == self._array[cur_index]:
                              return True
                        if data < self._array[cur_index]:
                              cur_index = 2*cur_index + 1
                              if self._array[cur_index] == None:
                                    return None
                        else:
                              cur_index = 2*cur_index + 2
                              if self._array[cur_index] == None:
                                    return None
                        

      def print(self):
            for i in self._array:
                  if i != None:
                        print(i)
            
tree = BST()
import random
for i in range(15):
      tree.insert(random.randint(1,50))
tree.print()
