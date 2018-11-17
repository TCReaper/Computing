class Node():
    def __init__(self, data):
        self._data = data
        self._next = None
    def set_data(self, data):
        self._data = data
    def set_next(self, node):
        self._next = node    
    def get_data(self):
        return self._data
    def get_next(self):
        return self._next
    def __str__(self):
        return self._data

class LinkedList():
    def __init__(self):
        self._start = None

    def set_start(self, node):
        self._start = node

    def get_start(self):
        return self._start

    ## Task 3a
    def insert_data(self, data):
        pass

    ## Task 3b    
    def transfer(self, llist):
        pass

    ## Task 3c  
    def delete_pos(self, pos):
        pass

    def display(self):
        curr = self._start
        while curr:
            print(str(curr))
            curr = curr.get_next()

L1=LinkedList()
print("L1")
L1.insert_data("A")
L1.insert_data("B")
L1.insert_data("A")
L1.insert_data("B")
L1.insert_data("A")
L1.insert_data("B")
L1.display()
print("L2")
L2=LinkedList()
L2.insert_data("C")
L2.insert_data("D")
L2.insert_data("C")
L2.insert_data("D")
L2.insert_data("C")
L2.insert_data("D")
L2.display()
print("Transfer L2 to L1")
L1.transfer(L2)
print("L1--")
L1.display()
print("L2--")
L2.display()
print("Delete L1 1 - 6")
L1.delete_pos(1)
L1.delete_pos(2)
L1.delete_pos(3)
L1.delete_pos(4)
L1.delete_pos(5)
L1.delete_pos(6)
L1.display()
