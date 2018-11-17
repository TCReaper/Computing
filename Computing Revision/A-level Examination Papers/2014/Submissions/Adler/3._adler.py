def menu(linked_list):
    while True:
        choice = get_choice()
        if choice == 5:
            break
        elif choice == 1:
            linked_list.add_node()
        elif choice == 2:
            linked_list.traversal()
        elif choice == 3:
            linked_list.display_linked_list()
        elif choice == 4:
            linked_list.reverse_traversal()



def get_choice():
    while True:
        choice = input("\n1.  Add an item"\
                       "\n2.  Traverse the linked list of used nodes"\
                       " and output the data values"\
                       "\n3.  Output all pointers and data values"\
                       "\n4.  Traverse the linked list of used nodes"\
                       " and output the data values in reverse order"\
                       "\n5.  Exit\n")
        if choice.isdigit():
            choice = int(choice)
            if choice in range(1,6):
                return choice
        print("Invalid input! Enter a digit"\
              " corresponding to the desired option.")



class ListNode():
    def __init__(self, data_value):
        self._data_value = data_value
        self._pointer_value = 0

    def get_data_value(self):
        return self._data_value

    def set_data_value(self, new_data_value):
        self._data_value = new_data_value

    def get_pointer_value(self):
        return self._pointer_value

    def set_pointer_value(self, new_pointer_value):
        self._pointer_value = new_pointer_value

class LinkedList():
    def __init__(self):
        self._node = [None]
        for i in range(1, 30):
            temp = ListNode('')
            temp.set_pointer_value(i + 1)
            self._node.append(temp)
        self._node.append(ListNode(''))
        self._start = 0
        self._next_free = 1
        
    def add_node(self):
        if self.is_full():
            print("Linked list is full.")
            return False
        new_item = input("New Data Value: ")
        self._node[self._next_free].set_data_value(new_item)
        if self._start == 0:
            self._start = self._next_free
            temp = self._node[self._next_free].get_pointer_value()
            self._node[self._next_free].set_pointer_value(0)
            self._next_free = temp
        else:
            #traverse the list ñ at Start to find
            #the position at which to insert the new item
            temp = self._node[self._next_free].get_pointer_value()
            if new_item < self._node[self._start].get_data_value():
                #new item will become the start of the list
                self._node[self._next_free].set_pointer_value(self._start)
                self._start = self._next_free
                self._next_free = temp
            else:
                #the new item is not at the start of the list . . .
                previous = 0
                current = self._start
                found = False
                while not found and current != 0:
                    if new_item <= self._node[current].get_data_value():
                        self._node[previous].set_pointer_value(self._next_free)
                        self._node[self._next_free].set_pointer_value(current)
                        self._next_free = temp
                        found = True
                    else:
                        #move on the next node
                        previous = current
                        current = self._node[current].get_pointer_value()
                if current == 0:
                    self._node[previous].set_pointer_value(self._next_free)
                    self._node[self._next_free].set_pointer_value(0)
                    self._next_free = temp

    def display_linked_list(self):
        print("Start: " + str(self._start))
        print("Next Free: " + str(self._next_free))
        for i in range(1, len(self._node)):
            print("Index: {:<20}Data Value: {:<20}Pointer Value: {}"\
                  .format(str(i), str(self._node[i].get_data_value()),\
                          str(self._node[i].get_pointer_value())))
            
    def is_empty(self):
        return self._start == 0

    def is_full(self):
        return self._next_free == 0

    def traversal(self):
        self.traversal_in_order(self._start)
        
    def traversal_in_order(self, index):
        if index != 0:
            print(self._node[index].get_data_value())
            #follow the pointer to the next data item in the linked list
            self.traversal_in_order(self._node[index].get_pointer_value())
            
    def reverse_traversal(self):
        self.traversal_in_reverse_order(self._start)

    def traversal_in_reverse_order(self, index):
        if index != 0:
            #follow the pointer to the next data item in the linked list
            self.traversal_in_reverse_order(\
                self._node[index].get_pointer_value())
            print(self._node[index].get_data_value())

            
menu(LinkedList())

#51:11.68
