##from random import randint
##
##freq = {i:0 for i in range(1, 21)}
##for i in range(1000):
##    n = randint(1, 20)
##    freq[n] += 1
##
##def display(freq):
##    print("{:<20}{}".format("Integer", "Frequency"))
##    for key in freq:
##        print("{:<20}{}".format(str(key) + ":", str(freq[key])))
##        
##display(freq)
##


from random import randint
expected = int(1000/20)
freq = {i:[0, -expected] for i in range(1, 21)}
for i in range(1000):
    n = randint(1, 20)
    freq[n][0] += 1
    freq[n][1] += 1


def display(freq):
    print("{:<20}{:<20}{}".format("Integer", "Frequency", "Difference"))
    for key in freq:
        print("{:<20}{:<20}{}".format(str(key) + ":", \
                                str(freq[key][0]), str(freq[key][1])))
        
display(freq)

#Time Taken: 16.12.47
#Time Allowed: 17.33.00
