
# 2017 - Term 1 - SH1 Computing Practical Quiz
# Code for Q3

f = open("INPUT.txt", "w")
f.close()

continute = True
while continute:
    n = input("Rational Number (or X to stop) :")
    if n.lower() == "x":
        continute = False
        break
    for i in n:
        if i not in ["1","2","3","4","5","6","7","8","9","0",".","-"]:
            print("That's not a rational number!")
            continue
        else:
            g = open("INPUT.txt", "a")
            g.write(n+"\n")
            g.close()
            
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
