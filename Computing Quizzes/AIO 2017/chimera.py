

file = open('chimin.txt')
file_details = []
for i in file:
      i = i.strip('\n')
      file_details.append(i)
file.close()

first = file_details[1]
second = file_details[2]
final = file_details[3]

# test if foiled
output = ''
for i in range(len(final)):
      if final[i] == first[i] or final[i] == second[i]:
            pass
      else:
            output = 'PLAN FOILED'
            break
if output == '':
      output = 'SUCCESS'

subtask2 = open('chimout.txt','w')
subtask2.write(output)
subtask2.close()

# count splices

if output == 'SUCCESS':
      splices = 0
      current = ''
      for i in range(len(final)):
            print(first[i],second[i],final[i],splices,current)
            if final[i] == first[i] and final[i] == second[i]:
                  pass
            elif final[i] == first[i] and final[i] != second[i]:
                  if current == '':
                        current = 'a'
                  elif current == 'a':
                        pass
                  elif current == 'b':
                        splices += 1
                        current = 'a'
            elif final[i] == second[i] and final[i] != first[i]:
                  if current == '':
                        current = 'b'
                  elif current == 'b':
                        pass
                  elif current == 'a':
                        splices += 1
                        current = 'b'
      print(str(splices))

      outputfile = open('chimout.txt','a')
      outputfile.write('\n'+str(splices))
      outputfile.close()
















                        
