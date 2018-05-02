


def ls(arr,data):
      for i in range(len(arr)):
            if i == arr[i]:
                  return True
      return i

def bs(arr,data):
      index = len(arr)//2
      mid = len(arr)//2
      if len(arr) == 0:
            return -1
      while True:
            if data == arr[index]:
                  return index
            if mid == 1:
                  return -1
            elif data > arr[mid]:
                  index += mid//2
                  mid = mid//2
            else:
                  index -= mid//2
                  mid = mid//2   

def b_sort(arr):
      for i in range(len(arr)):
            for j in range(i,len(arr)):
                  if arr[i]>arr[j]:
                        arr[i],arr[j]=arr[j],arr[i]
                        
      return arr

arr = [1,3,5,4,2]

def i_sort(arr):
      for i in range(len(arr)-1):
            while i >= 0 and arr[i]>arr[i+1]:
                  arr[i],arr[i+1]=arr[i+1],arr[i]
                  i -= 1
      return arr

def qsort(arr):
      if len(arr) == 1:
            return arr
      else:
            return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + \
                       qsort([x for x in arr[1:] if x>=arr[0]])
