import random
import time

def loading():
      print("")
      print("             ,__________________,")
      print("     Loading ",end="")
      for i in range(10):
            print("||",end="")
            time.sleep(random.uniform(0.33,1.33))
      print("")
