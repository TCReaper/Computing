# The NJC Text-based RPG

###############################################################################
# Classes:
###############################################################################
class GameMap():

    _areas_file_name = "Areas.txt"
    # the information corresponding to each area is stored on 1 line in the
    # following format:
    #       <area_id (INT)>;<area_name (STR)>;<area_desc (STR)>;
    #       <link_1 (INT), ..., link_n (INT)>;<link_1_name (STR), ..., link_n_name (STR)>

    def __init__(self):
        self._next_area_id = 1
        self._areas = []
        
        # load existing areas from file
        f = open(self._areas_file_name)
        for line in f:
            current_area_info = line.split(";")
            try:
                if int(current_area_info[0]) > self._next_area_id:
                    self._next_area_id = int(current_area_info[0]) + 1
                self._areas.append(GameArea(int(current_area_info[0]), current_area_info[1], current_area_info[2]))
                current_links = current_area_info[3].strip().split(",")
                current_link_names = current_area_info[4].strip().split(",")
                for i in range(len(current_links)):
                    self._areas[-1].add_link(int(current_links[i]), current_link_names[i])
            except:
                print("Failed to load area: " + line)
        f.close()

    def get_new_area_id(self):
        pass

    def find_area(self, id):
        pass

    def find_origin_link(self):
        pass

    def find_dest_link(self):
        pass
###############################################################################
class GameArea():

    def __init__(self, new_id, new_name, new_desc):
        self._id = new_id
        self._name = new_name
        self._desc = new_desc
        self._links = []
        self._link_names = []

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_desc(self):
        return self._desc

    def add_link(self, new_id, new_link_name):
        self._links.append(new_id)
        self._link_names.append(new_link_name)

###############################################################################
# Menu
###############################################################################
game_map = GameMap()
