from random import randint
name_input=input("Please enter your name: ")
validname="abcdefghijklmnopqrstuvwxyz"+" "
cont="T"

for i in name_input:
    try:
        if i in validname:
            continue

    except:
        if i not in validname:
            print("n")
    


n=2
def qn_generator(n):
    for e in range(1,n):
        score=0
        grade='x'
        for i in range(1,10):
            x=randint(1,100)
            y=randint(1,x)
            c=x-y
            answer=input("What is: "+str(x)+ '-'+str(y)+' equal to?')

            if answer==c:
                print("Correct!"+str(x)+ '-'+str(y)+'='+str(c) )
                score+=1

            else:
                print("Wrong.The correct answer is:"+str(c))

            

        print("Your score is:" + str(score)+'/10')
        percentage=(score/10)*100
        if percentage>=90:
            grade='A+'
        if percentage>=75:
            grade='A'

        if percentage>=70:
            grade='B+'

        if percentage>=65:
            grade='B'

        if percentage>=60:
            grade='C+'

        if percentage>=55:
            grade='C'

        if percentage>=50:
            grade='D'

        if percentage<50:
            grade="U"

        print("Your grade is:" + grade)


qn_generator(n)
option=input("Please select an option: "+'\n'+"1:Play another round"+'\n'+"2: Quit"+'\n' )

if option=='2':
    quit

else:
    qn_generator(n)
    
