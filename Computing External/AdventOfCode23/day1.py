f = open('input.txt','r')
ans = 0
for line in f:
    line = line.strip()
    #print(line)
    line2 = line[::-1]
    string = ''
    for i in line:
        try:
            int(i)
        except Exception:
            pass
        else:
            string += str(i)
            break
            
    for i in line2:
        try:
            int(i)
        except Exception:
            pass
        else:
            string += str(i)
            break
        
    print(line,string)
    ans += int(string)
f.close()
print(ans)
