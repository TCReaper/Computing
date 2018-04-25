

def qsort(lt):
      sortz = 0
      while sortz<len(lt):
              marked = lt[sortz][1]
              #print(lt)
              for i in range(sortz,len(lt)):
                      if lt[i][1] > marked:
                            #print(lt[i][1], marked)
                            tp = [lt[i]]
                            lt = lt[:sortz+1]+ tp  + lt[sortz+1:i] + lt[i+1:]      
              sortz+=1
      print(lt)
      return lt

def qsort2(arr):
        if len(arr) <= 1:
                return arr
        else:
                print(arr)
                return qsort([x for x in arr[1:] if x[1]<arr[0][1]]) + [arr[0]] + qsort([x for x in arr[1:] if x[1]>=arr[0][1]])

def bub(listed):
      for e in range(len(listed)):
            swap = False
            for i in range(len(listed)-e-1):
                  if listed[i][1] < listed[i+1][1]:
                        #print(listed[i][1],listed[i+1][1])
                        listed[i] , listed[i+1] = listed[i+1] , listed[i]
                        swap = True
            if not swap:
                  break
      return listed

students = []
f = open('DATA.TXT')
for line in f:
      line = line.strip().split(',')
      line[0] = 'Student ' + line[0] #set student name
      for index in range(1,len(line)):
            line[index] = int(line[index]) #int scores
      students.append(line)
f.close()


#print subjects individual

for subject in range(1,11):
      sub = []
      for index in range(len(students)):
            sub.append([students[index][0],students[index][subject]])
      sub = bub(sub)

      print('\n\nSubject '+str(subject)+' #'*10+'\n\nTop 3 Students:')
      for i in sub[:3]:
            print("{0:15}{1}".format(i[0],i[1]))
      
      print('\nBottom 3 Students:')
      for i in sub[-3:]:
            print("{0:15}{1}".format(i[0],i[1]))

# subjects average
sub = []
for index in range(len(students)):
      average = 0
      for subject in range(1,11):
            average += students[index][subject]
      average = average // 10
      sub.append([students[index][0],average])
sub = bub(sub)

print('\n\nAVERAGES'+'\n\nTop 3 Students:')
for i in sub[:3]:
      print("{0:15}{1}".format(i[0],i[1]))

print('\nBottom 3 Students:')
for i in sub[-3:]:
      print("{0:15}{1}".format(i[0],i[1]))

##########################################################################333

sub_freq = [0,0,0,0,0,0,0,0,0,0]

for subject in range(1,11):
      grade_freq = {'A':0,'B':0,'C':0,'D':0,'E':0,'S':0,'U':0}
      for index in range(len(students)):
            student = students[index]
            score = student[subject]
            if score >= 70:
                  score = 'A'
                  grade_freq[score] += 1
                  sub_freq[subject-1] +=1
            elif score >= 60:
                  score = 'B'
                  grade_freq[score] += 1
                  sub_freq[subject-1] +=1
            elif score >= 55:
                  score = 'C'
                  grade_freq[score] += 1
            elif score >= 50:
                  score = 'D'
                  grade_freq[score] += 1
            elif score >= 45:
                  score = 'E'
                  grade_freq[score] += 1
            elif score >= 40:
                  score = 'S'
                  grade_freq[score] += 1
            else:
                  score = 'U'
                  grade_freq[score] += 1
            student[subject] = score
            
      print('\n\nSubject '+str(subject))
      for keys,values in grade_freq.items():
            print("{0:15}{1}".format(keys,str(values) +' Students'))
  
print('\n\nSubject '+str(sub_freq.index(max(sub_freq))+1)+' has the most As and Bs.')

f = open('GRADES.TXT','w')
for index in range(len(students)):
      student = students[index]
      line = str(index+1)
      for sub in range(1,11):
            line += ','+student[sub]
      f.write(line+'\n')
f.close()








