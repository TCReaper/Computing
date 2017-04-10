class GameArea():				#Game Area objects, methods are pretty self explanatory. obj part is still preliminary
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

class Links():				#Linker objects, methods are pretty self explanatory
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
		
class GameMap():				#Game Map object, ahhhh gg...
	
	def __init__(self, filename):
		#Just some attributes
		self._area_id = 2
		self._links_src = {}
		self._area_list = [None]
		self._link_list = []
		
		#The real meat
		file_handle = open(filename, "r")
		
		for line in file_handle:
			current_area = line.strip().split(";")
			try:
				if int(current_area[0]) > self._area_id:
					self._area_id = int(current_area[0]) + 1		#Setting of the next area_id
					
				try:
					self._area_list[current_area[0]] = (GameArea(int(current_area[0]), current_area[1], current_area[2]))		#Create the new GameArea object
				except:
					self._area_list.append((GameArea(int(current_area[0]), current_area[1], current_area[2])))
				
				current_links = current_area[3].strip().split(",")					#Creating all the links
				current_link_names = current_area[4].strip().split(",")
				for ind in range(len(current_links)):
					temp = Links(int(current_area[0]), int(current_links[ind]), current_link_names[ind])
					self._link_list.append(temp)
					try:
						self._links_src[int(current_area[0])].append(self._link_list.index(self._link_list[-1]))
					except:
						self._links_src.setdefault(int(current_area[0]), [self._link_list.index(self._link_list[-1])])

			except Exception as ex:				#If things go south...
				print("Failed to load area: " + line)
				print(type(ex))
				
		file_handle.close()
		self._current_area = self._area_list[1]		#Set the starting room to the first room initialized
		
	def add_area(self, area_name, area_desc):				#Simply create a GameArea object and add it to the existing list
		temp = GameArea(self._area_id, area_name, area_desc)
		self._area_list.append(temp)
		self._area_id += 1
		print("Added " + area_name + " to the map")
		
	def add_link(self, area_src, area_dst, link_name):				#Still working on this part, links need to be added to the dict 
		temp = Links(area_src, area_dst, link_name)
		self._link_list.append(temp)
		ind = self._link_list.index(self._link_list[-1])
		try:
			self._links_src[area_src].append(ind)
		except:
			self._links_src.setdefault(area_src, [ind])
		
	def get_areas(self):				#Print the names of all the areas in this map
		for area in self._area_list:
			print(area.get_name())
			
	def get_links_src(self):			#Print the dict
		print(self._links_src)
			
	def remove_area(self, area_id):				#A bit complicated
		try:
			for link in self._link_list:
				if link.get_dst() == area_id or link.get_src() == area_id:			#If a link has the area_id associated with it
					ind = self._link_list.index(link)
					self._link_list[ind] = None				#Change the link to None type
					for key in self._links_src:
						if ind in self._links_src[key]:
							self._links_src[key].remove(ind)			#Remove the area_id from the dict coopletely
					
			self._links_src.pop(area_id)
			self._area_list.remove(self._area_list[area_id])
			print("Removed area: ", area_id)
		except Exception as ex:								#If anything foes wrong...
			print("Couldn't remove links for area of id: ", area_id)
			print("Due to: ", ex)
	
	def get_current(self):				#Print out details of the current room
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
		
	def move_with_link(self, link_ind):					#Change the current room using the link provided
		current = self._current_area
		self._current_area = self._area_list[self._link_list[self._links_src[current.get_id()][link_ind]].get_dst()]
		self.get_current()
		
	def save_state(self, filename):
		file_handle = open(filename, "w")
		
		for area in self._area_list[1:]:
			area_string = str(area.get_id()) + ";" + area.get_name() + ";" + area.get_desc() + ";"
			link_dst = []
			link_names = []
			for link in self._links_src[area.get_id()]:
				link_dst.append(self._link_list[link].get_dst())
				link_names.append(self._link_list[link].get_name())
				
			area_string += str(link_dst[0])
			for i in range(1, len(link_dst)):
				area_string += "," + str(link_dst[i])
			area_string += ";" + link_names[0]
			for i in range(1, len(link_names)):
				area_string += "," + link_names[i]
				
			file_handle.write(area_string + "\n")
		
		file_handle.close()

#How it works:
#Game Areas are stored in a list
#Link objects store the index of the source and destination Game Area, in the Game Area list
#Link objects are stored in a list too
#The dict contains the indexes of the Links associated with each Game Area id, in the Link objects list

#Main Menu and Modes of gameplay
def edit_game(map):
	while True:
		print("What do you want to do? ")
		print("0: Add room")
		print("1: Add Link")
		print("2: Remove room")
		print("3: Quit editing mode")
		choice = int(input())
		print("#"*50)
		if choice == 3:
			break
		elif choice == 0:
			new_name = input("Enter the name of the area: ")
			new_desc = input("Enter description of your room: ")
			map.add_area(new_name, new_desc)
			print("#"*50)
		elif choice == 1:
			new_link_src = int(input("Enter the area id of the source: "))
			new_link_dst = int(input("Enter the area id of the destination: "))
			new_link_name = input("Enter the link name: ")
			map.add_link(new_link_src, new_link_dst, new_link_name)
			print("#"*50)
		elif choice == 2:
			area_id = int(input("Enter the area id of the room to delete: "))
			map.remove_area(area_id)
			print("#"*50)
	return 0
		
def play_game(map):
	map.get_current()
	while True:
		player_in = input("Enter exit: ")
		print("#"*50)
		
		try:
			map.move_with_link(int(player_in))
		except Exception as ex:
			if player_in.upper() == "X":
				print("Thank you for playing...")
				break
			else:
				print("Please enter a valid input...")
				print(ex)
	return 0
				
def main_menu():
	map1 = GameMap("RahulAreas2.txt")
	while True:
		print("What do you want to do?")
		print("0: Edit map")
		print("1: Play map")
		print("2: Quit game")
		choice = int(input())
		print("#"*50)
		if choice == 2:
			map1.save_state("RahulAreas2.txt")
			return 0
		elif choice == 1:
			play_game(map1)
		elif choice == 0:
			edit_game(map1)
		
#Testing
main_menu()
