import time

#       stopwatch

timer = True
seconds = 0
minutes = 0
while timer:
        for i in range(0,60):
                time.sleep(1)
                seconds = i
                print("Timer: \t {0} minutes and {1} seconds have passed since you left !".format(minutes,seconds))
        minutes += 1
        continue
