##############################################################################################################################################################
# The NJC Text-based RPG
##############################################################################################################################################################





##############################################################################################################################################################
# Classes:
##############################################################################################################################################################
class GameMap():

    _areas_file_name = "DLAreas.txt"
    # the information corresponding to each area is stored on 1 line in the
    # refer to GameArea class's __init__ for format

    _links_file_name = "DLLinks.txt"
    # the information corresponding to each link is stored on 1 line in the
    # refer to GameAreaLink class's __init__ for format

    def __init__(self):
        self._next_area_id = 1
        self._areas = []
        self._links = []
        # load existing areas from file
        f = open(self._areas_file_name)
        for line in f:
            self._areas.append(GameArea(file_io_str = line.strip()))
            current_area_id = self._areas[-1].get_id()
            if current_area_id >= self._next_area_id:
                self._next_area_id = current_area_id + 1
        f.close()
        # load existing links from file
        f = open(self._links_file_name)
        for line in f:
            self._links.append(GameAreaLink(file_io_str = line.strip()))
        f.close()

    def save(self):
        # save areas
        f = open(self._areas_file_name, "w")
        for i in range(len(self._areas)):
            f.write(str(self._areas[i]) + "\n")
        f.close()
        # save links
        f = open(self._links_file_name, "w")
        for i in range(len(self._links)):
            f.write(str(self._links[i]) + "\n")
        f.close()
        print("\nCurrent game map saved.")

    def list_areas(self):
        if len(self._areas) == 0:
            print("\nCurrently no areas.")
        else:
            print("\n")
            print("{0:=<10}{1:=<30}".format("", ""))
            print("{0:<10}{1:<30}".format("AREA ID", "AREA NAME"))
            for i in range(len(self._areas)):
                print("{0:<10}{1:<30}".format(str(self._areas[i].get_id()), str(self._areas[i].get_name())))
            print("{0:=<10}{1:=<30}".format("", ""))

    def list_links(self, origin_id = None, destination_id = None):
        if len(self._links) == 0:
            print("\nCurrently no links.")
        else:
            print("\n")
            print("{0:=<10}{1:=<10}{2:=<30}".format("", "", ""))
            print("{0:<10}{1:<10}{2:<30}".format("ORIG. ID", "DEST. ID", "LINK NAME"))
            if origin_id == None and destination_id == None:
                for i in range(len(self._links)): 
                    print("{0:<10}{1:<10}{2:<30}".format(str(self._links[i].get_origin_id()), str(self._links[i].get_destination_id()), str(self._links[i].get_name())))
            elif origin_id == None:
                for i in range(len(self._links)):
                    if self._links[i].get_destination_id() == destination_id:
                        print("{0:<10}{1:<10}{2:<30}".format(str(self._links[i].get_origin_id()), str(self._links[i].get_destination_id()), str(self._links[i].get_name())))
            elif destination_id == None:
                for i in range(len(self._links)):
                    if self._links[i].get_origin_id() == origin_id:
                        print("{0:<10}{1:<10}{2:<30}".format(str(self._links[i].get_origin_id()), str(self._links[i].get_destination_id()), str(self._links[i].get_name())))
            else:
                for i in range(len(self._links)):
                    if self._links[i].get_origin_id() == origin_id and self._links[i].get_destination_id() == destination_id:
                        print("{0:<10}{1:<10}{2:<30}".format(str(self._links[i].get_origin_id()), str(self._links[i].get_destination_id()), str(self._links[i].get_name())))
            print("{0:=<10}{1:=<10}{2:=<30}".format("", "", ""))

    def get_new_area_id(self):
        new_area_id = self._next_area_id
        self._next_area_id += 1
        return new_area_id

    def get_area(self, area_id):
        # returns None if not found or else returns the GameArea object with
        # the specified area_id
        for i in range(len(self._areas)):
            if self._areas[i].get_id() == area_id:
                return self._areas[i]
        return None

    def get_link(self, origin_id, destination_id):
        # returns None if not found or else returns the GameLink object with
        # the specified origin_id and destination_id
        for i in range(len(self._areas)):
            if self._links[i].get_origin_id() == origin_id and self._links[i].get_destination_id() == destination_id:
                return self._links[i]
        return None

    def add_area(self, area_name, area_description):
        self._areas.append(GameArea(self.get_new_area_id(), area_name, area_description))

    def add_link(self, origin_id, destination_id, link_name):
        current_link = get_link(origin_id, destination_id)
        if (not current_link == None) and (current_link.get_name() == link_name):
            print("\nLink already exists.")
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
                if self._links[i].get_destination_id() == destination_id:
                    indices_to_delete = [i] + indices_to_delete
        elif destination_id == None:
            for i in range(len(self._links)):
                if self._links[i].get_origin_id() == origin_id:
                    indices_to_delete = [i] + indices_to_delete
        elif link_name == None:
            for i in range(len(self._links)):
                if self._links[i].get_origin_id() == origin_id and self._links[i].get_destination_id() == destination_id:
                    indices_to_delete = [i] + indices_to_delete
        else:
            for i in range(len(self._links)):
                if self._links[i].get_origin_id() == origin_id and self._links[i].get_destination_id() == destination_id and self._links[i].get_name() == link_name:
                    indices_to_delete = [i] + indices_to_delete
        for i in range(len(indices_to_delete)):
            del self._links[indices_to_delete[i]]
        if len(indices_to_delete) > 0:
            return True
        else:
            return False

    def delete_area(self, area_id):
        # delete the area with the specified area_id as well as all links
        # with the area as the origin or the destination
        area_to_delete = self.get_area(area_id)
        if area_to_delete == None:
            return False # assumes that links will only contain an area_id that exists
        else:
            for i in range(len(self._areas)):
                if self._areas[i].get_id() == area_id:
                    del self._areas[i]
                    break
            self.delete_link(origin_id = area_id, destination_id = None, link_name = None)
            self.delete_link(origin_id = None, destination_id = area_id, link_name = None)
            return True
##############################################################################################################################################################
class GameArea():

    def __init__(self, new_id = None, new_name = None, new_description = None, file_io_str = None):
        if file_io_str == None:
            # all other parameters must be specified
            self._id = new_id
            self._name = new_name
            self._description = new_description
        else:
            try:
                # if file_io_str != None then expecting ";" delimited attributes
                # following format:
                # <area_id (INT)>;<area_name (STR)>;<area_desc (STR)>
                # also expecting that other parameters == None
                data = file_io_str.split(";")
                self._id = int(data[0])
                self._name = data[1]
                self._description = data[2]
            except:
                print("\nFailed to load area: " + file_io_str)

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def set_id(self, new_id):
        self._id = new_id

    def set_name(self, new_name):
        self._name = new_name

    def set_description(self, new_description):
        self._description = new_description

    def display(self):
        print("\n" + self.get_name() + "\n\n" + self.get_description() + "\n")

    def __str__(self):
        return str(self._id) + ";" + self._name + ";" + self._description
    
##############################################################################################################################################################
class GameAreaLink():

    def __init__(self, new_origin_id = None, new_destination_id = None, new_name = None, file_io_str = None):
        if file_io_str == None:
            # all other parameters must be specified
            self._origin_id = new_origin_id
            self._destination_id = new_destination_id
            self._name = new_name
        else:
            try:
                # if file_io_str != None then expecting ";" delimited attributes
                # following format:
                # <origin_area_id (INT)>;<destination_area_id (INT)>;<link name (STR)>
                # also expecting that other parameters == None
                data = file_io_str.split(";")
                self._origin_id = int(data[0])
                self._destination_id = int(data[1])
                self._name = data[2]
            except:
                print("\nFailed to load link: " + line)

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

    def __str__(self):
        return str(self._origin_id) + ";" + str(self._destination_id) + ";" + self._name
    
##############################################################################################################################################################

class MiniMenu():
    def __init__(self,new_id,new_name,new_options):
        self._id = new_id
        self._name = new_name
        self._options = new_options #list

    def get_options(self):
        for option in self._options:
            print(option+"\n")

    

    
    
    

##############################################################################################################################################################
##############################################################################################################################################################





##############################################################################################################################################################
# main
##############################################################################################################################################################

# MAIN MENU
###########
# (1) Play
# (2) Edit
# (3) Quit

# MAIN EDIT MENU
################
# (1) List Areas
# (2) List Links
# (3) Goto Existing Area
# (4) Create New Area
# (5) Save Changes
# (6) Back to Main Menu

# AREA EDIT MENU
################
# (1) Edit Area Name/Desc
# (2) List (Related) Link
# (3) Add Link
# (4) Delete Link
# (5) Delete Current Area
# (6) Save Changes
# (7) Back to Main Edit Menu
# (8) Back to Main Menu

# PLAY MENU
###########
# (1) Link_1 Name
# ... ... ... ...
# (n) Link_n Name



# main initialisation variables
global debug
global game_map
global current_area

debug = True
game_map = GameMap()
current_aera = None

main_menu_options = ["Play", "Edit" , "Quit"]
main_edit_menu_options = ["List Areas", "List Links", "Goto Existing Area", "Create New Area", "Save Changes", "Back to Main Menu"]
area_edit_menu_options = ["Edit Area Name/Desc", "List (Related) Link", "Add Link", "Delete Link", "Delete Current Area", "Save Changes", "Back to Main Edit Menu", "Back to Main Menu"]

menu_options = [["exit"], main_menu_options, main_edit_menu_options, area_edit_menu_options, ["play"]]


# helper functions
def menu(option_strings):
    # expects option_strings to be a list of strings containing the menu options
    get_input = True
    while get_input:
        for i in range(len(option_strings)):
            print("(" + str(i + 1) + ") " + option_strings[i])
        menu_input = input("\nPlease select an option: ")
        valid_options = []
        for i in range(len(option_strings)):
            valid_options.append(str(i + 1))
        if not menu_input in valid_options:
            print("\nInvalid input!")
            print("Please only input an integer from 1 to " + str(len(option_strings)) + " (inclusive).")
        else:
            get_input = False
    return int(menu_input)

def invalid_value_message(tag):
    global debug
    if debug:
        print("\nInvalid menu selection input! (" + str(tag) + ")") # should never reach this unless someone really messed up ... meaning you!

def get_area_id_input(msg):
    get_input = True
    while get_input:
        try:
            area_id_input = int(input(msg))
            get_input = False
        except:
            print("\nInvalid input, area id should be an integer.")
    return area_id_input

def get_new_area_name():
    get_input = True
    while get_input:
        area_name_input = input("\nPlease enter the area name: ")
        if area_name_input != "":
            get_input = False
    return area_name_input

def get_new_area_decription():
    get_input = True
    while get_input:
        area_decription_input = input("\nPlease enter the area description: ")
        if area_decription_input != "":
            get_input = False
    return area_decription_input

def do_selection(current_menu, menu_selection):
    global debug
    global game_map
    global current_area
    if current_menu == 0:
        invalid_value_message(1) # this should never be true
        return 0 # exit
    elif current_menu == 1:
        if menu_selection == 1:
            # TO BE IMPLMENTED
            # (1) Edit Area Name/Desc
            print("\nNot implemented.")
            return 1 # main
            #return 4 # play
        elif menu_selection == 2:
            return 2 # main_edit
        elif menu_selection == 3:
            return 0 # exit
        else:
            invalid_value_message(2) # this should never be true
    elif current_menu == 2:
        if menu_selection == 1:
            game_map.list_areas()
            return current_menu # no menu change
        elif menu_selection == 2:
            game_map.list_links()
            return current_menu # no menu change
        elif menu_selection == 3:
            # print area information
            current_area = game_map.get_area(get_area_id_input("\nPlease enter the area id to goto: "))
            if current_area == None:
                print("\nArea not found.")
            else:
                print("\nCurrent Area ID: " + str(current_area.get_id()))
                current_area.display()
                # print link information (all origin ids as current area id)
                game_map.list_links(current_area.get_id())
                # print link information (all destination ids are current area id)
                game_map.list_links(destination_id = current_area.get_id())
            return 3 # main_area_edit
        elif menu_selection == 4:
            game_map.add_area(get_new_area_name(), get_new_area_decription())
            print("\nArea created.")
            return current_menu # no menu change
        elif menu_selection == 5:
            game_map.save()
            return current_menu # no menu change
        elif menu_selection == 6:
            return 1 # main
        else:
            invalid_value_message(3)
    elif current_menu == 3:
        if menu_selection == 1:
            # TO BE IMPLMENTED
            # (1) Edit Area Name/Desc
            print("\nNot implemented.")
            return 1 # main
        elif menu_selection == 2:
            # print link information (all origin ids as current area id)
            game_map.list_links(current_area.get_id())
            # print link information (all destination ids are current area id)
            game_map.list_links(destination_id = current_area.get_id())
            return current_menu
        elif menu_selection == 3:
            # TO BE IMPLMENTED
            # (3) Add Link
            print("\nNot implemented.")
            return 1 # main
        elif menu_selection == 4:
            if game_map.delete_link(get_area_id_input("Please enter origin area id for link to delete: "), get_area_id_input("Please enter destination area id for link to delete: ")):
                print("\nLink deleted.")
            else:
                print("\nLink not found.")
            return current_menu
        elif menu_selection == 5:
            if game_map.delete_area(current_area.get_id()):
                current_area = None
                print("\nArea deleted.")
            else:
                print("\nArea not found.")
            return 2 # main_edit
        elif menu_selection == 6:
            game_map.save()
            return current_menu
        elif menu_selection == 7:
            return 2 # main_edit
        elif menu_selection == 8:
            return 1 # main
        else:
            invalid_value_message(4)
    elif current_menu == 4:
        # TO BE IMPLMENTED
        # (1) Play
        print("\nNot implemented.")
        return 1 # main
    else:
        invalid_value_message(5)

def print_buffer():
    print("\n\n"+"="*78)



# main execution
current_menu_option = 1 # main
while current_menu_option != 0:
    print_buffer()
    current_menu_option = do_selection(current_menu_option, menu(menu_options[current_menu_option]))



##############################################################################################################################################################
# Next Phase:
##############################################################################################################################################################
# GameObject(object)
# MobileObject(GameObject)
# NonMobileObject(GameObject)
# NPC(MobileObject)
# PC(MobileObject)
# NonCollectable(NonMobileObject)
# Collectable(NonMobileObject)
# Usable(Collectable)
# Equippable(Collectable)
