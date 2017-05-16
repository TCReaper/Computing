


# jane's traffic light


import time
traffic = True
while traffic:
      print("The traffic light is red.")
      print("\n"*2)
      button_push = input("Press <Enter> to click traffic light button :P  \n")
      time.sleep(3)
      for i in range(11):
            print("beep")
            time.sleep(1)
      print("The traffic light is orange.")
      time.sleep(1.5)
      print("The cars slow down.")
      time.sleep(1.5)
      print("The traffic light is green.")
      time.sleep(2)
      print("A minute passes.")
      time.sleep(2)
      print("\n"*2)
