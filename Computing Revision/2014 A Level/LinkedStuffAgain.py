

class LinkedList():
      def __init__(self):
            self.Initialise()
            
      def Initialise(self):
            self._Start = 1
            self._NextFree = 1
            self._Node = [ListNode('',x+1) for x in range(30)]

      def IsEmpty(self):
            if self._NextFree == 1:
                  return True
            else:
                  return False
            
      def DisplayLinkedList(self):
            currentNode = self._Node[self._Start]
            point = self._Start
            while currentNode._PointerValue != 1:
                  print(point,currentNode._DataValue,' ==> ',currentNode._PointerValue)
                  point = currentNode._PointerValue
                  if point == 30:
                        point = 0
                  currentNode = self._Node[point]
            print(point,currentNode._DataValue,' ==> ',currentNode._PointerValue)
                  
      def AddNode(self):
            NewItem = input('New item to add: ')
            self._Node[self._NextFree]._DataValue

            if self._Start = 0:
                  self._Start = self._NextFree
                  temp = self._Node[self._NextFree]._PointerValue
                  self._Node[self._NextFree]._PointerValue = 0
                  self._NextFree = temp
            else:
                  pass
      def Traversal(self):
            pass

class ListNode():
      def __init__(self,datavalue,point):
            self._DataValue = datavalue
            self._PointerValue = point
      
#Task 3.1

linkedlist = LinkedList()
menu = True
while menu:
      choice = input(" CHOOSE YOUR MENU OPTION:\n   \
                     1. Add an item\n   \
                     2. Traverse the linked list of used nodes and output the data values\n   \
                     3. Output all pointers and data values\n   \
                     5. Exit\n\t>> ")
      if choice == '5':
            menu = False
      else:
            if choice == '1':
                  linkedlist.AddNode()
            elif choice == '2':
                  linkedlist.Traversal()
            elif choice == '3':
                  linkedlist.DisplayLinkedList()
            
                  
      
