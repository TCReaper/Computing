# 2017 - Term 1 - SH1 Computing Practical Quiz
# Code for Q4




n = input('wth:  ')
lengthn = len(n)
indexlenn = lengthn - 1
indexn = 0

p = []
final = []

while indexn <= indexlenn:
        chosen = n[indexn]
        remainder = n[:indexn] + n[indexn + 1:]
        p.append([chosen,remainder])
        indexn += 1

for listed in p:
        indexn = 0
        while indexn < indexlenn :
                remainder = listed[1]
                choose = remainder[indexn]
                chosen = listed[0] + choose
                remainder = remainder[:indexn] + remainder[indexn+1:]
                final.append([chosen,remainder])
                indexn += 1

for i in final:
        for k in i:
                print(k,end="")
        print("")
