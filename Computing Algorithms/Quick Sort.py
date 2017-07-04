
lt = [5,4,3,2,1]

sortz = 0
while sortz<len(lt):
        marked = lt[sortz]
        print(lt)
        for i in range(sortz,len(lt)):
                if lt[i] < marked:
                        tp = [lt[i]]
                        lt = lt[:sortz+1]+ tp  + lt[sortz+1:i] + lt[i+1:]      
        sortz+=1
        
                        
