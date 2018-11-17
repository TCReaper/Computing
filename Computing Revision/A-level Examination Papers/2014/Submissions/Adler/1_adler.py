def display_menu():
    print("\n+++++++++++++++++++++++"\
          "\n1.  Exact match"\
          "\n2.  Start of term"\
          "\n3.  Within term"\
          "\n++++++++++++++++++")

def get_choice():
    while True:
        choice = input("Choice ?")
        if choice == 'XXX':
            return choice
        if choice.isdigit():
            choice = int(choice)
            if choice in range(4):
                return choice
        print("Invalid input!"\
              " Please the number corresponding to your desired option.")
        
        


def read_file():
    f = open("JARGON.TXT")
    temp = f.read().split('\n')[:-1]
    f.close()
    return temp

def menu():
    contents = read_file()
    while True:
        display_menu()
        choice = get_choice()
        if choice == 'XXX':
            break
        term = input("Term?")
        result = []
        if choice == 1:
            for i in range(len(contents)):
                if contents[i] == term:
                    result.append(contents[i])
        elif choice == 2:
            for i in range(len(contents)):
                if contents[i][:len(term)] == term:
                    result.append(contents[i])
        elif choice == 3:
            for i in range(len(contents)):
                for j in range(len(contents)):
                    if contents[i][j: j + len(term)] == term and\
                       (not search(result, contents[i])):
                        result.append(contents[i])
        for i in result:
            print(i)
        print("There were " + str(len(result)) + " matching term(s)")

def search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return True
    return False


menu()

#29:29.19
