import random

frequency_table = [0]*21
for i in range(1000):
    random_integer = random.randint(1,20)
    frequency_table[random_integer] += 1

expected_frequency = 1000/20
print("Expected Frequency:"+str(expected_frequency))

print("{:<10}{:<15}{:<30}".format("Integer","Frequency","Difference btw actual and expected frequency"))
for i in range(1, len(frequency_table)):
    print("{:<10}{:<15}{:<30}".format(str(i)+":",frequency_table[i], frequency_table[i]-expected_frequency))

    


    
