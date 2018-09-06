
import random
import math

def generator(n,n_range):
      n_dict = {}
      for i in range(n):
            rand_int = random.randint(1,n_range)
            if search_dict(n_dict,rand_int):
                  n_dict[rand_int] += 1
            else:
                  n_dict[rand_int] = 1

      print('{0:<9}{1}'.format('Integer','Frequency'))
      for i in range(1,n_range+1):
            print('{0:<9}{1}'.format(str(i)+':',n_dict[i]))

def search_dict(dictionary,key):
      for e in dictionary.keys():
            if key == e:
                  return True
      return False
      
generator(1000,20)

def generator_plus(n,n_range):
      expect = n // n_range
      print('Expected frequency for each integer is '+str(expect))
      n_dict = {}
      for i in range(n):
            rand_int = random.randint(1,n_range)
            if search_dict(n_dict,rand_int):
                  n_dict[rand_int] += 1
            else:
                  n_dict[rand_int] = 1
                  
      print('{0:<9}{1:<11}{2}'.format('Integer','Frequency','Deviation'))
      for i in range(1,n_range+1):
            print('{0:<9}{1:<11}{2}'.format(str(i)+':',n_dict[i],
                                     abs(n_dict[i]-expect)))

      return n_dict

generator_plus(1000,20)
