



############################################ TASK 1.1 ################################

import math

def vote_application(file):
      votes = open(file+'.txt','r')
      vote_list = [0,0,0,0]

      for line in votes:
            line = line.strip()
            if line == 'A':
                  vote_list[0] += 1
            elif line == 'B':
                  vote_list[1] += 1
            elif line == 'C':
                  vote_list[2] += 1
            elif line == 'V':
                  vote_list[3] += 1
                  
      votes.close()

      nsp = vote_list[0]
      pap = vote_list[1]
      wp = vote_list[2]
      void = vote_list[3]
      print(pap,wp)
      #sort
      for i in range(len(vote_list)-1):
            for x in range(len(vote_list) - i - 1):
                  #print(vote_list[x],vote_list[x+1])
                  if vote_list[x] < vote_list[x+1]:
                        vote_list[x],vote_list[x+1] = vote_list[x+1],vote_list[x]
                        
      if vote_list[0] == vote_list[1]:
            print('Revote between PAP and WP')

      winnerVotes = vote_list[0]
      find_winner = True
      while find_winner:
            if winnerVotes == pap:
                  winner = "Winner is PAP"
                  find_winner = False
            if winnerVotes == nsp:
                  winner = "Winner is NSP"
                  find_winner = False
            if winnerVotes == wp:
                  winner = "Winner is WP"
                  find_winner = False
            if winnerVotes == void:
                  winnerVotes = vote_list[1]
            
      #output
      print('Results for the Electoral Division of MacPherson')
      for element in vote_list:
            if element == nsp:
                  print('NSP',str(round(element/28481*100,1))+'%')
            if element == void:
                  print('Void',str(round(element/28481*100,1))+'%')
            if element == wp:
                  print('WP',str(round(element/28481*100,1))+'%')
            if element == pap:
                  print('PAP',str(round(element/28481*100,1))+'%')
      print(winner)




############################################ TASK 1.2 ################################



generate = open('TIE.txt','w')
generate.close()
generate = open('TIE.txt','a')

votes = 28481
import random
votelist = []

while votes > 0:
      vote_percent = random.randint(1,100)
      if vote_percent <= 4:
            votelist.append('V')
            votes -= 1
      elif vote_percent <= 11:
            votelist.append('A')
            votes -= 1
      elif vote_percent <= 56:
            votelist.append('B')
            votes -= 1
      elif vote_percent >= 55:
            votelist.append('C')
            votes -= 1
for i in votelist:
      generate.write(i+'\n')
generate.close()
      
vote_application('ELECTION')
vote_application('TIE')


