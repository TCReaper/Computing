
class node():
        def __init__(self,data):
                self._data = data
                self._next = None
        def get_data(self):
                return self._data
        def get_next(self):
                return self._next
        def set_data(self,new_data):
                self._data = new_data
        def set_next(self,new_next):
                self._next = new_next

class linkedlist():
        def __init__(self):
                self._root = None
        def insert(self,data):
                if self._root == None:
                        self._root = node(data)
                else:
                        current_node = self._next
                        while current_node.get_next() != None:
                                current_node = current_node.get_next()
                        current_node.set_node(node(data))

                        
