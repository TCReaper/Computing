

###################################  Task 3.1 #############

def ISBN_Check_Digit(isbn):
      isbnstring = isbn.replace('-','')
      if check_type(isbnstring) == 13:
            isbn = isbnstring[:-1]
            switch = 0
            total = 0
            for i in isbn:
                  if switch == 0:
                        total += int(i)
                        switch += 1
                  if switch == 1:
                        total += int(i) * 3
                        switch -= 1
            output = total % 10
      elif check_type(isbnstring) == 10:
            isbn = isbnstring[:-1]
            count = 1
            total = 0
            for i in isbn:
                  total += int(i) * count
                  count += 1
            output = total % 11
      elif check_type(isbnstring) == 9 or check_type(isbnstring) == 12:
            isbnstring += '0'
            return ISBN_Check_Digit(isbnstring)
      else:
            return 'Not a valid ISBN-10 or ISBN-13 number!'
      return output

            
def check_type(isbn):
      isbn = isbn.replace('-','')
      if len(isbn) == 13:
            return 13
      if len(isbn) == 10:
            return 10
      if len(isbn) == 12:
            return 12
      if len(isbn) == 9:
            #print(isbn,'check')
            return 9

###################################  Task 3.2 #############
      
def Valid_ISBN(isbn):
      if ISBN_Check_Digit(isbn) != 'Not a valid ISBN-10 or ISBN-13 number!':
            return True
      return False

###################################  Task 3.3 #############

def ISBN10_To_ISBN13(isbn):
      isbnstring = isbn.replace('-','')
      if check_type(isbnstring) == 13:
            return 'This is already a ISBN-13 number.'
      elif check_type(isbnstring) == 10:
            return '978-'+isbnstring
      else:
            return 'Not a valid ISBN-10 or ISBN-13 number!'

###################################  Task 3.4 #############
      
def ISBN13_To_ISBN10(isbn):
      isbnstring = isbn.replace('-','')
      if check_type(isbnstring) == 13:
            return isbn[3:]
      elif check_type(isbnstring) == 10:
            return 'This is already a ISBN-10 number.'
      else:
            return 'Not a valid ISBN-10 or ISBN-13 number!'

###################################  Task 3.5 #############

                        
                        
##                                      czezcompu            
##                                  tingdarenlerfuncz                                     
##                              ezcomputingdarenlerfuncz                                  
##                      ezcomputingdare           nlerfunc                                
##                   zezcomputingd                  arenler                               
##                 funczezcomputin                   gdaren                               
##                 lerfunczezcomput                   ingda                               
##                 renlerfuncz ezcomp    utingdarenl  erfun                               
##                 czezcomputingdarenl erfunczezcomput ingd                               
##                 arenlerfunczezcom  putingdarenlerfunczez                     
##                compu  tingdarenle  rfunczezcomputingdare                      
##               nlerfunczezcomputing darenlerfun czezcompu                      
##              tingdarenlerfunczez   computingdarenlerfunc                               
##             zezcomputingdarenlerfunczezcomputing  daren                                
##            lerfu          nczezcomputingdare     nlerfu                      
##           nczez                      computi     ngdare                  
##          nlerfu                                 nczezc
##         omputi                                 ngdare                                  
##        nlerfu                                  nczezc                                  
##        omput                      ingd        arenle                         
##        rfun                      czezc omp   utingd      
##        aren                      lerfunczez  compu                         tin
##       lerfu                      nczezcomp  uting                        daren
##       zezco                     mputingdar enler                       funcze
##       putin                     gdarenler  funcz                     ezcompu
##       arenl                    erfunczez  comput                   ingdare 
##       uncze                    zcomputi   ngdarenlerfunczezcom   putingd     a   
##        erfu                   nczezcom    putingdarenlerfunczezcomputi      ng   
##        enle                   rfuncze     zcomp   uting   darenlerfu      ncze   
##        ompu                  tingdare      nle   rfunczezcomputing      darenl   
##        erfun               czezc omput         ingdarenlerfunczez     computi  
##         ngda             renle  rfuncze         zcomputingdarenlerf   unczezc
##         mputi            ngdarenlerfunc                     zezcompu    tingda
##          lerfu            nczezcomputi              ngda       renler  func ze     
##          mputin              gdar                   enle        rfuncz  ezcomp     
##           ingdar                                enl              erfun    czez      
##            computin                            gdar              enler     fun    
##               zezcomp                          utin              gdarenlerfunc        
##      ingdare    nlerfunczezcomput                  ing         darenle    r              
##      funczezcomputi ngdarenlerfunczezcomp           utin    gdarenl                      
##      erfu nczezcomputing    darenlerfunczez computingdarenlerfunc                        
##      zezc  omputingda         renlerfuncz ezcomputingdarenler                           
##      func   zezcom         putingdarenl erfun czezcomputi
##       ngdarenler           funczezcomp  utin        
##        gdarenl              erfuncze   zcom
##          put                ingdar    enle              
##                              rfuncz  ezco                
##                               mputingdar        
##                                 enlerfu      
##                                   ncz                                                                        


# assume array is of 267 books
# next prime is 269
global lib_array

lib_array = [0 for i in range(269)]

def Hash_Key(isbn):
      global lib_array
      isbn = isbn.replace('-','')
      isbnint = 0
      for i in isbn:
            isbnint += int(i)
      index = isbnint % 269
      if lib_array[index] == 0:
            return index
      else:
            step = isbnint % 17
            found_space = False
            while not found_space:
                  if lib_array[step] == 0:
                        found_space = True
                  else:
                        step = isbnint % 11
            
      return step
      

###################################  Task 3.6 #############



def generate_library():
      libraryfile = open('LIBRARY.txt','w')
      libraryfile.close()
      libraryfile = open('LIBRARY.txt','a')

      for i in range(267):
            libraryfile.write(str(Hash_Key(generate_isbn()))+'\n')
            
def generate_isbn():
      import random
      if random.randint(0,1) == 0: #generate isbn10
            isbn = ''
            for i in range(9):
                  isbn += str(random.randint(0,9))
            return isbn + str(ISBN_Check_Digit(isbn))
      else: #generate isbn13
            isbn = ''
            for i in range(9):
                  isbn += str(random.randint(0,9))
            isbn = isbn + str(ISBN_Check_Digit(isbn))
            isbn = ISBN10_To_ISBN13(isbn)
            return isbn

def Insert_Book(isbn):
      libraryfile = open('LIBRARY.txt','r')
      global lib_array
      lib_array = []
      for i in libraryfile:
            i = i.strip()
            lib_array.append(i)
      libraryfile.close()
      index = Hash_Key(isbn)
      lib_array[index] = isbn
      libraryfile = open('LIBRARY.txt','w')
      for i in lib_array:
            libraryfile.write(i+'\n')
      





































