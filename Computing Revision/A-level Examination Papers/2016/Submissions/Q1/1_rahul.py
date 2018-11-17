import random

freq = [0 for i in range(20)]

expected_freq = 1000 // 20

for i in range(1000):
    ind = random.randint(1, 20)
    freq[ind-1] += 1

print('Expected frequency: ', expected_freq)
print('{:<15}{:<15}{:<15}'.format('Integer', 'Frequency', 'Difference'))
for i in range(len(freq)):
    print('{:<15}{:<15}{:<15}'.format(i+1, freq[i], \
                                            abs(freq[i]-expected_freq)))
