def ValidateUserID(ThisUserID):
    if len(ThisUserID) != 9:
        return 1
    elif ThisUserID[4] != '_':
        return 2
    else:
        for i in ThisUserID:
            if i.isalpha() == True:
                return 3
    return 0

ThisUserID = input('UserID: ')
if ValidateUserID(ThisUserID) == 1:
    print('Invalid UserID length.')
elif ValidateUserID(ThisUserID) == 2:
    print('Invalid UserID format.')
elif ValidateUserID(ThisUserID) == 3:
    print('Invalid UserID characters.')
else:
    print('Valid UserID.')

#4.3
class PrintJob():
    def __init__(self, UserID, TerminalNumber, FileSize):
        self._UserID = UserID
        self._TerminalNumber = TerminalNumber
        self._FileSize = FileSize

    def get_UserID(self):
        return self._UserID

    def get_TerminalNumber(self):
        return self._TerminalNumber

    def get_FileSize(self):
        return self._FileSize
class PrintQueue():
    def __init__(self):
        self._Queue = []

    def print(self):
        for i in range(len(self._Queue)):
            print(str(i) + ': ' + str(self._Queue)[1:-1])
        
    def insert(self, Job):
        if len(self._Queue) == 5:
            print('Maximum queue size reached, try again later.')
        else:
            self._Queue = [Job] + self._Queue

    def output(self):
        if len(self._Queue) == 0:
            print('Empty queue, no jobs to output.')
        else:
            self._queue = self._Queue[:-1]

#4.4-#4.5
Room16 = PrintQueue()
Cont = True
while Cont:
    Option = input('1. New print job added to print queue\n2. Next print job output from printer\n3. Current print queue displayed\n 4. End\n')
    if Option == '1':
        UserID = input('UserID: ')
        while ValidateUserID(UserID) != 0:
            UserID = input('UserID: ')
        TerminalNumber = input('Terminal number: ')
        while TerminalNumber < 0 or TerminalNumber > 172:
            TerminalNumber = input('Terminal number: ')
        FileSize = input('File size : ')
        Room16.insert(PrintJob(UserID, TerminalNumber, FileSize))
    elif Option == '2':
        Room16.output()
    elif Option == '3':
        Room16.print()
    else:
        Cont = False

#4.5: enter 3
#4.6: enter 1
#4.7: enter 1 three times, enter 2, enter 3

#28


        
        
        
        
        
