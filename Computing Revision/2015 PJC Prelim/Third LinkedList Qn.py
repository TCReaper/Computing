

class ListNode():
      def __init__(self,word,point):
            self._word = word
            self._count = 1
            self._pointer = point
            print(' i want to kill myself',point)

      
class LinkedList():
      def __init__(self):
            self.Initialise()
            self._Start = 0
            self._NextFree = 0
      def Initialise(self):
            self._Node = [ListNode('',x) for x in range(0,30)]
