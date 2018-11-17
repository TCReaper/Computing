class Node():
    def __init__(self, data, leftPtr = -1, rightPtr = -1):
        self._data = data
        self._leftPtr = leftPtr
        self._rightPtr = rightPtr

    def setData(self, s):
        self._data = s

    def setLeftPtr(self, x):
        self._leftPtr = x

    def setRightPtr(self, y):
        self._rightPtr = y

    def getData(self):
        return self._data

    def getLeftPtr(self):
        return self._leftPtr

    def getRightPtr(self):
        return self._rightPtr


class Tree():
    def __init__(self):
        self._root = -1
        self._tree = []

    def add(self, newItem):
        if self._root == -1:
            self._tree.append(Node(newItem))
            self._root = 0
        else:
            current = self._root
            while current != -1:
                if self._tree[current].getData() > newItem:
                    if self._tree[current].getLeftPtr() == -1:
                        index = 2 * current + 1
                        while len(self._tree) < index + 1:
                            self._tree.append(None)
                        self._tree[current].setLeftPtr(index)
                        self._tree[index] = Node(newItem)
                        break
                    else:
                        current = self._tree[current].getLeftPtr()
                else:
                    if self._tree[current].getRightPtr() == -1:
                        index = 2 * current + 2
                        while len(self._tree) < index + 1:
                            self._tree.append(None)
                        self._tree[current].setRightPtr(index)
                        self._tree[index] = Node(newItem)
                        break
                    else:
                        current = self._tree[current].getRightPtr()
                        
    def print(self):
        if self._root == -1:
            print("No data in array")
        else:
            print('{:<20}{:<20}{:<20}{}'.format('',\
                                        'Data', \
                                        'LeftPtr', \
                                        'RightPtr'))
            print('=' * 80)
            for i in range(len(self._tree)):
                if self._tree[i] != None:
                    print('{:<20}{:<20}{:<20}{}'.format(str(i) + ': ', \
                                        str(self._tree[i].getData()), \
                                        str(self._tree[i].getLeftPtr()), \
                                        str(self._tree[i].getRightPtr())))

    def inOrderTraversal(self):
        self._inOrderTraversalHelper(self._root)

    def _inOrderTraversalHelper(self, index):
        if index != -1:

            self._inOrderTraversalHelper(self._tree[index].getLeftPtr())
            print(self._tree[index].getData())
            self._inOrderTraversalHelper(self._tree[index].getRightPtr())

new_tree = Tree()
new_tree.add("Dave")
new_tree.add("Fred")
new_tree.add("Ed")
new_tree.add("Greg")
new_tree.add("Bob")
new_tree.add("Cid")
new_tree.add("Ali")
new_tree.print()
print()
new_tree.inOrderTraversal()

#Time Taken: 42.12.64
#Time Allowed: 54.00.00
