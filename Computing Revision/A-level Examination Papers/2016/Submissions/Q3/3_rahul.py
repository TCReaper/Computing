class Node():
    def __init__(self, data):
        self._data = data
        self._leftPtr = -1
        self._rightPtr = -1

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
        self._tree = []
        self._root = -1

    def add(self, newItem):
        if self._root == -1:
            self._root = 0
            node = Node(newItem)
            self._tree.append(node)
        else:
            node = Node(newItem)
            current = self._root
            while True:
                cur_node = self._tree[current]
                if newItem <= cur_node.getData():
                    if cur_node.getLeftPtr() == -1:
                        cur_node.setLeftPtr(len(self._tree))
                        self._tree.append(node)
                        break
                    else:
                        current = cur_node.getLeftPtr()
                else:
                    if cur_node.getRightPtr() == -1:
                        cur_node.setRightPtr(len(self._tree))
                        self._tree.append(node)
                        break
                    else:
                        current = cur_node.getRightPtr()

    def print(self):
        print('{:<10}{:<10}{:<10}'.format('Data', 'LeftPtr', 'RightPtr'))
        for i in range(len(self._tree)):
            node = self._tree[i]
            print('{:<10}{:<10}{:<10}'.format(node.getData(), node.getLeftPtr(), \
                                              node.getRightPtr()))

    def inOrderTraversal(self):
        if self._root == -1:
            print('Empty')
        else:
            self._in_order(self._root)

    def _in_order(self, ind):
        if ind == -1:
            pass
        else:
            node = self._tree[ind]
            self._in_order(node.getLeftPtr())
            print(node.getData())
            self._in_order(node.getRightPtr())

tree = Tree()
for i in ['Dave', 'Fred', 'Ed', 'Greg', 'Bob', 'Cid', 'Ali']:
    tree.add(i)
tree.print()
print()
tree.inOrderTraversal()
