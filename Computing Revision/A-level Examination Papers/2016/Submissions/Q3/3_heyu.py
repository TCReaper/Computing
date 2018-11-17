class Node:
    def __init__(self, data):
        self._data = data
        self._leftPtr = -1
        self._rightPtr = -1

    def get_data(self):
        return self._data

    def get_leftPtr(self):
        return self._leftPtr

    def get_rightPtr(self):
        return self._rightPtr

    def set_data(self, data):
        self._data = data

    def set_leftPtr(self, left):
        self._leftPtr = left

    def set_rightPtr(self, right):
        self._rightPtr = right

class Tree:
    def __init__(self):
        self._root = -1
        self._tree = []

    def add(self, newData):
        newNode = Node(newData)
        self._tree.append(newNode)
        if self._root == -1:
            self._root = 0
        else:
            i = self._root
            added = False
            while not added:
                if newData < self._tree[i].get_data():
                    if self._tree[i].get_leftPtr() == -1:
                        self._tree[i].set_leftPtr(len(self._tree)-1)
                        added = True
                    else:
                        i = self._tree[i].get_leftPtr()
                else:
                    if self._tree[i].get_rightPtr() == -1:
                        self._tree[i].set_rightPtr(len(self._tree)-1)
                        added = True
                    else:
                        i = self._tree[i].get_rightPtr()

    def print(self):
        print("{:<10}{:<10}{:<10}".format("Data item","Left Ptr","Right Ptr"))
        for i in range(len(self._tree)):
              print("{:<10}{:<10}{:<10}".format(self._tree[i].get_data(), \
                                                self._tree[i].get_leftPtr(), \
                                                self._tree[i].get_rightPtr()))
    def inOrderHelper(self,i):
        if self._tree[i].get_leftPtr() != -1:
            self.inOrderHelper(self._tree[i].get_leftPtr())
        print(self._tree[i].get_data())
        if self._tree[i].get_rightPtr() != -1:
            self.inOrderHelper(self._tree[i].get_rightPtr())


    def inOrderTraversal(self):
        if self._root != -1:
            self.inOrderHelper(self._root)


myTree = Tree()
myTree.add("Dave")
myTree.add("Bob")
myTree.add("Ali")
myTree.add("Cid")
myTree.add("Fred")
myTree.add("Ed")
myTree.add("Greg")
myTree.print()
myTree.inOrderTraversal()
                    
