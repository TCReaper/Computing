def ValidateUserID(ThisUserID):
    if len(ThisUserID) != 9:
        return 1 #not length of 9
    if ThisUserID[:4] != '2015':
        return 2 #doesn't start with 2015
    if ThisUserID[4] != '_':
        return 3 #separator not '_'
    if not ThisUserID[6:].isdigit():
        return 4 #doesn't end with 4 digits
    return 0 #valid user id

def output_validity(index):
    mapping = ['Valid User ID', 'Invalid User ID: not of length 9',\
               'Invalid User ID: does not start with 2015',\
               'Invalid User ID: separator used is not "_"',\
               'Invalid User ID: does not end with 4 digits']
    print(mapping[index])
    
userID = input("\nUser ID: ")
index = ValidateUserID(userID)
output_validity(index)


class PrintJob():
    def __init__(self, userID, terminal_no, file_size):
        self._userID = userID
        self._terminal_no = terminal_no
        self._file_size = file_size
        self._next = -1

    def get_userID(self):
        return self._userID

    def set_userID(self, new_userID):
        self._userID = new_userID

    def get_terminal_no(self):
        return self._terminal_no

    def set_terminal_no(self, new_terminal_no):
        self._terminal_no = new_terminal_no

    def get_file_size(self):
        return self._file_size

    def set_file_size(self, new_file_size):
        self._file_size = new_file_size

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next

class Printer():
    def __init__(self, name):
        self._name = name
        self._head = -1
        self._tail = -1
        self._queue = [None for i in range(5)]
        
    def is_full(self):
        return not (None in self._queue)

    def get_next_free(self):
        for i in range(len(self._queue)):
            if self._queue[i] == None:
                return i
        return -1
    
    def add(self, userID, terminal_no, file_size):
        if self.is_full():
            print('Printer queue is full! Please wait for a while.\n')
        else:
            temp = self.get_next_free()
            self._queue[temp] = PrintJob(userID, terminal_no, file_size)
            if self._head == -1: #and self._head == self._tail:
                self._head = 0
                self._tail = 0
            else:
                self._queue[self._tail].set_next(temp)
                self._tail = temp

    def delete(self): #returns bool based on wheter deletion was successful
        if self._head == -1:
            return False
        temp = self._head
        self._head = self._queue[temp].get_next()
        self._queue[temp] = None
        return True

    def output_next(self):
        if self._head == -1:
            print("No current job\n")
        else:
            index = self._queue[self._head].get_next()
            if index == -1:
                print("No next job\n")
            else:
                print(self._queue[index].get_userID(),\
                      self._queue[index].get_terminal_no(),\
                      self._queue[index].get_file_size())
    def output(self):
        cur = self._head
        while cur != -1:
            print(self._queue[cur].get_userID(),\
                  self._queue[cur].get_terminal_no(),\
                  self._queue[cur].get_file_size())
            cur = self._queue[cur].get_next()

def menu(queue):
    while True:
        choice = input("1.  New print job added to print queue\n"\
                       "2.  Next print job output from printer\n"\
                       "3.  Current print queue displayed\n"\
                       "4.  End\n")
        #assuming choice is valid
        choice = int(choice)
        if choice == 4:
            #break
            return
        if choice == 1:
            userID = input("User ID\n")
            terminal_no = input("Terminal Number\n")
            file_size = input("File size\n")
            #assuming all inputs are valid
            queue.add(userID, terminal_no, file_size)
        elif choice == 2:
            queue.output_next()
        elif choice == 3:
            queue.output()

queue = Printer('Room16')
menu(queue)



#Time Taken: 56.04.06
#Time Allowed: 51.18.00
