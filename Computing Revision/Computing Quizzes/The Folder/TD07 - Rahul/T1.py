# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 1
#GIDIJALA SAI RAHUL
import random

def get_num():
    while True:
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        if y <= x:
            return (x, y)
            break

def get_name():
    while True:
        name = input("Enter your name: ")
        is_legal = True
        for word in name.split():
            try:
                check_legal(name)
            except:
                is_legal  = False
                print("Illegal name. Only letters and spaces are allowed")
                break
            else:
                pass
        if is_legal:
            return name

def check_legal(name):
    if name.isalpha():
        pass
    else:
        raise ValueError

def evaluation(correct):
    percent = correct/10

    if percent < 0.5:
        return "U"
    elif percent < 0.55:
        return "D"
    elif percent < 0.6:
        return "C"
    elif percent < 0.65:
        return "C+"
    elif percent < 0.7:
        return "B"
    elif percent < 0.75:
        return "B+"
    elif percent < 0.9:
        return "A"
    else:
        return "A+"

def questions(name):
    correct = 0
    for num in range(1, 11):
        x, y = get_num()
        ans = get_input("Q" + str(num) + ") What is: " + str(x) + " - " + str(y) + " equal to?")
        if ans == (x-y):
            print("Correct! " + str(x) + " - " + str(y) + " = " + str(x-y))
            correct += 1
        else:
            print("Incorrect! " + str(x) + " - " + str(y) + " = " + str(x-y))

    print(name + ", your final score is: " + str(correct) + "/10")
    return correct

def last_step():
    print("Please select an option:")
    print("1: Play another round")
    print("2: Quit")

    while True:
        string = input()
        try:
            int(string)
        except:
            print("Please enter a valid input (1 or 2)")
        else:
            if int(string) == 1:
                return True
                break
            elif int(string) == 2:
                return False
                break
            else:
                print("Please enter a valid input (1 or 2)")

def get_input(prompt):
    while True:
        num = input(prompt)
        try:
            num = int(num)
            return num
            break
        except:
            print("Please enter a number")

keep_going = True

while keep_going:
    name = get_name()
    correct = questions(name)
    grade = evaluation(correct)
    print("Your grade is: " + grade)
    keep_going = last_step()
