

#     Google Code Jam Problem B
#     The Computational Reaper

x = open("Output - Tidy Numbers.txt","w")
x.close()

m = open("B-small-attempt1.in","r")

data = []

for inputted in m:
      #data = data[:len(data)-1]
      data.append(inputted)

#Case #1: 129

cases = data[0]
data = data[1:]

x=1

for number in data:
      
      printed = False
      while not printed:
            correct = False
            if len(str(number)) == 2:
                        print("Case #"+str(x)+": "+str(number))
                        x+=1
                        printed = True
            while not printed:
                  for indice in range(len(str(number))-1):
                        #print("check: " + str(number)[indice] + " " + str(number)[indice+1])
                        
                        if str(number)[indice] > str(number)[indice+1]:
                              correct = False
                              number = int(number) - 1
                              break
                        if str(number)[indice] <= str(number)[indice+1]:
                              correct = True
                  if correct == True:
                        print("Case #"+str(x)+": "+str(number))
                        x+=1
                        printed = True
