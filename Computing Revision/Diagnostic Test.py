

my_list = [5,3,1,2,4]
key = 2

def linear_search(my_list,key):
      for i in range(len(my_list)-1):
            if my_list[i] == key:
                  return i
      return None

def binary_search(my_list,key):
      key_found = False
      remainder = 0
      while not key_found:
            midindex = len(my_list)//2
            middle = my_list[midindex]
            print(midindex,remainder)
            if key == middle:
                  return midindex + remainder
            if len(my_list) == 1:
                  print('None')
                  return None
            if key > middle:
                  my_list = my_list[midindex+1:]
                  remainder += midindex
            elif key < middle:
                  my_list = my_list[:midindex]
            
def bubble_sort(my_list):
      not_swapped = False
      while not not_swapped:
            not_swapped = True
            for i in range(len(my_list)-1):
                  for e in range(len(my_list)-i-1):
                        if my_list[e] > my_list[e+1]:
                                    my_list[e],my_list[e+1]=my_list[e+1],my_list[e]
                                    not_swapped = False
      return my_list

def insertion_sort(my_list):
      for i in range(1,len(my_list)):
            checkers_index = i-1
            print(my_list,my_list[i],my_list[checkers_index])
            while my_list[i] < my_list[checkers_index] and i>0:
                  my_list[i],my_list[checkers_index]=my_list[checkers_index],my_list[i]
                  print(my_list,my_list[i],my_list[checkers_index],'<swap')
                  i -= 1
                  checkers_index -= 1
      return my_list

def quick_sort(my_list):
      if len(my_list) < 2:
            return my_list
      pivot = my_list[0]
      more = []
      less = []
      for i in range(1,len(my_list)):
            if my_list[i] >= pivot:
                  more.append(my_list[i])
            if my_list[i] < pivot:
                  less.append(my_list[i])
      return quick_sort(more) + [pivot] + quick_sort(less)

def base_n_to_denary(base_n_value,n):
      negative = False
      if base_n_value[0] == '-':
            negative = True
            base_n_value = base_n_value[1:]
      if base_n_value == '0':
            return 0

      base16 = '0123456789abcdef'
      denary = 0
      base_n_value = base_n_value[::-1]

      for i in range(len(base_n_value)):
            denary += base16.index(base_n_value[i]) * ( n ** i)

      return denary
      
def denary_to_base_n(denary_value,n):
      base16 = '0123456789abcdef'
      final = ''
      while denary_value>0:
            final = base16[ denary_value % n ] + final
            denary_value = denary_value // n
      return final










