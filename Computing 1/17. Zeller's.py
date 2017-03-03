

#       Zeller's Algorithm


b = int(input("Day Born?    "))
a = int(input("Month Born?    "))
e = int(input("Year Born?    "))
c = int(str(e)[2:])
d = int(str(e)[:2])

w = ( 13 * a - 1) / 5
x = c / 4
y = d / 4
z = w + x + y + b + c - 2*d
r = z%7

print(r)        #why doesn't it work
