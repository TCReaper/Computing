# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 1
from random import random

#ASKING FOR PLAYER NAME ============================================
name_p = str(input("Please enter your name:"))
name_p = name_p.strip()
while True:
    try:
        name_p = int(name_p)
        print("Illegal name; Please only use letters and/or spaces")
        name_p = str(input("Please enter your name:"))
    except ValueError:
        #print("\n")
        break
def quiz():
    #QUIZZING=====================================================================
    no_qns = 0
    score = 0
    while no_qns != 10:
        no_qns += 1
        while True:
            t1 = int((random())*100)
            t2 = int((random())*100)
            if t2 < t1:
                break
            else:
                pass
        ans_c = t1 - t2
        while True:
            try:
                ans = int(input("Q" + str(no_qns) + ") What is " + str(t1) + " - " + str(t2)+ " equals to:"))
                break
            except ValueError:
                print("Please enter a positive integer as your answer\n")

        
        if ans == ans_c:
            print("Correct!", end = "")
            score += 1
        else:
            print("Incorrect!", end = "")

        print(str(t1) + " - " + str(t2) + " = " + str(ans_c) + "\n\n")


    #RESULTS & SCORES========================================================================

    print(name_p + ", your final score is: " + str(score) + " / 10")

    grade = {1:"U",2:"U", 3:"U", 4:"U", 5:"D", 6:"C+", 7:"B+", 8:"A", 9:"A+", 10:"A+"}
    print("Your grade is " + grade[score]+ "\n")


    #RETRY & QUIT=====================================================================

    print("Please select an option:")

    while True:
        try:
            user_opt = int(input("1: Play another round\n2: Quit\n"))
            if user_opt == 1 or user_opt == 2:
                break
            else:
                print("Please enter either a \"1\" or \"2\".")
        except ValueError:
            print("Invalid input, please select either \"1\" or \"2\".")

    if user_opt == 2:
        exit()
    elif user_opt == 1:
        print("Sure! Let's start from the top!")
        quiz()
quiz()
