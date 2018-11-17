class Node():
    def __init__(self, Data, LeftP = 0, RightP = 0):
        self._Data = Data
        self._LeftP = LeftP
        self._RightP = RightP

    def get_Data(self):
        return self._Data

    def set_Data(self, new_Data):
        self._Data = new_Data

    def get_LeftP(self):
        return self._LeftP

    def set_LeftP(self, new_LeftP):
        self._LeftP = new_LeftP

    def get_RightP(self):
        return self._RightP

    def set_RightP(self, new_RightP):
        self._RightP = new_RightP


class BST():
    def __init__(self):
        self._ThisTree = [None] + [Node('', i, 0) for i in range(2, 21)]\
                         + [Node('')]
        self._Root = 0
        self._NextFreePosition = 1

    def AddItemToBinaryTree(self, NewTreeItem):
        if self._NextFreePosition == 0:
            return False
        self._ThisTree[self._NextFreePosition].set_Data(NewTreeItem)
        
        if self._Root == 0:
            self._Root = self._NextFreePosition
        else:
            #traversse the tree to find the position for the new value
            CurrentPosition = self._Root
            LastMove = 'X'
            while CurrentPosition != 0:
                PreviousPosition = CurrentPosition
                if NewTreeItem < self._ThisTree[CurrentPosition].get_Data():
                    #move left
                    LastMove = 'L'
                    CurrentPosition = self._ThisTree[CurrentPosition]\
                                      .get_LeftP()
                else:
                    #move right
                    LastMove = 'R'
                    CurrentPosition = self._ThisTree[CurrentPosition]\
                                      .get_RightP()
            if LastMove == 'X':
                raise IndexError
            if LastMove == 'R':
                self._ThisTree[PreviousPosition]\
                .set_RightP(self._NextFreePosition)
            else:
                self._ThisTree[PreviousPosition]\
                .set_LeftP(self._NextFreePosition)
        temp = self._ThisTree[self._NextFreePosition]
        self._NextFreePosition = self._ThisTree[self._NextFreePosition]\
                                 .get_LeftP()
        temp.set_LeftP(0)
        return True

    def OutputData(self):
        print("Root:", self._Root)
        print("NextFreePosition:", self._NextFreePosition)
        print("{:<10}{:<20}{:<10}{}".format("Index", "Data", "LeftP", "RightP"))
        for i in range(1, len(self._ThisTree)):
            print("{:<10}{:<20}{:<10}{}".format(\
                i,\
                self._ThisTree[i].get_Data(),\
                self._ThisTree[i].get_LeftP(),\
                self._ThisTree[i].get_RightP()))

    def InOrderTraversal(self, index = None):
        if index == None:
            index = self._Root
        if index != 0:
            self.InOrderTraversal(self._ThisTree[index].get_LeftP())
            print(self._ThisTree[index].get_Data())
            self.InOrderTraversal(self._ThisTree[index].get_RightP())
            
tree = BST()
while True:
    NewTreeItem = input("Data to input: ")
    if NewTreeItem == 'XXX':
        break
    tree.AddItemToBinaryTree(NewTreeItem)
tree.OutputData()
tree.InOrderTraversal()
