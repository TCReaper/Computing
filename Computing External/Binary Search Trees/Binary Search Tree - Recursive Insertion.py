

def insert(self,data):
      if self._root == None:
            self._root = Node(data)
      else:
            self.insert_recursive(data,self._root)

def insert_recursive(self,data,current_root):
      if data < current_root.data():
            if current_root.left() == None:
                  current_root.set_left( Node(data) )
            else:
                  self.insert_recursive( data, current_root.left() )
      else:
            if current_root.right() == None:
                  current_root.set_right( Node(data) )
            else:
                  self.insert_recursive( data, current_root.right() )
