# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 1

def ask_qn():
    global correct
    global wrong
    import random
    qn = 0
    correct = 0
    wrong = 0
    for qn in range(0, 10):
        x = random.randint(1, 100)
        y = random.randint(1, x)
        answer = input("Q" + str(qn + 1) + ")" + "  What is: " + str(x) + " - " + str(y) + " equal to? ")
        try:
            int(answer) == x - y
        except:
               print("Incorrect! " + str(x) + " - " + str(y) + " = " + str(x-y))
               wrong += 1
        else:
            if int(answer) == x - y:
                print("Correct! " + str(x) + " - " + str(y) + " = " + str(x-y))
                correct += 1
            else:
                print("Incorrect! " + str(x) + " - " + str(y) + " = " + str(x-y))
                wrong += 1
        qn += 1
    print("")


    
def get_grades():
    global correct
    global wrong
    percentage = (correct / (correct + wrong)) * 100
    print(str(percentage) + "%")
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 65:
        grade = "B"
    elif percentage >= 60:
        grade = "C+"
    elif percentage >= 55:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "U"
    


run = True
while run == True:
    name = input("Please enter your name: ")
    
    ask_qn()
    get_grades()
    print(name + ", your final score is: " + str(correct) + "/" + str(correct + wrong))
    print("Your grade is: " + grade)

    trying = True
    while trying == True:
        print("Please select an option")
        print("1: Play another round")
        print("2: Quit")
        checkrun = input("")
        try:
            int(checkrun) == 2
        except ValueError:
            print('Invalid input. Please enter either "1" or "2".')
        else:
            trying = False


    if int(checkrun) == 2:
        run = False
