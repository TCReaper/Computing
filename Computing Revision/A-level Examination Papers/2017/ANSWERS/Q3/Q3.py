class ConnectionNode():
    def __init__(self):
        self._DataValue = ''
        self._LeftChild = 0
        self._RightChild = 0

    def get_DataValue(self):
        return self._DataValue

    def get_LeftChild(self):
        return self._LeftChild

    def get_RightChild(self):
        return self._RightChild

    def set_DataValue(self, data):
        self._DataValue = data

    def set_LeftChild(self, left):
        self._LeftChild = left

    def set_RightChild(self, right):
        self._RightChild = right

class DataStructure():
    def __init__(self):
        self._RobotData = [None]
        self._Root = 1
        self._NextFreeChild = 1

        for i in range(1, 26):
            node = ConnectionNode()
            if not i == 25:
                node.set_LeftChild(i+1)
            self._RobotData.append(node)

    def FindNode(self, NodeValue):
        Found = False
        CurrentPosition = self._Root
        while Found != True and CurrentPosition < 26:
            if self._RobotData[CurrentPosition].get_DataValue() == NodeValue:
                Found = True
            else:
                CurrentPosition += 1

        if CurrentPosition > 25:
            return 0
        else:
            return CurrentPosition

    def AddToRobotData(self, NewDataItem, ParentItem, ThisMove):
        if self._Root == 1 and self._NextFreeChild == 1:
            self._NextFreeChild = self._RobotData[self._NextFreeChild].get_LeftChild()
            self._RobotData[self._Root].set_LeftChild(0)
            self._RobotData[self._Root].set_DataValue(NewDataItem)
        else:
            ParentPosition = self.FindNode(ParentItem)
            if ParentPosition > 0:
                ExistingChild = self.FindNode(NewDataItem)
                if ExistingChild > 0:
                    ChildPointer = ExistingChild
                else:
                    ChildPointer = self._NextFreeChild
                    self._NextFreeChild = self._RobotData[self._NextFreeChild].get_LeftChild()
                    self._RobotData[ChildPointer].set_LeftChild(0)
                    self._RobotData[ChildPointer].set_DataValue(NewDataItem)

                if ThisMove == 'L':
                    self._RobotData[ParentPosition].set_LeftChild(ChildPointer)
                else:
                    self._RobotData[ParentPosition].set_RightChild(ChildPointer)

    def OutputData(self):
        print('{:<13}: {}'.format('Root', self._Root))
        print('{:<13}: {}'.format('NextFreeChild', self._NextFreeChild))
        print()
        print('{:<15} {:<9} {:<9}'.format('DataValue', 'LeftChild', 'RightChild'))
        for i in range(1, 26):
            node = self._RobotData[i]
            print('{:<15} {:<9} {:<9}'.format(node.get_DataValue(), \
                                              node.get_LeftChild(), \
                                              node.get_RightChild()))

    def _pre_order(self, tree, string):
        node = self._RobotData[tree]
        if node == None or node.get_DataValue() == '':
            return
        elif node.get_DataValue() == 'Z':
            print(string + 'Z')
        else:
            string += node.get_DataValue()
            self._pre_order(node.get_LeftChild(), string)
            self._pre_order(node.get_RightChild(), string)

    def FindAtoZ(self):
        if self._Root == self._NextFreeChild:
            print('Empty')
        else:
            self._pre_order(1, '')

tree = DataStructure()

file_handle = open('SEARCHTREE.TXT')

for line in file_handle:
    data, parent, move = line.strip().split(',')
    tree.AddToRobotData(data, parent, move)
file_handle.close()

tree.OutputData()
