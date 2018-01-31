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
                  branch = sorted(branch)
                  print(int(temp*10),end = '\t|\t')
                  for i in branch:
                        print(str(i)+'   ',end='')
                  print()
                  temp += 1.0
                  branch = [round(element - temp*10.0,1)]
                  
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
      def set_left(self,node):
            self._left = node
      def set_right(self,node):
            self._right = node
      
class BST():
      def __init__(self,filename):
            self._root = None
            leafs = []
            file = open(filename)
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
                  while True:
                        if score < cur.get_score():
                              if cur.get_left() == None:
                                    cur.set_left( Node(boyid,score) )
                                    break
                              else:
                                    cur = cur.get_left()
                        else:
                              if cur.get_right() == None:
                                    cur.set_right( Node(boyid,score) )
                                    break
                              else:
                                    cur = cur.get_right()
                                    
      def inorder_traversal(self,score):
            self._iot_helper(self._root,score)
            
      def _iot_helper(self,node,score):
            if node == None:
                  pass
            else:
                  self._iot_helper(node.get_left(),score)
                  if float(node.get_score()) < score:
                        print(node.get_id(),node.get_score())
                  self._iot_helper(node.get_right(),score)
                              
      def get_all_data(self):
            self.inorder_traversal(100.1)

      def get_weak_scores(self,score):
            self.inorder_traversal(score)

#############################################################

def task_e():
      students = []
      for i in range(50):
            student_ID = str(chr(random.randint(65,90))) + str(random.randint(000,999))
            while len(student_ID) != 4:
                  student_ID += "0"
            students.append(student_ID)
      for file_ext in range(1,5):
            write_file("SUBJECT_"+str(file_ext)+".TXT",students)
      BST_folder = []
      for make_bst in range(1,5):
            BST_folder.append(BST("SUBJECT_"+str(make_bst)+".TXT"))
      for i in BST_folder:
            print(str(i)*88)
            i.get_all_data()
            print('#'*88)
            i.get_weak_scores(40)
            

def write_file(filename,student_ids):
      task_a()
      file = open('SCORES.TXT')
      data = []
      for i in file:
            data.append(i.strip())
      file.close()
      file = open(filename,'w')
      for i in range(50):
            file.write(student_ids[i] + ',' + data[i] + '\n')
      file.close()
      

      
                  
            
                  
