

# kopi o gao

def read():
      file_handle = open('DRINKS.txt')
      drinklist = []

      for drink in file_handle:
            drink = drink.strip()
            drinklist.append(drink)
      file_handle.close()
      
      return drinklist

def search(arr,term):
      n = 0
      for i in range(len(arr)):
            if term in arr[i]:
                  n+=1
      return n

def menu():
      choices = ['brewedcoffee','brewedtea','otherdrinks']
      print('menu')
      for i in range(len(choices)):
            print('{0}. {1}'.format(i+1,choices[i]))
      data = read()
      selection = input('what u want: ')
      if selection == '1':
            return search(data,'Kopi')
      elif selection == '2':
            return search(data,'Teh')
      else:
            return len(data) - search(data,'Kopi') - search(data,'Teh')



