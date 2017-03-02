


# count words


#.count()

romeo = open("5. romeo.txt", "r+")

wordcount={}

for word in romeo.read().split():
        word = word.lower()
        if word not in wordcount:
                wordcount[word] = 1
        else:
                wordcount[word] += 1

#print(wordcount)

text = open("5. Word Count.txt","w+")
for i in wordcount:
        text.write(i + ", " + str(wordcount[i]) + "\n")
        
