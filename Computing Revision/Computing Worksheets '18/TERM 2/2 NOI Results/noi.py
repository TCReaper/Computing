

# rank schools based on medals

f = open('NOI2018results.txt')
schools = []

def calculate(f):
      global schools

      for line in f:
            line = line.strip()
            #print(line)
            try:
                  int(line[0])
            except ValueError:
                  if line == 'Gold':
                        #print('gold'*10)
                        gold = True
                  if line == 'Silver':
                        #print('silver'*10)
                        silver = True
                        gold = False
                  if line == 'Bronze':
                        #print('bronze'*10)
                        bronze = True
                        silver = False
                  if line == 'Honorable Mention':
                        #print('mention'*10)
                        mention = True
                        bronze = False
            else:
                  line = line.split('.',1)[1]
                  #print(line)
                  line = line[::-1].split(',',1)
                  final = []
                  for i in line:
                        i = i[::-1]
                        final.append(i.upper())
                  final = final[0].split(' ',1)[1]
                  #print(final)
                  
                  school_exists = False
                  index = 0
                  
                  for i in schools:
                        if final in i:
                              index = schools.index(i)
                              school_exists = True
                              
                  if not school_exists:
                        schools.append( [final, 0, 0, 0, 0] )
                        index = schools.index([final, 0, 0, 0, 0])
                  
                  if gold:
                        schools[index][1] += 1
                  elif silver:
                        schools[index][2] += 1
                  elif bronze:
                        schools[index][3] += 1
                  elif mention:
                        schools[index][4] += 1

                  #print(schools[index])
      f.close()        
      #print('|'*80)
      #** NAME_OF_THE_SCHOOL_LALALALALALALALALALALALALALALAL | G:**  S:**  B:**  HM:**

      #for i in schools:
            #print('{0:54}{1:5}{2:5}{3:5}{4:5}'.format(i[0],i[1],i[2],i[3],i[4]))


      for e in range(len(schools)):  # get max n times, each time excl. last max in A
            for i in range(len(schools)-e-1):
                  if schools[i][1] < schools[i+1][1]:
                        # Switch current index with next index, vice versa
                        schools[i] , schools[i+1] = schools[i+1] , schools[i]
                        
                  elif schools[i][1] == schools[i+1][1]:
                              if schools[i][2] < schools[i+1][2]:
                                    schools[i] , schools[i+1] = schools[i+1] , schools[i]
                                    
                              elif schools[i][2] == schools[i+1][2]:
                                    if schools[i][3] < schools[i+1][3]:
                                          schools[i] , schools[i+1] = schools[i+1] , schools[i]
                                          
                                    elif schools[i][3] == schools[i+1][3]:
                                          if schools[i][4] < schools[i+1][4]:
                                                schools[i] , schools[i+1] = schools[i+1] , schools[i]
                                                
                                          elif schools[i][4] == schools[i+1][4]:
                                                if schools[i][0] > schools[i+1][0]:
                                                      schools[i] , schools[i+1] = schools[i+1] , schools[i]
                                                      
                                    

def printer():
      global schools
      print('|'*80)
      print('{5:<7}{0:54}{1:5}{2:5}{3:5}{4:5}'.format('Name','Gld','Slvr','Brnz','HM','Rank'))
      for i in schools:
            print('{5:<7}{0:54}{1:<5}{2:<5}{3:<5}{4:<5}'.format(i[0],i[1],i[2],i[3],i[4],schools.index(i)+1))


for year in range(6,19):
      print('|'*80)
      print('NOI20'+str(year).zfill(2))
      #print('|'*80)
      handle = 'NOI20'+str(year).zfill(2)+'results.txt'
      f = open(handle)
      calculate(f)
printer()

















