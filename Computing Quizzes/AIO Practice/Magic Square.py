
#     A I O
#     Magic Square

# abc
# def
# ghi

input_file = open('magicin.txt','r')

# input_file = '2 5 7'    #for testing

for i in input_file:
      text = i.split(' ')
a = int(text[0])
b = int(text[1])
d = int(text[2])

input_file.close()

solved = False
c = 1
e = 1
while not solved:
      summed = a + b + c      #get total sum
      while True:
            if e > summed - d - 1: #check if e is too high
                  c += 1
                  break
            g = summed - a - d
            if g < 1:   #check if g is positive
                  c += 1
                  break
            else:
                  while True:
                        f = summed - d - e
                        if f < 1:   #check if f is positive
                              e += 1
                              break
                        else:
                              #get values for h and i
                              h = summed - b - e
                              i = summed - c - f
                              if g + h + i == summed:
                                    #print( [a,b,c,d,e,f,g,h,i] )
                                    solved = True
                                    break
                              else:
                                    e += 1
                                    break
                  break
                              

output_file = open('magicout.txt','w')
output_file.write( str(a)+' '+str(b)+' '+str(c)+'\n'
                  +str(d)+' '+str(e)+' '+str(f)+'\n'+
                  str(g)+' '+ str(h)+' '+str(i) )

output_file.close()




















                              
                              
                  
      


