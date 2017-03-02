

# check for highest frequency
# in 4. Words.txt

f = open("4. Words.txt","r")
data = []
for i in f:
        length = len(i)
        remove = length - 1
        i = i[:remove]
        data.append(i)
f.close()

#seperating values
worddata = []
freqdata = []
for i in data:
        try:
                i = int(i)
                freqdata.append(i)
        except ValueError:
                worddata.append(i)

#getting max value
print(freqdata)
print(worddata)

high = max(freqdata)
print(high)

index = freqdata.index(high)
highword = worddata[index]

print("The word with the highest frequency of " + str(high) + " is " + highword)
