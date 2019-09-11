

# iay antway otay illkay yselfmay


import math

def decode():
##    file_name = input("Exact file name including \".txt\":   ")
    file_name = "ENCODED-FILE.TXT"
    f = open(file_name,"r")
    kms = []
    bases = []
    for i in f:
        bases.append(int(i[:2]))
        kms.append(i[3:len(i)-1])
    decoding(kms,bases)

def decoding(kms,bases):
    print(kms)
    print(bases)
    for i in range(len(kms)):
        cur_base = bases[i]
        cur_line = kms[i]
        cur_step_value = math.ceil(math.log(122,cur_base))

        step = 0
        printing = True
        while printing:

            element = cur_line[step:step+cur_step_value-1]
            step += cur_step_value -1 
            try:
                char = int(str(element),cur_base)
                print(chr(char),end="")
            except:
                printing = False
            







    
decode()
