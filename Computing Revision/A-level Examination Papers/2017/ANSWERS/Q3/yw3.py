#2017 q3
class ConnectionNode():
    def __init__(self, DataValue, LeftChild):
        self._DataValue = DataValue
        self._LeftChild = LeftChild
        self._RightChild = 0

    def set_DataValue(self, NewDataValue):
        self._DataValue = NewDataValue

    def get_DataValue(self):
        return self._DataValue

    def set_LeftChild(self, NewLeftChild):
        self._LeftChild = NewLeftChild

    def get_LeftChild(self):
        return self._LeftChild

    def set_RightChild(self, NewRightChild):
        self._RightChild = NewRightChild

    def get_RightChild(self):
        return self._RightChild

class linkedlist():
    def __init__(self):
        self._RobotData = [0] + [ConnectionNode(None, x+1) for x in range(1,25)] + [ConnectionNode(None, 0)]
        self._Root = 1
        self._NextFreeChild = 1

    def FindNode(self, NodeValue):
        found = False
        CurrentPosition = self._Root
        while not found and CurrentPosition <= 25:
            if self._RobotData[CurrentPosition].get_DataValue() == NodeValue:
                found = True
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
        print('Root: ' + str(self._Root))
        print('NextFreeChild: ' + str(self._NextFreeChild))
        for i in range(1,len(self._RobotData)):
            if self._RobotData[i].get_DataValue() != None:
                print(self._RobotData[i].get_DataValue() + ' ' + str(self._RobotData[i].get_LeftChild()) + ' '+ str(self._RobotData[i].get_RightChild()))

    def PreOrder(self):
        self._PreOrder_T(self._Root, '')

    def _PreOrder_T(self, index, string):
        if index != 0:
            temp = self._RobotData[index].get_DataValue()
            string += str(temp)
            if temp == 'Z':
                print(string)
                return
            self._PreOrder_T(self._RobotData[index].get_LeftChild(), string)
            if self._RobotData[index].get_RightChild() != 0:
                self._PreOrder_T(self._RobotData[index].get_RightChild(), string)
            else:
                pass
            return
            
temp = linkedlist()
f = open('SEARCHTREE.txt')
for i in f:
    i = i.strip().split(',')
    temp.AddToRobotData(i[0], i[1], i[2])
f.close()
temp.OutputData()
temp.PreOrder()





    
