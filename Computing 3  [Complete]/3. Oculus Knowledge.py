


# read iris.data text file and print


oculus = open("3. iris-data.txt", "r")
data = []
for line in oculus:
        data.append(line)
for i in data:
        print(i)

