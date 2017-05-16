

def get_parent(self,data):
      if self._root == None:
            return None
      else:
            current_node = self._root
            iterating = True
            while iterating:
                  if current_node == None:
                        return None
                  if data < current_node.data():
                        if data == current_node.left().data():
                              return current_node
                        else:
                              current_node = current_node.left()
                  else:
                        if data == current_node.right().data():
                              return current_node
                        else:
                              current_node = current_node.right()

def find_node(self,data):
      parent = self.get_parent(data)
      if parent == None:
            return None
      else:
            if data < parent.data():
                  return parent.left()
            else:
                  return parent.right()
