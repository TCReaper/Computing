
#ThisIsAComment

elec = open("ELECTIONS2017.TXT","r")
stats = []
for i in elec:
    i = i[:4] #appends voted president without the '\n'
    stats.append(i)
elec.close()
def sampling():
    samplez = int(input("Sample size:  "))
    temp = samplez
    if samplez==0 or samplez>len(stats)-1:
        print("Input valid sample size")
        sampling()
    else:
        return temp
        
sample = sampling()

import random

chosen_votes = []
chosen_vote_id = []

i=1
while i <= sample:
    index = random.randint(0,len(stats)-1)
    if index in chosen_vote_id:
        continue
    else:
        chosen_vote_id.append(index)
        chosen_votes.append(stats[index])
        i+=1

        

abcd = 0
wxyz = 0

for data in chosen_votes: #for every vote, check which president is voted
    if data == "ABCD":
        abcd += 1
    elif data == "WXYZ":
        wxyz += 1


per1 = int((abcd*100/sample*100000))
per2 = int((wxyz*100/sample*100000))

import math

round1 = str(math.ceil(int(str(per1)[2:5])/10)/1000)
round2 = str(math.ceil(int(str(per2)[2:5])/10)/100)

per1 = str(int(str(per1)[:2]) + float(round1))[:5]
per2 = str(int(str(per2)[:2]) + float(round2))[:5]

while len(per1) != 5:
    per1 += "0"
while len(per2) != 5:
    per2 += "0"

print("Sampled Votes:\t"+str(sample))
print("ABCD:\t\t"+per1+"%")
print("WXYZ:\t\t"+per2+"%")
president = ""
if float(per1)>float(per2):
    president += "ABCD"
else:
    president += "WXYZ"

print("Based on a random sample of "+str(sample)+", "+president+" would be elected")
