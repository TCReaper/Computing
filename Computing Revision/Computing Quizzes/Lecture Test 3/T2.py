
#ThisIsAComment

read = False
student = []

def Menu(read,student):
    print("\n"*5)
    print("1. Read File Data\n2. Enter Additional Data\n3. Rank via merge sort\n4. End")
    option = input("\n>> ")
    incorrect = True
    while incorrect:
        if option not in ["1","2","3","4"]:
            print("Enter a valid option\n")
            Menu(read,student)
        else:
            incorrect = False

    if option == "1":
        if read == True:
            print("Not allowed.")
            Menu(read,student)
        else:
            RFD()
    if option == "2":
        if read == False:
            print("Not allowed.")
            Menu(read,student)
        AddData(student)
    if option == "3":
        if read == False:
            print("Not allowed.")
            Menu(read,student)
        Merge(student)
    if option == "4":
        print("End.")
    
def RFD():
    f = open("DATA.TXT","r")
    student = []
    for line in f:
        student.append(line.split())
    f.close()
    print("DATA HAS BEEN READ")
    read = True
    Menu(read,student)
    

def AddData(student):

    nric = input("Please input the Student NRIC: ")
    q1 = int(input("Please input the Quiz 1 Score (max 25): "))
    q2 = int(input("Please input the Quiz 2 Score (max 35): "))
    q3 = int(input("Please input the Quiz 3 Score (max 50): "))
    new_data = [nric,q1,q2,q3]
    student.append(new_data)
    
    f = open("DATA.TXT","a")
    data_line = ""
    for i in new_data:
        data_line += str(i) + " "
    f.write(str(data_line)+"\n")
    f.close()
    
    cont = input("Enter More Data? (Y/N)  ")
    if cont.lower() == "y":
        AddData(student)
    else:
        Menu(read,student)

def Merge(student):
    calculate(student)
    mergesort()

def calculate(student):
    student_score = []
    for i in student:
        percentage = ((20*(int(i[1])/25))+(30*(int(i[2])/35))+(50*(int(i[3])/50)))
        student_score.append(percentage)
def mergesort():
    print("ehhhhhhhhhhhhhhhh")



Menu(read,student)
