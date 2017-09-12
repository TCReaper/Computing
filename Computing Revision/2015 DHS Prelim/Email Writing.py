
import datetime

f = open('PARTICIPANTS.txt','r')


p_list = {}
dates = []
emails = []

for line in f:
      line = line.split('-2015')
      dates.append(line[0])
      emails.append(line[1][:len(line[1])-1])
      
false_count = 0
for i in range(0,len(dates)):
      #print(emails[i],dates[i])
      check = True
      while check:
            try:
                  
                  if p_list[emails[i]] != dates[i]:
                        current = p_list[emails[i]]
                        temp = dates[i]
                        current = current.split('-')
                        temp = temp.split('-')
                        if current[1] > temp[1]:
                              false_count += 1
                              check = False
                        else:
                              if current[0] > temp[0]:
                                    check = False
                        p_list[emails[i]] = dates[i]
                        check = False
                  false_count += 1
                  check = False
            except KeyError:
                  p_list[emails[i]] = dates[i]
                  check = False

#print(p_list)
#sort list



for i in pee:
      print(i,p_list[i])

print('\n'+str(false_count) + ' duplicate entries removed.')

def Valid_Email(email):
      if email.count('@') != 1:
            return 'YOU SUCK'
      email = email.split('@')
      if email[1] == '' or email[0] == '':
            return 'YOU SUKC'
      emailWithoutAt = email[0]+email[1]
      for i in emailWithoutAt:
            if i not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','.','-','_']:
                  return "YOU SUCK"
      return "VALID"

