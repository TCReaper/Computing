

class BST():
      def __init__(self):
            self._root = None

      def insert(self,ndata):
            if self._root == None:
                  self._root = Node(ndata,None)
            else:
                  current_node = self._root
                  while True:
                        if ndata < current_node.data():
                              if current_node.left() == None:
                                    current_node.set_left( Node(ndata,current_node) ) 
                                    break
                              else:
                                    current_node = current_node.left()
                        else:
                              if current_node.right() == None:
                                    current_node.set_right( Node(ndata,current_node) )
                                    break
                              else:
                                    current_node = current_node.right()

      def find(self,node_key):
            current_node = self._root
            while True:
                  try:
                        if current_node.data() == node_key:
                              return current_node

                        if node_key < current_node.data():
                              current_node = current_node.left()
                        else:
                              current_node = current_node.right()
                  except:
                        return None
                  finally:
                        pass
      
      def set_parents(self):
            start = self._root
            self._root.set_parent(None)
            self._parentset(start.left(),start)
            self._parentset(start.right(),start)

      def _parentset(self,node=None,parent=None):
            node.set_parent(parent)
            if node.left() is not None:
                  self._parentset(node.left(),node)
            if node.right() is not None:
                  self._parentset(node.right(),node)

      def set_heights(self):
            start = self._root
            a,b=0,0
            if start.left() != None:
                  a = self._heightset( start.left())
            if start.right() != None:
                  b = self._heightset( start.right())
            start.set_height( max(a,b))


      def _heightset(self,node=None,n=0):
            if node.left() == None and node.right() == None:
                  node.set_height(0)
                  return 1
            else:
                  a,b=0,0
                  if node.left() != None:
                        a = self._heightset( node.left(), n )
                  if node.right() != None:
                        b = self._heightset( node.right(), n )
                  node.set_height( max(a,b))
                  return max(a,b) + 1

      def check_avl(self,x=0):
            self.set_heights()
            avl = True
            node = self._root
            
            return self._avlcheck(node)[x]

      def _avlcheck(self,node=None):
            if node.left() != None and node.right() != None:
                  if node.left().height() - node.right().height() > 1 or node.left().height() - node.right().height() < -1:
                        return False,node.data()
                  else:
                        return self._avlcheck(node.left()) and self._avlcheck(node.right())
            return True,None

      def fix_avl(self):
            issue = self.find(self.check_avl(1))
            if issue == None:
                  print('BST already fulfils AVL')
                  self.display(sh=True)
                  return
            print('\nviolation of AVL with branches of',issue.data())
            self.display(sh=True)
            h = lambda x : x.height()
            if h(issue.right()) > h(issue.left()): #node is right heavy
                  if h(issue.right().right()) >= h(issue.right().left()): #right imbalance
                        self.left_rotate(issue)
                  else:
                        self.right_rotate(issue.right())
                        self.left_rotate(issue)
            else:
                  if h(issue.left().right()) <= h(issue.left().left()): #left imbalance
                        self.right_rotate(issue)
                  else:
                        self.left_rotate(issue.left())
                        self.right_rotate(issue)
            self.display(sh=True)

      



            


      def left_rotate(self,node_key):
            node = self.find(node_key)
            if node is None:
                  try:
                        node_key = node_key.data()
                        node = self.find(node_key)
                  except:
                        return 'failed'
            if node.parent() is None:
                  self._root = node.right()
                  node.set_right(self._root.left())
                  self._root.set_left(node)
            else:
                  parent_node = node.parent()
                  parent_node.set_left(node.right())
                  node.set_right(node.right().left())
                  parent_node.left().set_left(node)
            self.set_parents()
            print('\n=== left rotate on node {}'.format(node_key))
            self.display()

      def right_rotate(self,node_key):
            node = self.find(node_key)
            if node is None:
                  try:
                        node_key = node_key.data()
                        node = self.find(node_key)
                  except:
                        return 'failed'
            if node.parent() is None:
                  self._root = node.left()
                  node.set_left(self._root.right())
                  self._root.set_right(node)
            else:
                  parent_node = node.parent()
                  parent_node.set_right(node.left())
                  node.set_left(node.left().right())
                  parent_node.right().set_right(node)
            self.set_parents()
            print('\n=== right rotate on node {}'.format(node_key))
            self.display()

            

      def display(self,node=None,sh=False):
            if node is None:
                  node = self._root
            if sh:
                  print('\ndisplay heights')
                  self.set_heights()
                  lines, *_ = self._display_height(node)
            else:
                  print('\ndisplay data')
                  lines, *_ = self._display_aux(node)
            for line in lines:
                  print(line)
            print('- '*15)

      def _display_aux(self,node):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if node.right() is None and node.left() is None:
                  line = '%s' % node.data()
                  width = len(line)
                  height = 1
                  middle = width // 2
                  return [line], width, height, middle

            # Only left child.
            if node.right() is None:
                  lines, n, p, x = self._display_aux(node.left())
                  s = '%s' % node.data()
                  u = len(s)
                  first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                  second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                  shifted_lines = [line + u * ' ' for line in lines]
                  return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if node.left() is None:
                  lines, n, p, x = self._display_aux(node.right())
                  s = '%s' % node.data()
                  u = len(s)
                  first_line = s + x * '_' + (n - x) * ' '
                  second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                  shifted_lines = [u * ' ' + line for line in lines]
                  return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = self._display_aux(node.left())
            right, m, q, y = self._display_aux(node.right())
            s = '%s' % node.data()
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                  left += [n * ' '] * (q - p)
            elif q < p:
                  right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2


      def _display_height(self,node):
            # No child.
            if node.right() is None and node.left() is None:
                  line = '%s' % node.height()
                  width = len(line)
                  height = 1
                  middle = width // 2
                  return [line], width, height, middle

            # Only left child.
            if node.right() is None:
                  lines, n, p, x = self._display_height(node.left())
                  s = '%s' % node.height()
                  u = len(s)
                  first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                  second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                  shifted_lines = [line + u * ' ' for line in lines]
                  return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if node.left() is None:
                  lines, n, p, x = self._display_height(node.right())
                  s = '%s' % node.height()
                  u = len(s)
                  first_line = s + x * '_' + (n - x) * ' '
                  second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                  shifted_lines = [u * ' ' + line for line in lines]
                  return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = self._display_height(node.left())
            right, m, q, y = self._display_height(node.right())
            s = '%s' % node.height()
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                  left += [n * ' '] * (q - p)
            elif q < p:
                  right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2


class Node():
      def __init__(self,data,parent,height=0):
            self._data = data
            self._left = None
            self._right = None
            self._height = height
            self._parent = parent
      def data(self):
            return self._data
      def left(self):
            return self._left
      def right(self):
            return self._right
      def height(self):
            return self._height
      def parent(self):
            return self._parent
      def set_left(self,new_node):
            self._left = new_node
      def set_right(self,new_node):
            self._right = new_node
      def set_height(self,new_height):
            self._height = new_height
      def set_parent(self,new_parent):
            self._parent = new_parent



tree = BST()
for i in [50,40,60,55,35,45,65,53,57,58,47]:
      tree.insert(i)

tree.display()
tree.fix_avl()

