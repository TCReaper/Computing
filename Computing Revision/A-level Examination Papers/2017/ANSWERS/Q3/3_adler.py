class ConnectionNode():
    def __init__(self, DataValue, LeftChild = 0, RightChild = 0):
        self._DataValue = DataValue
        self._LeftChild = LeftChild
        self._RightChild = RightChild

    def get_DataValue(self):
        return self._DataValue

    def set_DataValue(self, NewDataValue):
        self._DataValue = NewDataValue

    def get_LeftChild(self):
        return self._LeftChild

    def set_LeftChild(self, NewLeftChild):
        self._LeftChild = NewLeftChild

    def get_RightChild(self):
        return self._RightChild

    def set_RightChild(self, NewRightChild):
        self._RightChild = NewRightChild

    def __str__(self):
        return str(self._DataValue) + ' '\
               +  str(self._LeftChild) + ' '\
               + str(self._RightChild)

class LinkedList():
    def __init__(self):
        self.RobotData = [ConnectionNode(None, i + 1) for i in range(1, 25)]
        self.RobotData.append(ConnectionNode(None))
        self.Root = 1
        self.NextFreeChild = 1

    def FindNode(self, NodeValue): #returns INT
        Found = False
        CurrentPosition = self.Root
        while (not Found) and CurrentPosition <= 25:
            if self.RobotData[CurrentPosition - 1].get_DataValue() == NodeValue:
                Found = True
            else:
                CurrentPosition += 1
        if CurrentPosition > 25:
            return 0
        else:
            return CurrentPosition

    def AddToRobotData(self, NewDataItem, ParentItem, ThisMove):
        if self.Root == 1 and self.NextFreeChild == 1:
            self.NextFreeChild = \
                    self.RobotData[self.NextFreeChild - 1].get_LeftChild()
            self.RobotData[self.Root - 1].set_LeftChild(0)
            self.RobotData[self.Root - 1].set_DataValue(NewDataItem)
        else:
            #does parent exist?
            ParentPosition = self.FindNode(ParentItem)
            if ParentPosition > 0:
                #parent exists
                #does child exist?
                ExistingChild = self.FindNode(NewDataItem)
                if ExistingChild > 0:
                    #child exists
                    ChildPointer = ExistingChild
                else:
                    ChildPointer = self.NextFreeChild
                    self.NextFreeChild = \
                        self.RobotData[self.NextFreeChild - 1].get_LeftChild()
                    self.RobotData[ChildPointer - 1]\
                                                .set_LeftChild(0)
                    self.RobotData[ChildPointer - 1]\
                                                .set_DataValue(NewDataItem)
                if ThisMove == 'L':
                    self.RobotData[ParentPosition - 1]\
                                                  .set_LeftChild(ChildPointer)
                else:
                    self.RobotData[ParentPosition - 1]\
                                                  .set_RightChild(ChildPointer)
			    
               
    def OutputData(self):
        for i in range(len(self.RobotData)):
            if self.RobotData[i].get_DataValue() != None:
                print(self.RobotData[i])
        print()

    def PreOrderTraversal(self):
        self._helperPreOrderTraversal(self.Root, '')
        print()
        
    def _helperPreOrderTraversal(self, index, result):
        if index != 0:
            result += str(self.RobotData[index - 1].get_DataValue())
            if self.RobotData[index - 1].get_DataValue() == 'Z':
                print(result)
            self._helperPreOrderTraversal(\
                self.RobotData[index - 1].get_LeftChild(), result)
            self._helperPreOrderTraversal(\
                self.RobotData[index - 1].get_RightChild(), result)
        else:
            return result
        
        
array = LinkedList()
f = open("SEARCHTREE.txt")
for line in f:
    temp = line.strip().split(',')
    array.AddToRobotData(temp[0], temp[1], temp[2])
f.close()

array.OutputData()
array.PreOrderTraversal()

      
#Time Taken: 57.27.35
#Time Allowed: 54.00.00
