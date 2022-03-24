a = input('') #amt of beams
ls = input('').split(' ') #arr of beams

for i in range(len(ls)):
    ls[i] = int(ls[i])

ls.sort()

total = 0
highest = ls[-1]
for i in ls:
    total += int(i)
maxx = total//2
print(maxx)
print(ls)

def isSubsetSum(arr, n, sum):
	if sum == 0:
		return True
	if n == 0 and sum != 0:
		return False

	if int(arr[n-1]) > sum:
		return isSubsetSum(arr, n-1, sum)

	return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])


def findPartion(arr, n):
	sum = 0
	for i in range(0, n):
		sum += int(arr[i])
	if sum % 2 != 0:
		return False
	return isSubsetSum(arr, n, sum // 2)

arr = ls
n = len(arr)

print(findPartion(arr, n))

