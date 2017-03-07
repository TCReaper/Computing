# 2017 - Term 1 - SH1 Computing Practical Quiz
# Code for Q2

f = open("NUMBERS.txt", "r")
data = []
outputdata = []
freqdata = []
for i in f:
    length = len(i)
    killdex = int(length)-1
    data.append(i[:killdex])
# data is a list of all elements
for element in data:
    if element not in outputdata:
        outputdata.append(element)
for i in outputdata:
    freq = data.count(i)
    freqdata.append(freq)
length = len(freqdata)
step = 0
print("Number Frequency")
outputdata.sort()
while step<length:
    print(outputdata[step] + "      " + str(freqdata[step]))
    step += 1
