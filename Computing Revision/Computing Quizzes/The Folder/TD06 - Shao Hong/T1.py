# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Sze Shao Hong's Code for Task 1

from random import randint

name = ""
choice = ""
while choice == "":
    while name == "":
        name = input("Please enter your name: ")
        try:
            name = int(name)
            name = ""
            print("Illegal name; must only include letters and/or space")
        except:
            continue

    score = 0
    for drler in range(10):
        x = randint(1,100)
        y = randint(1,100)
        while y > x:
            y = randint(1,100)

        print("Q",drler+1,": What is ",x," - ",y,"?",sep="")
        while True:
            try:
                answer = int(input())
                break
            except:
                print("Illegal value; please enter a number!")
                print("Q",drler+1,": What is",x,"-",y,"?")

        if answer == x - y:
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is ",x-y,"!",sep="")
    print(name,", Your score is ",score," / 10",sep="")

    if score >= 9:
        grade = "A+"
    elif score >= 7.5:
        grade = "A"
    elif score >= 7:
        grade = "B+"
    elif score >= 6.5:
        grade = "C+"
    elif score >= 6:
        grade = "C"
    elif score >= 5.5:
        grade = "C"
    elif score >= 5:
        grade = "D"
    else:
        grade = "U"

    print("Your grade is:",grade)

    while choice == "":
        choice = input("Please enter an option: \n1: Play another round \n2: Quit\n")
        try:
            choice = int(choice)

            if choice == 1:
                continue
            elif choice == 2:
                break
            else:
                choice = ""
                print("Not a valid input. Please select either \"1\" or \"2\".")
        except:
            choice = ""
            print("Not a valid input. Please select either \"1\" or \"2\".")
    else:
        choice = ""
    
    


    


