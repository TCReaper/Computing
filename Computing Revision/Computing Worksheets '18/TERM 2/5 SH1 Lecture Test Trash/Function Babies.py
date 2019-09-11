
def iterative(my_list):
      for i in my_list:
            print(i,end=' ')
      print()

def recursive(s):
      if len(s)>1:
            output = s[-1] + recursive(s[:-1])
      else:
            output = s
      return output
        
def iterative2(n):
      roots = [i for i in range(1,n+1)]
      negroots = roots[::-1]

      for i in negroots:
            print('-'+str(i**2))
      print('0')
      for i in roots:
            print(i**2)

def recursive2(n):
      if n%2 == 1:
            n -= 1
      if n>0:
            lists = recursive2(n-2) + [ (n)]
      if n==0:
            return [0]
      return lists

#     ~      #     ~      #     ~      #     ~      #     ~      #

def insertion(my_list):
      for i in range(1,len(my_list)+1):
            while len(my_list) > i > 0 and my_list[i] < my_list[i-1]:
                  my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
                  i -= 1
      return my_list

def bin2hex(s):
      binary = [i for i in s][::-1]
      #print(binary)
      integer = 0
      for i in range(len(binary)):
            if binary[i] == '1':
                  integer += (2)**(i)
      hexa = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
      hexad = ''
      while integer > 1:
            remainder = integer % 16
            hexad = str(hexa[remainder]) + hexad
            integer = integer // 16
      return hexad

#     ~      #     ~      #     ~      #     ~      #     ~      #

def bsearcher(array,n):
      index = len(array)//2
      mid = index
      while True:
            print(mid)
            if n == array[mid][1]:
                  return index
            elif len(array) == 1:
                  return -1
            elif n < array[mid][1]:
                  array = array[mid:]
                  mid = len(array)//2
                  index = index + mid
            elif n > array[mid][1]:
                  array = array[:mid]
                  mid = len(array)//2
                  index -= len(array)-mid 
            
      
def bmark_to_find():
      f = open('MARKS.TXT')
      marks = []
      for line in f:
            line = line.strip().split(',')
            marks.append( (int(line[0]),int(line[1])) )
      f.close()

      while True:
            try:
                  mark_to_find = int(input('who u want lmao [1 to 100]:  '))
                  if mark_to_find > 100 or mark_to_find < 1:
                        a = int('error')
            except ValueError:
                  print('Try using a real ID\n')
            else:
                  break
            
      index = bsearcher(marks,mark_to_find)
      if index == -1:
            print('No student found that attained the mark '+str(mark_to_find))
      else:
            print('Student '+str(marks[index][0])+' attained the mark '+str(mark_to_find))
      
#     ~      #     ~      #     ~      #     ~      #     ~      #

def get_input():
      choice = input('Select an option [1,2,3,5]: ')
      try:
            choice = int(choice)
            if choice not in [1,2,3,5]:
                  a = int('error')
      except ValueError:
            print('Select a legitimate option.')
      return choice
      
def jakes_menu():
      while True:
            menu = [None,'Load Data from File','Add New Entry','Save Data to File',\
                    'Display Top 3 Shots','Quit']
            for i in range(1,len(menu)):
                  print('{0}.{1:^3}'.format(i,menu[i]))
            choice = get_input()
            new_data = []
            if choice == 5:
                  return None
            elif choice == 1:
                  f = open('RANGE_DATA.TXT')
                  data = []
                  for line in f:
                        line = line.strip().split(',')
                        data.append(line)
                  f.close()
                  print('Data loaded from RANGE_DATA.txt')
                  
            elif choice == 2:
                  name = input('Shooter name: ')
                  x = input('X-Cood: ')
                  y = input('Y-Cood: ')
                  new_data.append( [name,x,y] )
                  print('New shot stored.')

            elif choice == 3:
                  f = open('RANGE_DATA.TXT','a')
                  for i in new_data:
                        line = ''
                        for e in i:
                              line +=str(e)+','
                        line = line[:-1]+'\n'
                        f.write(line)
                  new_data = []
                  print('Data has been stored')

            elif choice == 4:
                  sorted_data = qsort(data)
                  top = sorted_data[:3]
                  print('Top 3 Shots:')
                  print('{0:2}{1:28}{2}'.format('#','Shooter','Distance'))
                  for i in range(len(top)):
                        print('{0:2}{1:28}{2}'.format(i+1,top[i][0],round(float(top[i][1])**2+float(top[i][2])**2,6)))

def qsort(arr):
        if len(arr) <= 1:
                return arr
        else:
                #print(arr)
                return qsort([x for x in arr[1:] if (float(x[1])**2 + float(x[2])**2)< (float(arr[0][1])**2 + float(arr[0][2])**2)]) + [arr[0]] + \
                       qsort([x for x in arr[1:] if (float(x[1])**2 + float(x[2])**2)>=(float(arr[0][1])**2 + float(arr[0][2])**2)])
            
            









        
        
