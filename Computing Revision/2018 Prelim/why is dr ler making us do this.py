import datetime

###########################question 1##############################

a = datetime.datetime(1965,8,9)

data = []

file_handle = open('DATA.txt')

for line in file_handle:
      line = line.split('V1')[1].split('V2')
      v1 = float(line[0])
      line = line[1].split('V3')
      v2 = float(line[0])
      v3 = float(line[1])

      dd = '{0:>02}'.format(a.day)
      mm = '{0:>02}'.format(a.month)
      yyyy = '{0:>04}'.format(a.year)

      date = dd+mm+yyyy

      data_tuple = (date,v1,v2,v3)
      
      data.append(data_tuple)

      a += datetime.timedelta(1)
      
file_handle.close()

###########################question 3##############################


class FaultReport():
      def __init__(self,senderName,senderEmail,description,date):
            for i in senderName:
                  if i.isalpha() == False and i != ' ':
                        raise ValueError
            self._senderName = senderName
            if senderEmail != 'email':
                  raise ValueError
            self._senderEmail = senderEmail
            self._description = description
            if len(date.replace('-','')) != 6 or not date.replace('-','').isnumeric():
                  raise ValueError
            self._date = date

            self._priority = ''
            self._serviceType = ''
            self._status = ''

      def getName(self):
            return self._senderName
      
      def getEmail(self):
            return self._senderEmail
      
      def getDesc(self):
            return self._description
      
      def getDate(self):
            return self._date
      
      def getPriority(self):
            return self._priority
      
      def getServiceType(self):
            return self._serviceType
      
      def getStatus(self):
            return self._status

      def setPriority(self,priority):
            self._priority = priority
            
      def setServiceType(self,serviceType):
            self._serviceType = serviceType
            
      def setStatus(self,status):
            self._status = status

      def print(self):
            print('== REPORT ==\n')
            
            print('{0:<10}{1}'.format('Name',self._senderName))
            print('{0:<10}{1}'.format('Email',self._senderEmail))
            print('{0:<10}{1}'.format('Description',self._description))
            print('{0:<10}{1}'.format('Date',self._date))
            print('{0:<10}{1}'.format('Priority',self._priority))
            print('{0:<10}{1}'.format('Service Type',self._serviceType))
            print('{0:<10}{1}'.format('Status',self._status))

            print('\n'*3)

class QueueNode():
      def __init__(self,index):
            self._index = index
            self._link1 = -1
            
      def get_data(self):
            return self._data
      
      def get_link1(self):
            return self._link1
      
      def set_link1(self,link):
            self._link1 = link

      def print(self):
            print('REPORT INDEX: {0}; NEXT: {1}'.format(self._index,self._link1))

class BSTNode(QueueNode):
      def __init__(self,index):
            super()
            self._link2 = -1
            
      def get_link2(self):
            return self._link2
      
      def set_link2(self,link):
            self._link2 = link

      def print(self):
            print('REPORT INDEX: {0}; LEFT: {1}; RIGHT: {2}'.\
                  format(self._index,self._link1,self._link2))


class Reports():
      def __init__(self,max_capacity):
            self._reports = []
            self._capacity = max_capacity
            self._BST = []
            self._rootIndex = -1
            self._queue = []
            self._headIndex: -1
            self._tailIndex = -1

      def BSTInsert(self,data):
            pass
      
      def BSTSearch(self,data):
            pass
      
      def queueIsFull(self):
            if len(self._queue) == self._capacity:
                  return True
            else:
                  return False
      def 























                  
            
