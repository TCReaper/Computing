

def binary_search(this_array, find_value, low, high): #returns INT

    if low > high: #A
        return -1 #not found
    else:
        #calculate new middle value
        middle = (low + high) // 2 #B
        if this_array[middle] > find_value:
            return binary_search(this_array, find_value, low, middle - 1)
        elif this_array[middle] < find_value:
            return binary_search(this_array, find_value, middle + 1, high) #C
        else:
            return middle

def initialise_animals():
    MyAnimal = [None for i in range(33)]
    MyAnimal[0]="aardvark"
    MyAnimal[1]="ant"
    MyAnimal[2]="antelope"
    MyAnimal[3]="bat"
    MyAnimal[4]="boa constrictor"
    MyAnimal[5]="camel"
    MyAnimal[6]="cat"
    MyAnimal[7]="cheetah"
    MyAnimal[8]="dog"
    MyAnimal[9]="donkey"
    MyAnimal[10]="duck"
    MyAnimal[11]="elephant"
    MyAnimal[12]="frog"
    MyAnimal[13]="giraffe"
    MyAnimal[14]="hare"
    MyAnimal[15]="horse"
    MyAnimal[16]="iguana"
    MyAnimal[17]="jackass"
    MyAnimal[18]="jaguar"
    MyAnimal[19]="leopard"
    MyAnimal[20]="lion"
    MyAnimal[21]="llama"
    MyAnimal[22]="mouse"
    MyAnimal[23]="ostrich"
    MyAnimal[24]="panther"
    MyAnimal[25]="parrot"
    MyAnimal[26]="rhinoceros"
    MyAnimal[27]="seahorse"
    MyAnimal[28]="seal"
    MyAnimal[29]="spider"
    MyAnimal[30]="turtle"
    MyAnimal[31]="whale"
    MyAnimal[32]="zebra"
    return MyAnimal

def find_animal():
    my_animal = initialise_animals()
    name = input("Animal name: ")
    index = binary_search(my_animal, name, 0, len(my_animal) - 1)
    if index == -1:
        print("Animal not found.")
    else:
        print("Animal found at index " + str(index))

##find_animal()
        
def binary_search_amended(this_array, find_value, low, high, calls = 0): 
    #returns INT

    if low > high: #A
        return -1, calls #not found
    else:
        #calculate new middle value
        middle = (low + high) // 2 #B
        if this_array[middle] > find_value:
            return binary_search_amended(this_array, find_value, low, \
                                         middle - 1, calls + 1)
        elif this_array[middle] < find_value:
            return binary_search_amended(this_array, find_value, middle + 1, \
                                 high, calls + 1) #C
        else:
            return middle, calls
        
def find_animal_amended():
    my_animal = initialise_animals()
    name = input("Animal name: ")
    index, calls = binary_search_amended(my_animal, name, 0, len(my_animal) - 1)
    if index == -1:
        print("Animal not found with " + str(calls) + " function calls")
    else:
        print("Animal found at index " + str(index) + " with " + str(calls)\
              + " function calls")

find_animal_amended()

#19:45.29
