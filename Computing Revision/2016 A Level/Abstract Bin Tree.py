

            
class Node():
      def __init__(self,data):
            self._data = data
            self._leftPtr = None
            self._rightPtr = None
      def setData(self,s):
            self._data = s
      def setLeftPtr(self,x):
            self._leftPtr = x
      def setRightPtr(self,y):
            self._rightPtr = y
      def getData(self):
            return self._data
      def getLeftPtr(self):
            return self.leftPtr
      def getRightPtr(self):
            return self.rightPtr


      
class Tree():
      def __init__(self):
            self._tree = []#array of node
            self._root = -1
      def add(self,newItem):
            if self._root == -1:
                  self._tree.append(Node(newItem))
                  self._root = 0
            else:
                  cur_node = self._tree[self._root]
                  not_input = True
                  while not_input:
                        cur_data = ord(cur_node.getData()[0])
                        if cur_data >= ord(newItem[0]):
                              if cur_node._rightPtr == None:
                                    cur_node._rightPtr = len(self._tree)
                                    self._tree.append(Node(newItem))
                                    not_input = False
                              else:
                                    cur_node = self._tree[cur_node._rightPtr]
                        else:
                              if cur_node._leftPtr == None:
                                    cur_node._leftPtr = len(self._tree)
                                    self._tree.append(Node(newItem))
                                    not_input = False
                              else:
                                    cur_node = self._tree[cur_node._leftPtr]

                  
      def print(self):
            for i in self._tree:
                  print(i.getData())
                  
      def iOT(self,mid):
            if mid._rightPtr != None:
                  self.iOT(self._tree[mid._rightPtr])
            print(mid._data)
            if mid._leftPtr != None:
                  self.iOT(self._tree[mid._leftPtr])
                  
      def inOrderTraversal(self):
            mid = self._tree[self._root] #mid is a Node()
            self.iOT(mid)
            
      
            
      


x = Tree()
x.add('Dave')
x.add('Fred')
x.add('Ed')
x.add('Greg')
x.add('Bob')
x.add('Cid')
x.add('Ali')
x.print()
