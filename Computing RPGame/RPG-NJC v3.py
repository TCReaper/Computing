


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
                self._player_id = ""
                self._editing_game = True
        
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
                                #print("Failed to load area:  " + line)
                                continue
                load_area.close()

        def show_areas(self):
                print("{0:<10}{1:<10}".format("LINK ID", "AREA NAME"))
                for i in self._areas:
                        print("{0:<10}{1:<10}".format(str(i.get_id()), str(i.get_name())))



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

        def set_name(self,new_name):
                self._name = new_name

        def set_desc(self,new_desc):
                self._desc = new_desc


        
        
        
                        


############################################################################################### GAME PLAYING ##############################################################################
        
x = GameMap()



import time
import random

def PlayGame():
        x._player_id = input("What's your name, traveller?  ")
        print("\n"*50)
        intro()
        TheGame()
        

def TheGame():
        logfile = open("LogFile.txt","w")
        logfile.close()
        x._area_index = random.randint(0,len(x._areas)-1)
        print("     You begin your journey in the "+x._areas[x._area_index]._name+"...")
        time.sleep(2)

        no_events = True
        while no_events:
                stage()

def EditGame():
        logfile = open("LogFile.txt","w")
        logfile.close()
        print("GAME EDIT MODE ACTIVATED")
        print("\n"*5)
        x._area_index = random.randint(0,len(x._areas)-1)
        print("     You begin your journey in the "+x._areas[x._area_index]._name+"...")
        time.sleep(2)
        x._editing_game = True
        while x._editing_game == True:
                editstage()
        savestage()
        intro()

def edit_area():
        print("\n"*5)
        print("#"*80,end="")
        print("\n"*5)
        print(x._areas[x._area_index]._name.upper())
        print("")
        print(x._areas[x._area_index]._desc)
        print("")
        option = 1
        for i in x._areas[x._area_index]._link_names:
            print ("\t" + str(option) + ": " + i, end="\n")
            option+=1
        print("\n"*5)
        print("#"*80,end="")
        print("\n"*5)
        print("Edit Name (1) or Description (2) or Save/Exit (3)")
        print("")
        wut_you_wan = input("    >> ")
        if wut_you_wan == "1":
                new_name = input("What is this area's new name?  ")
                x._areas[x._area_index].set_name(new_name)
        if wut_you_wan == "2":
                new_desc = input("What is this area's new description?  ")
                x._areas[x._area_index].set_desc(new_desc)
        if wut_you_wan == "3":
                savestage()
                editstage()
        edit_area()
        
def editstage():
        print("\n"*5)
        print("#"*80,end="")
        print("\n"*5)
        print(x._areas[x._area_index]._name.upper())
        print("")
        print(x._areas[x._area_index]._desc)
        print("")
        
        print("")
        option = 1
        for i in x._areas[x._area_index]._link_names:
            print ("\t" + str(option) + ": " + i, end="\n")
            option+=1
        print("")
        print("")
        print("")
        print("Move / Edit / Quit Edit")
        print(" 1   /  2   /    3")
        menu_choice = input("What dyu want? ")
        
        if menu_choice == "1":
                where_to = input("Destination Option Please: ")
                nextstagefunction(where_to,option)
        if menu_choice == "2":
                edit_area()
        if menu_choice == "3":
                print("check")
                x._editing_game = False



def savestage():
        saving = open("Areas.txt","w")
        saving.close()
        for i in x._areas:
                saving = open("Areas.txt","a")
                line = str(i._id)+";"+i._name+";"+i._desc+";"+str(i._links)+";"+str(i._link_names)+"\n"
                saving.write(line)
                

def stage():
        print("\n"*5)
        print("#"*80,end="")
        print("\n"*5)
        print(x._areas[x._area_index]._name.upper())
        print("")
        print(x._areas[x._area_index]._desc)
        time.sleep(1)
        print("")
        print("")
        print("")
        print("You may choose to go to the following location(s):")
        time.sleep(1)
        option = 1
        for i in x._areas[x._area_index]._link_names:
            print ("\t" + str(option) + ": " + i, end="\n")
            option+=1
            time.sleep(0.15)
        print("")
        print("")
        time.sleep(0.3)
        where_to = input("Area Option Selected >> ")
        nextstagefunction(where_to,option)

def nextstagefunction(where_to,option):
        try:
                where_to = int(where_to)
                if int(where_to) > option-1:
                        print("Choose A Valid Option.")
                        time.sleep(2)
                        stage()
        except ValueError:
                print("Choose A Valid Option.")
                time.sleep(2)
                stage()
        else:
                destination = x._areas[x._area_index]._link_names[where_to - 1]
                logs(destination)
                currentArea = x._areas[x._area_index]
                x._area_index = currentArea._links[currentArea._link_names.index(destination)]
                


def intro():
        print("\n"*50)
        print("###########################################################################")
        print("#                    WELCOME TO THE NJC TEXT-BASED RPG                    #")
        print("###########################################################################")
        print("#                                                                         #")
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
        print("#                                                                         #")
        print("#                                                                         #")
        print("###########################################################################")
        time.sleep(0.25)
        print("#                                                                         #")
        time.sleep(0.25)
        print("#                     1: Play Game                                        #")
        print("#                     2: Edit Game                                        #")
        print("#                     3: Quit Game                                        #")
        time.sleep(0.25)
        print("#                                                                         #")
        print("###########################################################################")
        print("")
        WOW = input("                   >> ")
        if WOW == "1":
                print("\n"*50)
                TheGame()
        if WOW == "2":
                print("\n"*50)
                EditGame()

def logs(destination):
        logfile = open("LogFile.txt","a")
        logfile.write(x._player_id.upper() + " moves from "+str(x._areas[x._area_index]._name)+" to "+str(x._areas[x._areas[x._area_index]._links[x._areas[x._area_index]._link_names.index(destination)]]._name)+"\n")

print("start game with PlayGame()")
        
        
