
import random
import math

def num_gen(int_size,int_range):
      int_dict = {}
      for i in range(int_size):
            ran_int = random.randint(1,int_range)
            #print(int_dict)
            if ran_int in int_dict:
                  int_dict[ran_int] += 1
            else:
                  int_dict[ran_int] = 1
      #print(int_dict)
      print('Integer\tFrequency')
      for i in range(1,int_range+1):
            print(str(i)+':\t'+str(int_dict[i]))

def modded_num_gen(int_size,int_range):
      expect = int_size // int_range
      print('Expected frequency for each integer is '+str(expect))
      int_dict = {}
      for i in range(int_size):
            ran_int = random.randint(1,int_range)
            #print(int_dict)
            if ran_int in int_dict:
                  int_dict[ran_int] += 1
            else:
                  int_dict[ran_int] = 1
                  
      print('Integer\tFrequency\tDeviation')
      for i in range(1,int_range+1):
            print(str(i)+':\t'+str(int_dict[i])+'\t\t'+str(math.modf(int_dict[i]-expect)))


      #     "{}{}{}...".format(v1,v2,v3...)
      #     "{0:#^{3}} {} {}...".format(v1,v2,v3...)
