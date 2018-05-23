
#qn 1 temperature

f = open('WIDEST.txt')

def menu():
      citylist = []
      for i in range(3):
            cities = input_city()
            high = temp('highest',-90,60)
            low = temp('lowest',-90,high)
            citylist.append([cities,high-low])
            if i < 2:
                  check = input('Do you want to insert another city? [y/n]:  ')
                  if check.lower() == 'n':
                        break
      print('\n{0:15}{1}'.format('Cities','Abs Diff in Temp'))
      for data in citylist:
            print('{0:15}{1}'.format(data[0],data[1]))
                              

            
def input_city():
      while True:
            city = input('Insert city:  ')
            if city.replace(' ','').isalpha() == True:
                  return city
            else:
                  print('Please input a valid city name!\n')
                  
def temp(polarity,mini,maxi):
      while True:
            try:
                  temp = int(input('Insert '+str(polarity)+' temperature:  '))
            except:
                  print('Please input valid temperature!\n')
            else:
                  if temp >= mini and temp <= maxi:
                        return temp
                  else:
                        print('Please input valid temperature between '\
                              +str(mini)+' and '+str(maxi))
print('\n'*33)
menu()
