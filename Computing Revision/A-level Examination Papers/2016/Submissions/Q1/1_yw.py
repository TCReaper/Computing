from random import randint
data = {}
for i in range(1000):
    temp = randint(1,20)
    if temp not in data:
        data[temp] = 1
    else:
        data[temp] +=1

print('{:>5}{:>10}'.format('Integer', 'Frequency'))
for j in range(1,21):
    to_print = str(j) + ':'
    print('{:<5}{:>10}'.format(to_print, str(data[j])))

#1.2
def frequency_difference(frequency):
    expected_frequency = 1000/20
    difference = frequency - expected_frequency
    if difference < 0:
        difference = -difference
    return difference

print('{:>5}{:>10}{:>15}'.format('Integer', 'Frequency', 'Difference'))
for k in range(1,21):
    to_print = str(j) + ':'
    print('{:<5}{:>10}{:>15}'.format(to_print, str(data[k]), str(frequency_difference(data[k]))))
