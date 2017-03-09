


# count words

romeo = open("5. romeo.txt", "r+")

wordcount={}
punctuation = ["/","[","]",".",",",":",";","(",")","-","!","?"]

for word in romeo.read().split():
        lenword = len(word)
        for i in range(0,lenword):
                try:
                        if word[i] in punctuation:
                                word = word[:i] + word[i+1:]

                except:
                        lenword -= 1
                        try:
                                for i in range(0,lenword):
                                        if word[i] in punctuation:
                                                word = word[:i] + word[i+1:]
                        except:
                                lenword -= 1
                                try:
                                        for i in range(0,lenword):
                                                if word[i] in punctuation:
                                                        word = word[:i] + word[i+1:]
                                                else:
                                                        continue
                                except:
                                        continue

        word = word.lower()
        if word not in wordcount:
                wordcount[word] = 1
        else:
                wordcount[word] += 1
                
romeo.close()

text = open("5. Word Count.txt","w+")
for i in wordcount:
        text.write(i + ", " + str(wordcount[i]) + "\n")
        
