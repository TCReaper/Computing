
import time

old = open('CURRENCIES.txt','r')
updated = open('UPDATED.txt','r')


olddict = {}

for country in old:
      country = country.split(",")
      olddict[country[0]] = (country[1])[:len(country[1])-1]
      
for country in updated:
      country = country.split(",")
      if olddict[country[0]] != (country[1])[:len(country[1])-1]:
            olddict[country[0]] = (country[1])[:len(country[1])-1]


#     how long more can i take ?


sorted(olddict.keys())

new = open('NEWCURRENCIES.txt','w')
new.close()
new = open('NEWCURRENCIES.txt','a')

for country in olddict:
      new.write(country+'\n')
      
new.close()

def HashKey(Country):
      total = 0
      for letter in Country:
            asciiValue = ord(letter)
            total += asciiValue
      total = total % 53
      total += 1
      return total

def CreateCurrency():
      world = open('NEWCURRENCIES.txt','r')
      countryList = []
      for country in world:
            countryList.append(country[:len(country)-1])
      print(countryList)

      hashdik = [None for x in range(len(countryList)+3)]
      for name in countryList:
                  hashkey = HashKey(name)
                  inserted=False
                  print(name+' has hashkey '+str(hashkey))
                  while not inserted:
                        if hashkey > 49:
                              hashkey -= 50
                        if hashdik[hashkey] == None:
                              hashdik[hashkey] = name
                              print(name+' inserted into hashkey '+str(hashkey))
                              inserted=True
                        print('collision with '+hashdik[hashkey]+' at hashkey '+str(hashkey))
                        hashkey+=1
      print(hashdik)



                  
      new = open('DIRECTCURRENCIES.txt','w')
      new.close()
      new = open('DIRECTCURRENCIES.txt','a')
      
      



CreateCurrency()

            













      
