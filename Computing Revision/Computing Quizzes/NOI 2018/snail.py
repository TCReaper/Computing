

height_phases = raw_input().split()
routine = raw_input().split()

#height_phases = '50 3'.split()
#routine = '5 2 3'.split()

exit_height = int(height_phases[0])
phases = int(height_phases[1])
phase = 0
running = True
checking = True

check_possible = 0
check_s = 0
for i in routine:
      check_possible += int(i)
      check_s += int(i)
      if check_s < 0:
            check_s = 0
      if check_s >= exit_height:
            checking = False

if checking == True:
      if check_possible <= 0 and exit_height != 0:
            print('-1 -1')
            running = False

height =0
day = 0

while running:
      for motion in routine:
            height += int(motion)
            print(height)
            if height < 0:
                  height = 0
            if height >= exit_height:
                  print str(day)+' '+str(phase)
                  running = False
                  break

            phase += 1
            
      phase = 0
      day += 1
            
                  
