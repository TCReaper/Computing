class Node(object):
	def __init__(self, data):
		self._data = data
		self._left = None
		self._right = None
		
	def get_data(self):
		return self._data
		
	def get_left(self):
		return self._left
		
	def get_right(self):
		return self._right
	
	def set_data(self, new_data):
		self._data = new_data
		
	def set_left(self, new_left):
		self._left = new_left
		
	def set_right(self, new_right):
		self._right = new_right

class BST():
	def __init__(self):
		self._root = None
		
	def insert_i(self, data):
		if self._root == None:
			self._root = Node(data)
		else:
			current = self._root
			while True:
				if data < current.get_data():
					if current.get_left() == None:
						current.set_left(Node(data))
						break
					else:
						current = current.get_left()
				else:
					if current.get_right() == None:
						current.set_right(Node(data))
						break
					else:
						current = current.get_right()
	
	def insert_r(self, data):
		if self._root == None:
			self._root = Node(data)
		else:
			self.insert_recursive(data, self._root)
	
	def insert_recursive(self, data, current):
		if data < current.get_data():
			if current.get_left() == None:
				current.set_left(Node(data))
			else:
				self.insert_recursive(data, current.get_left())
		else:
			if current.get_right() == None:
				current.set_right(Node(data))
			else:
				self.insert_recursive(data, current.get_right())
	
	def find(self, data):
		parent = self.get_parent(data)
		
		if parent == None:
			return None
		else:
			if data < parent.get_data():
				return parent.get_left()
			else:
				return parent.get_right()

	def get_parent(self, data):
		if self._root.get_data() == data:
			return None
			
		if self._root == None:
			return None
		else:
			current = self._root
			while True:
				if current == None:
					return None
				
				if data < current.get_data():
					if current.get_left().get_data() == data:
						return current
					else:
						current = current.get_left()
				else:
					if current.get_right().get_data() == data:
						return current
					else:
						current = current.get_right()
				
	def delete(self, data):
		node_del = self.find(data)
		node_parent = self.get_parent(data)
		left = node_parent.get_left() == node_del
		if node_del.get_left() == None and node_del.get_right() == None:
			if left:
				node_parent.set_left(None)
			else:
				node_parent.set_right(None)
		elif node_del.get_left() == None:
			if left:
				node_parent.set_left(node_del.get_right())
			else:
				node_parent.set_right(node_del.get_right())
		elif node_del.get_right() == None:
			if left:
				node_parent.set_left(node_del.get_left())
			else:
				node_parent.set_right(node_del.get_left())
		else:
			node_rep = self.find_max(node_del.get_left())
			new_data = node_rep.get_data()
			node_rep_parent = self.get_parent(new_data)
			if node_rep_parent.get_left() == node_rep:
				node_rep_parent.set_left(None)
			else:
				node_rep_parent.set_right(None)
			node_del.set_data(new_data)
	
	def find_max(self, tree):
		current = tree
		while current.get_right() != None:
			current = current.get_right()
		return current
	
	def print_pre_order(self):
		for x in self._pre_order(self._root):
			print(x)
	
	def print_post_order(self):
		for x in self._post_order(self._root):
			print(x)
			
	def print_in_order(self):
		for x in self._in_order(self._root):
			print(x)
	
	def _pre_order(self, tree):
		if tree == None:
			pass
		else:
			yield tree.get_data()
			for x in self._pre_order(tree.get_left()):
				yield x
			for x in self._pre_order(tree.get_right()):
				yield x
				
	def _post_order(self, tree):
		if tree == None:
			pass
		else:
			for x in self._post_order(tree.get_left()):
				yield x
			for x in self._post_order(tree.get_right()):
				yield x
			yield tree.get_data()
			
	def _in_order(self, tree):
		if tree == None:
			pass
		else:
			for x in self._in_order(tree.get_left()):
				yield x
			yield tree.get_data()
			for x in self._in_order(tree.get_right()):
				yield x


#Checking functionality
tree = BST()
for x in [5, 3, 7, 2, 4, 6, 8]:
	tree.insert_r(x)

print('#'*30)
tree.print_in_order()
print('#'*30)
tree.delete(3)
tree.print_in_order()
print('#'*30)
print(tree.get_parent(5))
