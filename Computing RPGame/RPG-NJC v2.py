


#       NJC Text Based RPG
        #ThisIsAComment

class GameMap():

        _area_file = "Areas.txt"
        # information corresponding to each area is stored on 1 line in the format:
        #       <area_id> ; <area_name> ; <area_desc> ;
        #       <link 1, link 2, ... link n> ; <link 1 name, link 2 name, ... link n name>
        
        _links_file = "Links.txt"
        # information corresponding to each link is stored on 1 line in the format:
        #       <origin_area_id> ; <destination_area_id>

        def __init__(self):
                self._areas = []
                self._next_area_id = 1
        
                #loading areas from file
                load_area = open(self._area_file)
                for line in load_area:
                        area_info = line.split(";")
                        try:
                                if int(area_info[0]) > self._next_area_id:
                                        self._next_area_id = int(area_info[0]) + 1
                        
                                self._areas.append(GameArea(int(area_info[0]),area_info[1],area_info[2]))
                                _links = area_info[3].strip().split(",")
                                _link_names = area_info[4].strip().split(",")
                                for i in range(len(_links)):
                                        self._areas[-1].add_link(int(_links[i]),_link_names[i])
                                

                        except:
                                print("Failed to load area:  " + line)
                load_area.close()

        def show_areas(self):
                print(self._areas)



class GameArea():

        def __init__(self,new_id,new_name,new_desc):
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

        def add_link(self,new_id,new_link_name):
                self._links.append(new_id)
                self._link_names.append(new_link_name)
        
                        

        
x = GameMap()



import time

def TheGame():
      intro()

      x._area_index = 0
      print("     You begin your journey in the "+x._areas[x._area_index]._name+"...")
      time.sleep(2)

      no_events = True
      while no_events:
        stage()

        
def stage():
        print("\n"*50)
        print(x._areas[x._area_index]._name.upper())
        print("")
        print(x._areas[x._area_index]._desc)
        time.sleep(1)
        print("")
        print("")
        print("")
        print("You may choose to go to the following location(s):")
        time.sleep(1)
        for i in x._areas[x._area_index]._link_names:
            print ("\t" + ">>" + i, end="\n")
            time.sleep(0.65)
        print("")
        print("")
        where_to = input("I want to go to the ")
        if where_to in x._areas[x._area_index]._link_names:
            x._area_index = x._areas[x._area_index]._links[x._areas[x._area_index]._link_names.index(where_to)]
        print(x._area_index)


def intro():
        print("")
        print("")
        print("###########################################################################")
        print("#                    WELCOME TO THE NJC TEXT-BASED RPG                    #")
        print("###########################################################################")
        print("")
        time.sleep(1.5)
        print("                      Loading",end="")
        time.sleep(0.5)
        print(".",end="")
        time.sleep(0.5)
        print(".",end="")
        time.sleep(0.5)
        print(".",end="")
        time.sleep(2)
        print("  Completed!")
        time.sleep(1.5)
        print("")
        print("")
        print("###########################################################################")
        time.sleep(0.25)
        print("")
        time.sleep(0.25)
        print("                       Press any key to continue ")
        time.sleep(0.25)
        print("")
        print("###########################################################################")        
        WOW = input("")
        print("\n"*50)
        
        
        
        

TheGame()
        
        
