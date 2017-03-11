


# fixings

import random
name = ""
for i in range(100):
        name = name + str(random.randint(0,9))
name = "2. " + name + ".txt"
try:
        f = open(name, "r")
except FileNotFoundError:
        g = open(name, "w")
        g.close()
        f = open(name, "r")
else:
        data = f.read()
        f.close()
