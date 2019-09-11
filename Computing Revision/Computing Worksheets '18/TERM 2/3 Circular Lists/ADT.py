

class Node():
      def __init__(self,name,mark):
            self._name = name
            self._mark = mark
            self._nextPtr = -1

      def setName(self,name):
            self._name = name
      def getName(self):
            return self._name

      def setMark(self,mark):
            self._mark = mark
      def getMark(self):
            return self._mark

      def setNextPtr(self,ptr):
            self._nextPtr = ptr
      def getNextPtr(self):
            return self._nextPtr

class LinkedList():
      def __init__(self):
            self._nodes = []
            self._head = -1

      def set_head(self,head):
            self._head = head
      def get_head(self):
            return self._head
            
      def addInOrder(self,name,mark):
            node = Node(name,mark)
            index = len(self._nodes)
            self._nodes.append(node)

            if self.get_head() == -1:
                  self.set_head(index)
            else:
                  curPtr = self.get_head()
                  current = self._nodes[curPtr]

                  if current.getName() > name:
                        node.setNextPtr(self._head)
                        self._head = index
                  while curPtr != -1:
                        
                        #print('check')
                        nextPtr = self._nodes[curPtr].getNextPtr()
                        if nextPtr == -1:
                              self._nodes[curPtr].setNextPtr(index)
                              break
                        if self._nodes[nextPtr].getName() > name:
                              node.setNextPtr(nextPtr)
                              self._nodes[curPtr].setNextPtr(index)
                              break
                        else:
                              curPtr = self._nodes[curPtr].getNextPtr()
                              break
            
      def print(self):
            for node in self._nodes:
                  print('{0:<15} | {1:<3} | {2:<4}'.format(node.getName(),str(node.getMark()),str(node.getNextPtr())))

      def countNodes(self):
            return len(self._nodes)

      def sortByMark(self):
            #just use a standard sorting algorithm?
            if self._head == -1:
                  return False
            else:
                  temp = []
                  self._head = -1
                  for i in range(len(self._nodes)):
                        node = self._nodes[i]
                        index = len(temp)
                        temp.append(node)
               
                        curPtr = self._head
                  if self._head == -1:
                        self._head = index
                  if temp[self._head].getMark() < node.getMark():
                        node.setNextPtr(self._head)
                        self._head = index
                  while curPtr != -1:
                        nextPtr = temp[curPtr].getNextPtr()
                        if nextPtr == -1:
                              temp[curPtr].setNextPtr(index)
                              break
                        if temp[nextPtr].getName() < node.getName():
                              node.setNextPtr(nextPtr)
                              temp[curPtr].setNextPtr(index)
                              break
                        else:
                              curPtr = temp[curPtr].getNextPtr()
                              self._nodes = temp
                              break

      def displayByMark(self):
            self.sortByMark()
            self.print()


x = LinkedList()
f = open('COLLEGE.txt')
for line in f:
      line = line.strip().split('|')
      x.addInOrder(line[0],line[1])
f.close()
x.displayByMark()
#i think ur ptrs r fked up




















