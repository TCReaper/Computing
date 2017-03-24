import time

lt = [3,4,2,1,5]

sortz = 0
while sortz<len(lt)+1:
        marked = lt[sortz]
        print(lt)
        for i in range(sortz+1,len(lt)):
                if lt[i] < marked:
                        tp = [lt[i]]
                        lt = lt[:sortz+1]+ tp  + lt[sortz+1:i] + lt[i+1:]
                        

                        
        sortz+=1
        
                        
