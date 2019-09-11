# 2017 - Term 1 - SH2 Computing Practical Lecture Test
# Code for Task 1
import random

def application():
      # get username
      namecheck = True
      while namecheck:
        name = input("What's your name:    ")
        try:
            name = int(name)
        except ValueError:
            namecheck = False
        else:
            print("")
            print("Illegal name; must only include letters/spaces")
            continue

      questions = 1
      correct = 0
      while questions != 11:
        x = random.randint(1,101)
        y = random.randint(1,100)
        if y <= x:
            #p
            ans = x-y
            title = "Q" + str(questions) + ")  What is: "
            title2 = " equal to?  "
            n = input(title + str(x) + " - " + str(y) + title2)
            try:
                n = int(n)
                if n == ans:
                    print("Correct!")
                    correct += 1
                    questions += 1
                else:
                    print("Incorrect! "+str(x)+" - "+str(y)+" = "+str(ans))
                    questions += 1
            except ValueError:
                ans = x-y
                title = "Q" + str(questions) + ")  What is: "
                title2 = " equal to?  "
                n = input(title + str(x) + " - " + str(y) + title2)
                try:
                    n = int(n)
                    if n == ans:
                        print("Correct!")
                        correct += 1
                        questions += 1
                    else:
                        print("Incorrect! "+str(x)+" - "+str(y)+" = "+str(ans))
                        questions += 1
                except ValueError:
                    print("Illegal value; Please only input numbers")
                    continue
            
        elif x <= y:
            continue

      index = correct
      gradelist = [" U"," U"," U"," U"," U"," D"," C+"," B+"," A"," A+","A+"]
      grade = gradelist[index]

      print( name + ", your final score is " + str(correct) + " / 10")
      print( "Your grade is:" + grade)
      application()
      continueplaying = True
      while continueplaying:
            print("")
            print("Select an option!")
            print("1) Play again")
            print("2) Quit")
            n = input("")
            try:
              n = int(n)
              if n == 1:
                  application()
              elif n == 2:
                  print("Goodbye!")
                  continueplaying = False
              else:
                  print("Invalid input; Only enter \"1\" or \"2\".")
                  print("")
            except ValueError:
              print("Invalid input; Only enter \"1\" or \"2\".")
              print("")


