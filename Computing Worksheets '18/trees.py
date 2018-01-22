import random

def task_a():
      leafs = []
      for i in range(50):
            x = random.randint(0,1000) / 10
            leafs.append(x)

      file = open('SCORES.TXT','w')
      file.close()

      file = open('SCORES.TXT','a')
      for element in leafs:
            file.write(str(element)+'\n')
      file.close()

def task_b():
      file = open('SCORES.TXT')
      leafs = []
      for line in file:
            line = line.strip()
            leafs.append(line)
      file.close()
      leafs = sorted(leafs)

      #printing

      temp = 0.0
      branch = []
      for element in leafs:
            element = float(element)
            #print(element)
            #print(element//10,temp)
            if element//10 == temp:
                  branch.append(round(element - temp*10.0,1))
            else:
                  print(int(temp*10),end = '\t|\t')
                  for i in branch:
                        print(str(i)+'\t',end='')
                  print()
                  temp += 1.0
                  branch = []
                  
def task_c():
      file = open('SCORES.TXT')
      leafs = []
      for line in file:
            line = line.strip()
            leafs.append(line)
      file.close()
      leafs = sorted(leafs)

      #printing

      temp = 0.0
      branch = []
      for element in leafs:
            element = float(element)
            #print(element//10,temp)
            if element//10 == temp:
                  branch.append(round(element - temp*10.0,1))
            else:
                  print(int(temp*10),end = '\t|')
                  for i in branch:
                        print('=',end='')
                  print()
                  temp += 1.0
                  branch = []
      print('\t|',end='')
      for i in range(1,10):
            print(i,end='')
      print()


#############################################################

class Node():
      def __init__(self,student_ID,score):
            self._student_ID = student_ID
            self._score = score
            self._left = None
            self._right = None
      def get_id(self):
            return self._student_ID
      def get_score(self):
            return self._score
      def get_left(self):
            return self._left
      def get_right(self):
            return self._right
      
class BST():
      def __init__(self,filename):
            self._root = None
            leafs = []
            file = open(filename,r)
            for line in file:
                  line = line.split(',')
                  leafs.append(line)
            for boi in leafs:
                  self.insert(boi[0],boi[1])
      def insert(self,boyid,score):
            if self._root == None:
                  self._root=Node(boyid,score)
            else:
                  cur = self._root
                  if boi[1] == 0:
                        pass

                  
            
                  
