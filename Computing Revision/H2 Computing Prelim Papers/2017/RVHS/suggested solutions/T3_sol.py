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

    def insert_data(self, data):
        newNode = Node(data)
        if self._start:
            newNode.set_next(self._start)
            self._start = newNode
        else:
            self._start = newNode
            
    def transfer(self, llist):
        curr = self._start
        prev = None
        if self._start:
            while curr:
                prev = curr
                curr = curr.get_next()
            prev.set_next(llist.get_start())
            llist.set_start(None)
        else:
            self._start = llist.get_start()
            llist.set_start(None)
            
    def delete_pos(self, pos):
        count = 1
        curr = self._start
        prev = None
        while curr and count < pos:
            prev = curr
            curr = curr.get_next()
            count += 1

        if curr and count == pos:
            if prev == None:
                #deleting the first Node
                self._start = curr.get_next()
                
            else:
                #deleting the Node at pos
                prev.set_next(curr.get_next())
        else:
            print("invalid pos")


            

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
