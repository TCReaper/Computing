#3.1
class Node():
    def __init__(self, data):
        self._data = data
        self._leftPtr = None
        self._rightPtr = None

    def get_data(self):
        return self._data

    def set_data(self, newData):
        self._data = newData

    def get_left(self):
        return self._leftPtr

    def set_left(self, newLeft):
        self._leftPtr = newLeft

    def get_right(self):
        return self._rightPtr

    def set_right(self, newRight):
        self._rightPtr = newRight

class Tree():
    def __init__(self):
        self._root = -1
        self._tree = []

    def add(self, data):
        if self._tree == []:
            self._tree.append(Node(data))
        else:
            current = self._root + 1
            added = False
            while not added:
                if data > self._tree[current].get_data():
                    if self._tree[current].get_right() != None:
                        current = self._tree[current].get_right()
                    else:
                        newright = len(self._tree)
                        self._tree.append(Node(data))
                        self._tree[current].set_right(newright)
                        added = True
                else:
                    if self._tree[self._tree[current].get_left()] != None:
                        current = self._tree[current].get_left()
                    else:
                        newleft = len(self._tree)
                        self._tree.append(Node(data))
                        self._tree[current].set_left(newleft)
                        added = True

    def print(self):
        for i in self._tree:
            print('Data: ' + str(i.get_data()))
            print('Left pointer: ' + str(i.get_left()))
            print('Right pointer: ' + str(i.get_right()))

    def inOrderTraversal(self):
        if self._tree == []:
            print('Tree empty')
        else:
            self._inOrderTraversal(self._root + 1)

    def _inOrderTraversal(self, tree):
        if self._tree[tree].get_left() != None:
            self._inOrderTraversal(self._tree[tree].get_left())
        print(self._tree[tree].get_data())
        if self._tree[tree].get_right() != None:
            self._inOrderTraversal(self._tree[tree].get_right())
                    
                    

#3.2          
a = Tree()
a.add('abc')
a.add('nnd')
a.add('zzz')
a.print()
a.inOrderTraversal()
