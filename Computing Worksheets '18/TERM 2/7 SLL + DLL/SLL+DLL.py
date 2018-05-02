class SLLNode():

    def __init__(self, new_data):
        self._data = new_data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, new_data):
        self._data = new_data

    def set_next(self, new_next):
        self._next = new_next

    def __str__(self):
        return str(self._data)

    def print(self):
        print(self)

class SLL():

    def __init__(self):
        self._first = None
        self._last = None

    def get_first(self):
        return self._first

    def get_last(self):
        return self._last

    def set_first(self, new_first):
        self._first = new_first

    def set_last(self, new_last):
        self._last = new_last

    def insert_front(self, new_data):
        new_node = SLLNode(new_data)
        if self._first == None:
            self._first = new_node
            self._last = new_node
        else:
            new_node.set_next(self._first)
            self._first = new_node

    def insert_back(self, new_data):
        new_node = SLLNode(new_data)
        if self._first == None:
            self._first = new_node
            self._last = new_node
        else:
            self._last.set_next(new_node)
            self._last = new_node

    def exists(self, target_data):
        current_node = self._first
        while current_node != None:
            if current_node.get_data() == target_data:
                return True
            else:
                current_node = current_node.get_next()
        return False

    def delete(self, target_data):
        if self._first == None:
            # empty SLL
            return False
        elif self._first.get_data() == target_data:
            # target in first node
            if self._first.get_next() == None:
                # only 1 element in SLL
                self._first = None
                self._last = None
            else:
                self._first = self._first.get_next()
            return True
        else:
            # non-empty SLL, target not in first
            previous_node = self._first
            current_node = self._first.get_next()
            while current_node != None:
                if current_node.get_data() == target_data:
                    current_next = current_node.get_next()
                    previous_node.set_next(current_node.get_next())
                    if current_next == None:
                        # current_node is the last node
                        self._last = previous_node
                    return True
                else:
                    previous_node = current_node
                    current_node = current_node.get_next()
            return False

    def __str__(self):
        res = ""
        current_node = self._first
        while current_node != None:
            res += str(current_node)
            if current_node.get_next() != None:
                res += ", "
            current_node = current_node.get_next()
        return res

    def print(self):
        print(self)

class DLLNode(SLLNode):

    def __init__(self, new_data):
        super().__init__(new_data)
        self._prev = None

    def get_prev(self):
        return self._prev

    def set_prev(self, new_prev):
        self._prev = new_prev

class DLL(SLL):

    def insert_front(self, new_data):
        new_node = DLLNode(new_data)
        if self._first == None:
            self._first = new_node
            self._last = new_node
        else:
            new_node.set_next(self._first)
            self._first.set_prev(new_node)
            self._first = new_node

    def insert_back(self, new_data):
        new_node = DLLNode(new_data)
        if self._first == None:
            self._first = new_node
            self._last = new_node
        else:
            self._last.set_next(new_node)
            new_node.set_prev(self._last)
            self._last = new_node

    def delete(self, target_data):

        if self._first == None:
            # empty SLL
            return False
        else:
            cur_n = self._first
            while cur_n != None:
                if cur_n.get_data() != target_data:
                    cur_n = cur_n.get_next()
                else:
                    # found - now delete
                    if cur_n.get_next() != None:
                        cur_n.get_next().set_prev(cur_n.get_prev())
                    if cur_n.get_prev() != None:
                        cur_n.get_prev().set_next(cur_n.get_next())
                    if cur_n == self._first:
                        self._first = cur_n.get_next()
                    if cur_n == self._last:
                        self._last = cur_n.get_prev()
                    return True
            return False

# testing
from random import randint
my_list = DLL()

elements1 = []
for i in range(10):
    elements1.append(randint(1, 100))
elements2 = []
for i in range(10):
    elements2.append(randint(-100, -1))

print("\nInserting (front): " + str(elements1))
for i in range(len(elements1)):
    my_list.insert_front(elements1[i])
print("List now contains:")
my_list.print()

print("\nInserting (back): " + str(elements2))
for i in range(len(elements2)):
    my_list.insert_back(elements2[i])
print("List now contains:")
my_list.print()

print("\nChecking exists (inserted front):")
for i in range(len(elements1)):
    print("\tElement " + str(elements1[i]) + " -> " + \
          ("Found" if my_list.exists(elements1[i]) else "Not Found"))

print("\nChecking exists (inserted back):")
for i in range(len(elements2)):
    print("\tElement " + str(elements2[i]) + " -> " + \
          ("Found" if my_list.exists(elements2[i]) else "Not Found"))

print("\nChecking exists (random):")
for i in range(10):
    current = randint(-100, 100)
    print("\tElement " + str(current) + " -> " + \
          ("Found" if my_list.exists(current) else "Not Found"))

print("\nList now contains:")
my_list.print()
print("\nChecking delete (3 inserted front; 3 inserted back):")
for i in [-3, -2, -1]:
    deleted1 = my_list.delete(elements1[i])
    deleted2 = my_list.delete(elements2[i])
    print("\tDeleting element [" + str(i) + "] " + str(elements1[i]) + \
          " -> " + ("Deleted" if deleted1 else "Unable to delete"))
    print("\tDeleting element [" + str(i) + "] " + str(elements2[i]) + \
          " -> " +("Deleted" if deleted2 else "Unable to delete"))

deleted = my_list.delete(0) # non-existent element
print("\tDeleting element " + str(0) + " -> " + \
          ("Deleted" if deleted else "Unable to delete"))

print("\nList now contains:")
my_list.print()

print("\nInserting (front): " + str(elements1))
for i in range(len(elements1)):
    my_list.insert_front(elements1[i])
print("List now contains:")
my_list.print()

print("\nInserting (back): " + str(elements2))
for i in range(len(elements2)):
    my_list.insert_back(elements2[i])
print("List now contains:")
my_list.print()

print("\nChecking exists (inserted front):")
for i in range(len(elements1)):
    print("\tElement " + str(elements1[i]) + " -> " + \
          ("Found" if my_list.exists(elements1[i]) else "Not Found"))

print("\nChecking exists (inserted back):")
for i in range(len(elements2)):
    print("\tElement " + str(elements2[i]) + " -> " + \
          ("Found" if my_list.exists(elements2[i]) else "Not Found"))

print("\nChecking exists (random):")
for i in range(10):
    current = randint(-100, 100)
    print("\tElement " + str(current) + " -> " + \
          ("Found" if my_list.exists(current) else "Not Found"))
