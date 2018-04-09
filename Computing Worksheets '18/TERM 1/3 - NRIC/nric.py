
# task 1a

def input_nric():
      getting = True
      while getting:
            checking = True
            while checking:
                  nric = input("Input NRIC:   ")

                  #checking if correct length
                  if len(nric) != 9:      
                        checking = True
                        print('\nNRICs should be 9 digits long!\n')
                        break

                  #checking if letters and numbers
                  for letter in nric:     
                        if letter.isalnum() == False:
                              checking = True
                              print('\nPlease only input accepted NRIC numbers!\n')
                              break
                        else:
                              checking = False

                  #check if legit Singapore issued IC
                  if nric[0].upper() not in "STFG":
                        checking = True
                        print('\nAre you sure this is a real NRIC number?\n')
                        break
                  
                  #check if last element is a letter      
                  if nric[8].isnumeric() == True:
                        checking = True
                        print('\nLast element should be a letter!\n')
                        break

                  #check if other elements are numbers
                  if nric[1:8].isalpha() == True:
                        checking = True
                        print('\nElements in the middle should be integers!\n')
                        break
                  
            if not checking:
                  getting = False
                  
      print(nric.upper())

# task 1b

testset = ['T0040067F','S1681944A','T0000661B',
           'T0001507A','T0059197J','G1444444K',
           'T0012574F','T0078219E','S1648379P']

# task 1c

import random

letters = "qwertyuioplkjhgfdsazxcvbnm"
numbers = "1234567890"

def gen_nric():
      nric = ''
      #filling with structure of the NRIC
      nric += random.choice('stfg')
      for x in range(7):
            nric += random.choice(numbers)
      nric += random.choice(letters)
      nric = nric.upper()
      return nric

def population():
      NRICs = []
      for x in range(20):
            NRICs.append(gen_nric())
      f = open('NRIC_DATA2.TXT','w+')
      for nric in NRICs:
            f.write(str(nric)+'\n')
      f.close()



# task 1d

def sorting():
      g = open('NRIC_DATA2.TXT')
      NRICs = []
      for line in g:
            line = line.strip('\n')
            NRICs.append(str(line))
      g.close()
      sorted_nrics = insertion(NRICs)
      return sorted_nrics

def insertion(list):
      for i in range(1,len(list)+1):
            # Check where to insert
            while len(list) > i > 0 and list[i] < list[i-1]:
                  # Swaps the two numbers
                  list[i], list[i-1] = list[i-1], list[i]
                  i -= 1
      return(list)



# task 1e

class BST():
      def __init__(self):
            self._root = None

      def insert(self,data):
            #print(      type(data)        )
            if self._root == None:
                  self._root = Node(data)
            else:
                  current_node = self._root
                  while True:
                        #print(type(current_node))
                        if data < current_node.get_data():
                              if current_node._left == None:
                                    current_node.set_left( Node(data) ) 
                                    break
                              else:
                                    current_node = current_node.left()
                        else:
                              if current_node._right == None:
                                    current_node.set_right( Node(data) )
                                    break
                              else:
                                    current_node = current_node.right()
      def print_in(self):
            branch = self._root
            self.in_order(branch)
      def print_pre(self):
            branch = self._root
            self.pre_order(branch)
      def print_post(self):
            branch = self._root
            self.post_order(branch)
            
      def in_order(self, branch):
            if branch == None:
                  pass
            else:
                  self.in_order(branch.left())
                  print(branch.get_data())
                  self.in_order(branch.right())

      def pre_order(self, branch):
            if branch == None:
                  pass
            else:
                  print(branch.get_data())
                  self.in_order(branch.left())
                  self.in_order(branch.right())

      def post_order(self, branch):
            if branch == None:
                  pass
            else:
                  self.in_order(branch.left())
                  self.in_order(branch.right())
                  print(branch.get_data())


class Node():
      def __init__(self,data):
            self._data = data
            self._left = None
            self._right = None
      def get_data(self):
            return self._data
      def left(self):
            return self._left
      def right(self):
            return self._right
      def set_left(self,new_node):
            self._left = new_node
      def set_right(self,new_node):
            self._right = new_node



# task 1f

def script():
      BooSTed = BST()
      NRICs = []
      
      f = open('NRIC_DATA2.TXT')
      for line in f:
            line = line.strip('\n')
            NRICs.append(line)
      f.close()

      data1 = False
      if data1 == True:
            g = open('NRIC_DATA.TXT')
            for line in g:
                  line = line.strip('\n')
                  NRICs.append(line)
            g.close()

      for entry in NRICs:
            #print(entry)
            BooSTed.insert(entry)

      


      BooSTed.print_pre()
      print('\n')
      BooSTed.print_in()
      print('\n')
      BooSTed.print_post()
            
      
