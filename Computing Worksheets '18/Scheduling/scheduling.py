
from random import *

def gen_process():
      proc_id = 1001
      f = open('PROCESSES.TXT','w')
      for i in range(30):
            arrival = randint(0,250)
            execution = randint(10,30)
            f.write(str(proc_id+i)+','+str(arrival)+','+str(execution)+'\n')
            
      f.close()

      
def read_process():
      gen_process()
      f = open('PROCESSES.TXT')
      processes = []
      for line in f:
            line = line.strip().split(',')
            processes.append(line)
      f.close()
      processes = quicksort(processes)
      print(processes)

def quicksort(arr):
      if len(arr) <= 1:
            return arr
      else:
            return quicksort([x for x in arr[1:] if int(x[1])<int(arr[0][1])]) + [arr[0]] + quicksort([x for x in arr[1:] if int(x[1])>= int(arr[0][1])])

#read_process()

class Process():
      def __init__(self,proc_array):
            self._id = proc_array[0]
            self._arrival = proc_array[1]
            self._execute = proc_array[2]

      def set_id(self,data):
            self._id = data
      def set_arr(self,data):
            self._arrival = data
      def set_execute(self,data):
            self._execute = data

      
      def get_id(self):
            return self._id
      def get_arr(self):
            return self._arrival
      def get_exec(self):
            return self._execute

      
class Node():
      def __init__(self,proc_array):
            self._data = Process(proc_array)
            self._next = None
            
      def set_data(self,data):
            self._data = data
      def get_data(self):
            return self._data
      
      def set_next(self,node):
            self._next = node
      def get_next(self):
            return self._next
      
class SLL():
      def __init__(self):
            self._root = None
      def insert(self,array):
            if self._root == None:
                  self._root = Node(array)
            elif self._root.get_next() == None:
                  self._root.get_next().set_next(Node(array))
            else:
                  current = self._root
                  while current.get_next() != None:
                        current = current.get_next()
                  current.set_next(Node(array))
      def find(self,array):
            if self._root == None:
                  return False
            else:
                  current = self._root
                  while current.get_next() != None:
                        if current.get_data():
                              pass

class PriorityQueue(SLL):
      def __init__(self):
            super().__init__()
            
                        
            








      

