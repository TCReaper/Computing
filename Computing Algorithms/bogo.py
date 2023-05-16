import random

def bogo_sort(arr):
    x , sorted = 0 , False 
    # sort array increasing
    while not sorted:
        sorted = True
        random.shuffle(arr)
        #print(arr,x)
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]: # if wrong 
                sorted = False
                break
        x+=1
    return x

def bogo_check(size,n):
    # n is number of iterations
    # returns percentage of correct sorts
    arr = list(range(size))
    total = 0
    for i in range(n):
        total += bogo_sort(arr)
        print('on iteration {}, total at {}'.format(i+1,total))
    print('final percentage for size {} array: {} %'.format(size,simplify(100*n/total)))
    return 100*n/total

def simplify(txt):
    txt = str(txt)
    if 'e' in txt:
        txt = txt.split('e')
        return str(round(float(txt[0]),3))+' x 10^'+txt[1]
    else:
        if txt[0] == '0':
            ntxt = txt.split('.')[1]
            e = 1
            while ntxt[0] == '0':
                e+=1
                ntxt = ntxt[1:]
            txt = ntxt[0]+'.'+str(round(int(ntxt[1:5]),3))+' x10^-'+str(e)
        return txt

bogo = 1
while True:
    try:
        bogo_check(bogo,5)
        bogo += 1
    except KeyboardInterrupt:
        break


