class ConnectionNode:
    def __init__(self):
        self._DataValue = None
        self._LeftChild = 0
        self._RightChild = 0

    def get_data(self):
        return self._DataValue

    def get_left(self):
        return self._LeftChild

    def get_right(self):
        return self._RightChild

    def set_data(self, data):
        self._DataValue = data

    def set_left(self, left):
        self._LeftChild = left

    def set_right(self, right):
        self._RightChild = right

class LinkedList:
    def __init__(self):
        self._Root = 1
        self._RobotData = [0] 
        for i in range(1,26):
            self._RobotData.append(ConnectionNode())
            if i!=25:
                self._RobotData[i].set_left(i+1)
        self._NextFreeChild = 1 

    def findNode(self, node_value):
        found = False
        currentPosition = self._Root
        while found == False and currentPosition <=25:
            if self._RobotData[currentPosition].get_data() == node_value:
                found = True
            else:
                currentPosition += 1
        if currentPosition > 25:
            return 0
        else:
            return currentPosition

    def addToRobotData(self, new_data, parent_item, this_move):
        if self._Root == 1 and self._NextFreeChild == 1:
            self._NextFreeChild = self._RobotData[self._NextFreeChild].get_left()
            self._RobotData[self._Root].set_left(0)
            self._RobotData[self._Root].set_data(new_data)
        else:
            parentPosition = self.findNode(parent_item)
            if parentPosition > 0:
                existingChild = self.findNode(new_data)
                if existingChild > 0:
                    childPointer = existingChild
                else:
                    childPointer = self._NextFreeChild
                    self._NextFreeChild = self._RobotData[self._NextFreeChild].get_left()
                    self._RobotData[childPointer].set_left(0)
                    self._RobotData[childPointer].set_data(new_data)
                if this_move == 'L':
                    self._RobotData[parentPosition].set_left(childPointer)
                else:
                    self._RobotData[parentPosition].set_right(childPointer)

    def OutputData(self):
        print("Root= ", self._Root)
        print("NextFreeChild= ", self._NextFreeChild)
        for i in range(1,len(self._RobotData)):
            print(self._RobotData[i].get_data())

    def pre_order_traversal(self, i, path):
        path += str(self._RobotData[i].get_data())
        if self._RobotData[i].get_data() == 'Z':
            print(path)
            return
        if self._RobotData[i].get_left() != 0:
            self.pre_order_traversal(self._RobotData[i].get_left(), path)
        else:
            current_left = ''
        if self._RobotData[i].get_right() != 0:
            self.pre_order_traversal(self._RobotData[i].get_right(), path)
        else:
            current_right = ''
        return

    def pre_order(self):
        if self._Root == None:
            print('')
        else:
            print(self.pre_order_traversal(self._Root, ''))
            


file = open("SEARCHTREE.TXT","r")
LL = LinkedList() 
for line in file:
    new_data, parent_item, this_move = line.replace("\n","").split(',')
    LL.addToRobotData(new_data, parent_item, this_move)
LL.OutputData()
LL.pre_order()

    
