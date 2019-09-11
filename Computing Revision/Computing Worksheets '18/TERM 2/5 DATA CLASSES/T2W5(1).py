# 1(a)
file = open("DATA.TXT","r") 
import time
score = [] 
for line in file:
	#print(line[:len(line)])
	#time.sleep(1)
	score.append(line[:len(line)-1].split(',')) 
	score[len(score)-1]=score[len(score)-1][1:] 

def quicksort(l,r,sorting):
	i=l
	j=r
	mid = sorting[int((l+r)/2)]
	while i<j:
		while sorting[i]>mid:
			i += 1 
		while sorting[j]<mid:
			j -= 1 
		if i<j:
			temp = sorting[i] 
			sorting[i]=sorting[j]
			sorting[j]=temp 
			temp = index[i] 
			index[i]=index[j]
			index[j]=temp 
			i += 1
			j -= 1 
		if l<j:
			quicksort(l,j-1,sorting) 
			quicksort(i+1,r,sorting) 
	return sorting 

def quicksort_helper(k,sorting):
	global index 
	index = []
	for i in range(len(sorting)):
		index.append(i) 
	sorting = quicksort(0, len(index)-1, sorting)
	if k==11:
		print("\nAverage") 
	else: 
		print("\nSubject"+str(k+1)) 
	print("\nTop 3 Students:") 
	for i in range(3):
		print("Student {:<10}{:>4}".format(index[i]+1,sorting[i])) 
	print("\nBottom 3 Students:") 
	for i in range(len(index)-3,len(index)):
		print("Student {:<10}{:>4}".format(index[i]+1,sorting[i])) 

for i in range(10):
	sorting = []
	for j in range(len(score)):
		sorting.append(int(score[j][i])) 
	quicksort_helper(i,sorting)  

summ=[] 
for i in range(len(score)):
	summ.append(0) 
	for j in range(10):
		summ[i] += int(score[i][j]) 
	summ[i]=float(summ[i]/10) 
quicksort_helper(11,summ) 

# 1(b) 
grade = [] 
count = []
for i in range(10):
	count.append([]) 
	for j in range(7):
		count[i].append(0) 

for i in range(len(score)):
	grade.append([]) 
	for j in range(10):
		current = int(score[i][j]) 
		if current >= 70:
			grade[i].append('A') 
			count[j][0] += 1
		elif current >= 60 and current < 70:
			grade[i].append('B') 
			count[j][1] += 1
		elif current >= 55 and current < 60:
			grade[i].append('C')
			count[j][2] += 1 
		elif current >= 50 and current < 55:
			grade[i].append('D')
			count[j][3] += 1 
		elif current >= 45 and current < 50:
			grade[i].append('E') 
			count[j][4] += 1
		elif current >= 40 and current < 45:
			grade[i].append('S')
			count[j][5] += 1
		else:
			grade[i].append('U') 
			count[j][6] += 1 

writefile = open("GRADES.TXT","w") 
for i in range(len(grade)):
	newline = str(i+1)
	for j in range(10):
		newline += ','+grade[i][j] 
	writefile.write(newline+"\n") 
writefile.close()

maxAB = 0 
maxIndex = 0 
for i in range(10):
	print("\nSubject "+str(i+1)) 
	print() 
	summ = 0 
	summAB = 0
	for j in range(7):
		summ+=count[i][j] 
		if j<2:
			summAB += count[i][j] 
		print("{:<5}{:<3}Students".format(chr(ord("A")+j),count[i][j])) 
	summAB = float(summAB/summ) 
	if maxAB < summAB:
		maxAB = summAB 
		maxIndex = i 
print("\nSubject {:<2} has the most As and Bs.".format(maxIndex)) 

