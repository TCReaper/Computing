
def ValidateUserID(userID):
    if len(userID) != 9:
        print("This is invalid!!! :<<<")
        return 0
    for i in range(4):
        if not userID[i].isdigit():
            print("This is invalid!!!!")
            return 0
    if userID[4]!="_":
        print("This is invalid!!!")
        return 0
    for i in range(5,9):
        if not userID[i].isdigit():
            print("This is invalid!!!")
            return 0
    print("This is a valid ID hahahhahaha.")
    return 1

class PrintJob:
    def __init__(self, userID):
        self._userID = userID
        self._terminalNO = -1
        self._fileSize = -1

    def get_userID(self):
        return self._userID

    def get_terminalNO(self):
        return self._terminalNO

    def get_fileSize(self):
        return self._fileSize

    def set_userID(self, userID):
        self._userID = userID

    def set_terminalNO(self, terminalNO):
        self._terminalNO = terminalNO

    def set_fileSize(self, fileSize):
        self._fileSize = fileSize

class Printer:
    def __init__(self, name):
        self._name = name
        self._queue = [0,0,0,0,0]
        self._head = 0
        self._tail = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def add_inqueue(self, newJob):
        self._queue[self._tail] = newJob
        self._tail += 1
        if self._tail == 5:
            self._tail = 0

    def del_queue(self):
        self._head += 1
        if self._head == 5:
            self._head = 0

    def display(self):
        i = self._head
        while i != self._tail:
            print(self._queue[i].get_userID())
            i += 1
            if i == 5:
                i = 0 



printer = Printer("heyu") 
endProgram = False
while not endProgram:
    print("1. New print job added to the queue.")
    print("2. Next print job output from printer.")
    print("3. Current print queue displayed.")
    print("4. End")
    n = int(input("Please choose an option: "))
    if n == 1:
        tested = False
        while not tested:
            userID = input("Please enter userID: ")
            if ValidateUserID(userID):
                tested = True
        newJob = PrintJob(userID)
        printer.add_inqueue(newJob)
    elif n == 2:
        printer.del_queue()
    elif n == 3:
        printer.display()
    else:
        endProgram = True 
        
            
        
