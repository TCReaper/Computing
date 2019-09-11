class GameArea():
	def __init__(self, area_id, area_name, area_desc):
		self._id = area_id
		self._name = area_name
		self._desc = area_desc
		self._obj = []

	def get_id(self):
		return self._id

	def get_name(self):
		return self._name

	def get_desc(self):
		return self._desc

	def add_obj(self, obj, obj_desc):
		self._obj.append([obj, obj_desc])

	def get_all_obj(self):
		for obj in self._obj:
			yield obj

class Links():
	def __init__(self, area_src, area_dst, link_name):
		self._src = area_src
		self._dst = area_dst
		self._name = link_name
		
	def get_src(self):
		return self._src
		
	def get_dst(self):
		return self._dst
		
	def get_name(self):
		return self._name
		
class GameMap():
	
	_areas_file = "RahulAreas.txt"
	
	def __init__(self):
		self._area_id = 1
		self._links_src = {}
		self._area_list = [None]
		self._link_list = []
		
		file_handle = open(self._areas_file, "r")
		
		for line in file_handle:
			current_area = line.strip().split(";")
			try:
				if int(current_area[0]) > self._area_id:
					self._area_id = int(current_area[0]) + 1
					
				try:
					self._area_list[current_area[0]] = (GameArea(int(current_area[0]), current_area[1], current_area[2]))
				except:
					self._area_list.append((GameArea(int(current_area[0]), current_area[1], current_area[2])))
				
				current_links = current_area[3].strip().split(",")
				current_link_names = current_area[4].strip().split(",")
				for ind in range(len(current_links)):
					temp = Links(int(current_area[0]), int(current_links[ind]), current_link_names[ind])
					self._link_list.append(temp)
					try:
						self._links_src[int(current_area[0])].append(self._link_list.index(self._link_list[-1]))
					except:
						self._links_src.setdefault(int(current_area[0]), [self._link_list.index(self._link_list[-1])])

			except Exception as ex:
				print("Failed to load area: " + line)
				print(type(ex))
				
		file_handle.close()
		self._current_area = self._area_list[1]
		
	def add_area(self, area_name, area_desc):
		temp = GameArea(self._area_id, area_name, area_desc)
		self._area_list.append(temp)
		self._area_id += 1
		
	def add_link(self, area_src, area_dst, link_name):
		temp = Links(area_src, area_dst, link_name)
		self._link_list.append(temp)
		
		
	def get_areas(self):
		for area in self._area_list:
			print(area.get_name())
			
	def get_links_src(self):
		print(self._links_src)
			
	def remove_area(self, area_id):
		try:
			for link in self._link_list:
				if link.get_dst() == area_id or link.get_src() == area_id:
					ind = self._link_list.index(link)
					self._link_list[ind] = None
					for key in self._links_src:
						if ind in self._links_src[key]:
							self._links_src[key].remove(ind)
					
			self._links_src.pop(area_id)
			self._area_list.remove(self._area_list[area_id])
			print("Removed area: ", area_id)
		except Exception as ex:
			print("Couldn't remove links for area of id: ", area_id)
			print("Due to: ", ex)
	
	def get_current(self):
		current = self._current_area
		print(current.get_name())
		print(current.get_desc())
		print()
		print("Objects available:")
		for obj in current.get_all_obj():
			print(obj[1])
		print()
		print("Exits available:")
		for link in self._links_src[current.get_id()]:
			print(str(self._links_src[current.get_id()].index(link)) + ": " + self._link_list[link].get_name())
		print()
		
	def move_with_link(self, link_ind):
		current = self._current_area
		self._current_area = self._area_list[self._link_list[self._links_src[current.get_id()][link_ind]].get_dst()]
		self.get_current()


map1 = GameMap()
map1._current_area.add_obj(..., "Empty object")
map1.get_current()

while True:
	player_in = input("Enter exit: ")
	print("#"*50)
	
	try:
		map1.move_with_link(int(player_in))
	except Exception as ex:
		if player_in.upper() == "X":
			print("Thank you for playing...")
			break
		else:
			print("Please enter a valid input...")
			print(ex)
	map1.get_links_src()
