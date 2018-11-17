

def readfile():

      file_handle = open('T1_gamescore.txt')
      data = []
      for line in file_handle:
            line = line.strip().split(':')
            player = line[0].split(',')
            acc_scores = line[1].split(',')
            player.append(int(acc_scores[0]))
            for i in range(1,len(acc_scores)):
                  player.append(int(acc_scores[i])-int(acc_scores[i-1]))
            data.append(player)
      return data
            
def count_class(clss):
      data = readfile()
      n = 0
      for i in range(len(data)):
            if data[i][1] == clss:
                  n += 1
      return n

for clss in ['warrior','mage','priest']:
      print('number of {0}: {1}'.format(clss,count_class(clss)))

def top_class_by_season(season):
      data = readfile()
      classes = []
      for i in range(len(data)):
            clss = data[i][1]
            season_score = data[i][1+season]
            
            if len(classes) == 0:
                  classes.append([clss,season_score,1])
            insert = False
            for i in range(len(classes)):
                  if clss == classes[i][0]:
                        classes[i][1] += season_score
                        classes[i][2] += 1
                        insert = True
            if not insert:
                  classes.append([clss,season_score,1])

      for i in range(len(classes)):
            classes[i][1] = classes[i][1] // classes[i][2]

      classes = b_sort(classes,1)
      return classes[0][0]

def b_sort(arr,sorted_index):
      for i in range(len(arr)):
            swap = False
            for j in range(len(arr)-1):
                  if arr[j][sorted_index] < arr[j+1][sorted_index]:
                        arr[j],arr[j+1] = arr[j+1],arr[j]
                        swap = True
            if not swap:
                  break
      return arr

for i in range(1,13):
      print('Top class in season {0}: {1}'.format(i,top_class_by_season(i)))

# i give ups


def top_n_players_by_season(n,season):
      data = readfile()
      data = b_sort(data,1+season)
      
      players = []
      for i in range(n):
            players.append(data[i][0])
      return players


def find_stagnant_players():
      data = readfile()
      stagnants = []
      for i in range(len(data)):
            player = data[i]
            #print(player)
            for x in range(2,len(player)):
                  if player[x] == 0:
                        stagnants.append(player[0])
                        break
      return stagnants

                  
































            
            
