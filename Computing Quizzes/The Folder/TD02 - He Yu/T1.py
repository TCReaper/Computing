# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 1

import random

def subtraction_exercise(name):
    total_correct=0
    for i in range(1,11):
        y=2
        x=1
        while(y>x):
            x=random.randint(1,100)     
            y=random.randint(1,100)
        output="Q"+str(i)+") What is: "+str(x)+"-"+str(y)+" equal to? "
        EnterAns=False
        while not EnterAns:
            try:
                ans=int(input(output))
            except ValueError:
                print("Illegal value; please enter a number!")
            else:
                EnterAns=True
            if ans<0:
                print("Illegal value; please enter a positive integer.")
                EnterAns=False
        if ans==x-y:
            response="Correct! "
            total_correct=total_correct+1
        else:
            response="Incorrect. "
        response=response+str(x)+" - "+str(y)+" = "+str(x-y)
        print(response)
        print("\n")
    feedback1=name+", your score final score is: "+str(total_correct)+"/ 10"
    percentage=total_correct/10
    if percentage>=0.9:
        grade="A+"
    elif percentage>=0.75:
        grade="A"
    elif percentage>=0.7:
        grade="B+"
    elif percentage>=0.65:
        grade="B"
    elif percentage>=0.6:
        grade="C+"
    elif percentage>=0.55:
        grade="C"
    elif percentage>=0.5:
        grade="D"
    else:
        grade="U"
    feedback2="Your grade is: "+grade
    print(feedback1)
    print(feedback2)
    print("\n")
    
"""
EnterName=False
while not EnterName:
    try:
        name=input("Please enter your name: ")
        x=name.upper()
        print (x)
    except ValueError:
        print("Illegal name; must only include letters and/or space")
    else:
        EnterName=True
"""
EnterName=False
while not EnterName:
    name=input("Please enter your name: ")
    check=True
    for i in range(0,len(name)):
        try:
            x=int(name[i])
        except ValueError:
            continue
        else:
            print("Illegal name; must only include letters and/or space")
            check=False
            break
    if check:
        EnterName=True

print("\n")
stop_game=False
while not stop_game:
    subtraction_exercise(name)
    print("Please selection an option:")
    print("1: Play another round")
    print("2: Quit")
    EnterSelection=False
    while not EnterSelection:
        try:
            n=int(input())
        except ValueError:
            print("Invalid input. Please enter either \"1\" or \"2\".")
        else:
            EnterSelection=True
    if n==1:
        print("\n")
        continue
    elif n==2:
        stop_game=True

    


    
    
