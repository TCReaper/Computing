

def insert(self,data):
      if self._root == None:
            self._root == Node(data)
      else:
            current_node = self._root
            while True:
                  if data < current_node.data():
                        if current_node.left() == None:
                              current_node.set_left( Node(data) ) 
                              break
                        else:
                              current_node = current_node.left()
                  else:
                        if current_node.right() == None:
                              current_node.set_right( Node(data) )
                              break
                        else:
                              current_node = current_node.right()
