

class BST():
      def __init__(self):
            self._root = None

      def insert(self,data):
            if self._root == None:
                  self._root == Node(data)
            else:
                  current_node = self._root
                  while True:
                        if data < current_node.data():
                              if current_node._left == None:
                                    current_node.set_left( Node(data) ) 
                                    break
                              else:
                                    current_node = current_node._left
                        else:
                              if current_node._right == None:
                                    current_node.set_right( Node(data) )
                                    break
                              else:
                                    current_node = current_node.right
                                    
      def in_order(self, tree):
            if tree == None:
                  pass
            else:
                  self.in_order(tree.left())
                  print(tree.data())
                  self.in_order(tree.right())


class Node():
      def __init__(self,data):
            self._data = data
            self._left = None
            self._right = None
      def data(self):
            return self._data
      def left(self):
            return self._left._data
      def right(self):
            return self._right._data
      def set_left(self,new_node):
            self._left = new_node
      def set_right(self,new_node):
            self._right = new_node


tree = BST
print("tree is the BST ",tree)
