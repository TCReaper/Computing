a = input('') #amt of beams
arr = input('').split(' ') #arr of beams

for i in range(len(arr)):
    arr[i] = int(arr[i])

#arr = [i for i in arr if i != 0]

arr.sort()
total = sum(arr)
sol_not_found = True

def findMinRec(arr, i, sumCalculated,
			sumTotal):
	if (i == 0):
		return abs((sumTotal - sumCalculated) -
				sumCalculated),sumCalculated
	return min(findMinRec(arr, i - 1,
						sumCalculated+arr[i - 1],
						sumTotal),
			findMinRec(arr, i - 1,
						sumCalculated, sumTotal))

def findMin(arr, n):
	sumTotal = 0
	for i in range(n):
		sumTotal += arr[i]

	return findMinRec(arr, n,
					0, sumTotal)

save = arr[:]

ans = 0

while sol_not_found:
    n = len(arr)
    if n == 1:
        break
    sol = findMin(arr, n)
    if sol[0] == 0:
        sol_not_found = False
        ans = sol[1]
        break
    else:
        if sol[0] in arr:
            del(arr[arr.index(sol[0])])
        else:
            arr = arr[1:]

arr = save[::-1]

while sol_not_found:
    
    n = len(arr)
    if n == 1:
        break
    sol = findMin(arr, n)
    if sol[0] == 0:
        sol_not_found = False
        if sol[1] > ans:
            ans = sol[1]
        break
    else:
        if sol[0] in arr:
            del(arr[arr.index(sol[0])])
        else:
            arr = arr[1:]

print(ans)