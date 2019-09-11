###############################################################################
# The NJC Text-based RPG
###############################################################################





###############################################################################
# Classes:
###############################################################################
class GameMap():

    _areas_file_name = "DLAreas.txt"
    # the information corresponding to each area is stored on 1 line in the
    # following format:
    #   <area_id (INT)>;<area_name (STR)>;<area_desc (STR)>

    _links_file_name = "DLLinks.txt"
    # the information corresponding to each link is stored on 1 line in the
    # following format:
    #   <origin_area_id (INT)>;<destination_area_id (INT)>;<link name (STR)>

    def __init__(self):
        self._next_area_id = 1
        self._areas = []
        self._links = []
        
        # load existing areas from file
        f = open(self._areas_file_name)
        for line in f:
            current_area_info = line.strip().split(";")
            try:
                current_area_id = int(current_area_info[0])
                if current_area_id > self._next_area_id:
                    self._next_area_id = current_area_id + 1
                self._areas.append(GameArea(current_area_id, current_area_info[1], current_area_info[2]))
            except:
                print("Failed to load area: " + line)
        f.close()

        # load existing links from file
        f = open(self._links_file_name)
        for line in f:
            current_link_info = line.strip().split(";")
            try:
                self._links.append(GameAreaLink(int(current_link_info[0]), int(current_link_info[1]), current_link_info[2]))
            except:
                print("Failed to load link: " + line)
        f.close()

    def list_areas(self):
        if len(self._areas) == 0:
            print("Currently no areas.")
        else:
            print("{0:<10}{1:<30}".format("AREA ID", "AREA NAME"))
            for i in range(len(self._areas)):
                print("{0:<10}{1:<30}".format(str(self._areas[i].get_id()), str(self._areas[i].get_name())))

    def list_links(self):
        if len(self._links) == 0:
            print("Currently no links.")
        else:
            print("{0:<10}{1:<10}{2:<30}".format("ORIGIN ID", "DEST. ID", "LINK NAME"))
            for i in range(len(self._links)):
                print("{0:<10}{1:<10}{2:<30}".format(str(self._links[i].get_origin_id()), str(self._links[i].get_destination_id()), str(self._links[i].get_name())))

    def get_new_area_id(self):
        new_area_id = self._next_area_id
        self._next_area_id += 1
        return new_area_id

    def find_area(self, area_id):
        # returns None if not found or else returns the GameArea object with
        # the specified area_id
        for i in range(len(self._areas)):
            if self._areas[i].get_id() == area_id:
                return self._area[i]
        return None

    def find_link(self, origin_id, destination_id):
        # returns None if not found or else returns the GameLink object with
        # the specified origin_id and destination_id
        for i in range(len(self._areas)):
            if self._links[i].get_origin() == origin_id and self._links[i].get_destination() == destination_id:
                return self._links[i]
        return None

    def add_area(self, area_name, area_description):
        self._areas.append(GameArea(self.get_new_area_id(), area_name, area_description))

    def add_link(self, origin_id, destination_id, link_name):
        current_link = find_link(origin_id, destination_id)
        if (not current_link == None) and (current_link.get_name() == link_name):
            print("Link already exists.")
        else:
            self._links.append(GameLink(origin_id, destination_id, link_name))

    def delete_link(self, origin_id = None, destination_id = None, link_name = None):
        # if origin_id == None and destination_id == None then do nothing; delete failed
        # if origin_id == None then delete all links with specified destination_id
        # if destination_id == None then delete all links with specified origin_id
        # if origin != None and destination_id != None and link_name == None then delete all links with specified origin_id and destination_id
        # if link_name != None then delete all links with specified origin_id, destination_id and link_name
        indices_to_delete = []
        if origin_id == None and destination_id == None:
            return False
        elif origin_id == None:
            for i in range(len(self._links)):
                if self._links[i].get_destination() == destination_id:
                    indices_to_delete = [i] + indices_to_delete
        elif destination_id == None:
            for i in range(len(self._links)):
                if self._links[i].get_origin() == origin_id:
                    indices_to_delete = [i] + indices_to_delete
        elif link_name == None:
            for i in range(len(self._links)):
                if self._links[i].get_origin() == origin_id and self._links[i].get_destination() == destination_id:
                    indices_to_delete = [i] + indices_to_delete
        else:
            for i in range(len(self._links)):
                if self._links[i].get_origin() == origin_id and self._links[i].get_destination() == destination_id and self._links[i].get_name() == link_name:
                    indices_to_delete = [i] + indices_to_delete
        for i in range(len(indices_to_delete)):
            del self._links[i]
        if len(indices_to_delete) > 0:
            return True
        else:
            return False

    def delete_area(self, area_id):
        # delete the area with the specified area_id as well as all links
        # with the area as the origin or the destination
        if self.find_area(area_id) == None:
            return False # assumes that links will only contain an area_id that exists
        else:
            for i in range(len(self._areas)):
                if self._areas[i].get_id() == area_id:
                    del self._areas[i]
                    break
            self.delete_link(self, origin_id = area_id, destination_id = None, link_name = None)
            self.delete_link(self, origin_id = None, destination_id = area_id, link_name = None)
            return True

###############################################################################
class GameArea():

    def __init__(self, new_id, new_name, new_description):
        self._id = new_id
        self._name = new_name
        self._description = new_description

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description
    
    def set_id(self,new_id):
        self._id = new_id

    def set_name(self,new_name):
        self._name = new_name

    def set_description(self,new_description):
        self._description = new_description
###############################################################################
class GameAreaLink():

    def __init__(self, new_origin_id, new_destination_id, new_name):
        self._origin_id = new_origin_id
        self._destination_id = new_destination_id
        self._name = new_name

    def get_origin_id(self):
        return self._origin_id

    def get_destination_id(self):
        return self._destination_id

    def get_name(self):
        return self._name

    def set_origin_id(self, new_origin_id):
        self._origin_id = new_origin_id

    def set_destination_id(self, new_destination_id):
        self._destination_id = new_destination_id

    def set_name(self, new_name):
        self._name = new_name
###############################################################################
###############################################################################
###############################################################################





###############################################################################
# main
###############################################################################
def main_menu():
    get_input = True
    while get_input:
        print("(1) Play\n(2) Edit Map\n(3) Exit\n")
        main_menu_input = input("Please select an option: 1, 2 or 3")
        if not main_menu_input in ["1", "2", "3"]:
            print("Invalid input! Please select only 1, 2 or 3.")
        else:
            get_input = False
    return main_menu_input

game_map = GameMap()
game_map.list_areas()
game_map.list_links()
