

file = open('JARGON.txt','r')
array = []
for line in file:
      line = line.strip('\n')
      array.append(line)

program = True
while program:
      choice = input('+'*23 + '\n1. Exact match\n2. Start of term\n 3. Within term\n' + '+'*18+'\nChoice ?')
      term = input('Term?')
      
      matches = 0
      match_list = []
      
      if choice == '1':
            for i in array:
                  if i == term:
                        matches += 1
                        match_list.append(i)
      elif choice == '2':
            for i in array:
                  matching = True
                  while matching:
                        #print(i)
                        for letter in range(len(term)):
                              if term[letter] == i[letter]:
                                    matching = True
                                    #print(term[letter],i[letter])
                              else:
                                    matching = False
                                    break
                        break
                  if matching == True:
                        matches += 1
                        match_list.append(i)

      elif choice == '3':
            for i in array:
                  for letter in range(len(i)):
                        if i[letter] == term[0]:
                              checker = letter
                              matching = True
                              while matching:
                                    for index in range(len(term)):
                                          #print(i,checker)
                                          if len(i)>checker and term[index] == i[checker] :
                                                matching = True
                                                checker += 1
                                          else:
                                                matching = False
                                                break
                                    break
                              if matching == True:
                                    matches += 1
                                    match_list.append(i)
                  

      else:
            print('Input valid choice!')

      for match_found in match_list:
            print(match_found)
      print('There were '+str(matches)+' matching term(s)')
