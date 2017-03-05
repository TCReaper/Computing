#
#       
#                       S I E V E 
#
#




##n = input(" Give a positive integer:    ")
##n = int(n)
##candidates = [ ]
##primes = [ ]
##i = 2
##
##while i <= n:
##        candidates.append(i)
##        i = i + 1

# you have candidate list [ ------------------------- ]

# add first prime to primes

n=input("Select the prime number you want (i.e., an interger): ")
n=int(n)
used=[]
for i in range(2,10010):
    used.append(True)
p=2
count=1
while count<n:
    for i in range(2,1000):
        if i*p<10000:
            used[i*p]=False
    p=p+1
    while used[p]==False:
        p=p+1
    count=count+1
print ("Prime number",n,":",p)
