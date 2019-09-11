class GameArea():
    def __init__(self, area_id, area_name, area_desc):
        self._id = area_id
        self._name = area_name
        self._desc = area_desc

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_desc(self):
        return self._desc

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
	
	_areas_file = "Areas.txt"
	
	def __init__(self):
		self._area_id = 1
		self._links_src = {}
		self._links_dst = {}
		self._area_list = []
		
		file_handle = open(self._areas_file, "r")
		
		for line in file_handle:
			current_area = line.strip().split(";")
			try:
				if int(current_area[0]) > self._area_id:
					self._area_id = int(current_area[0]) + 1
					
				try:
					self._area_list[current_area[0]-1] = (GameArea(int(current_area[0]), current_area[1], current_area[2]))
				except:
					self._area_list.append((GameArea(int(current_area[0]), current_area[1], current_area[2])))
				
				current_links = current_area[3].strip().split(",")
				current_link_names = current_area[4].strip().split(",")
				for ind in range(len(current_links)):
					temp1 = Links(int(current_area[0]), int(current_links[ind]), current_link_names[ind])
					temp2 = Links(int(current_links[ind]), int(current_area[0]), current_link_names[ind])
					try:
						self._links_src[int(current_area[0])].append(temp1)
					except:
						self._links_src.setdefault(int(current_area[0]), [temp1])
						
					try:
						self._links_dst[int(current_links[ind])].append(temp2)
					except:
						self._links_dst.setdefault(int(current_links[ind]), [temp2])
			except Exception as ex:
				print("Failed to load area: " + line)
				print(type(ex))
				
		file_handle.close()
		self._current_area = self._area_list[0]
		
	def add_area(self, area_name, area_desc):
		temp = GameArea(self._area_id, area_name, area_desc)
		self._area_list.append(temp)
		self._area_id += 1
		
	def add_link(self, area_src, area_dst):
		temp = Links(area_src, area_dst)
		self._link_list.append(temp)
		
	def get_areas(self):
		for area in self._area_list:
			print(area.get_name())
			
	def get_links_src(self):
		for link_list in self._links_src.values():
			for link in link_list:
				print(link.get_name())
			
	def get_links_dst(self):
		for link_list in self._links_dst.values():
			for link in link_list:
				print(link.get_name())
			
	def remove_area(self, area_id):
		self._area_list.remove(self._area_list[area_id-1])
		try:
			self._links_src.pop(area_id)
			self._links_dst.pop(area_id)
		except:
			print("Couldn't remove links for area of id: ", area_id)
			
	def get_current(self):
		current = self._current_area
		print(current.get_name())
		print(current.get_desc())
		print("Exits available:")
		for link in self._links_src[current.get_id()]:
			print(str(self._links_src[current.get_id()].index(link)) + ": " + link.get_name())
			
		print()
		

map1 = GameMap()
map1.get_current()