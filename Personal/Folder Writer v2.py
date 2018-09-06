

# function to rewrite files in a specific folder v2
# adding manual control as well as specific file extension to edit 

import os

def change(filename):
      print(filename)
      new = input('New filename (with extension):  ')
      if new.lower() == 'skip':
            new = filename
      os.rename(os.path.join(path,filename), \
                os.path.join(path,new))
      print('Success!\n')

      
while True:
      path = input('Enter path:  ')
      files = os.listdir(path)
      # retrives all files in specified path as array
      editing = []
      extension = input('Enter extension to edit:  ')
      for file in range(len(files)):
            if files[file].split('.')[-1] == extension:
                change(files[file])
            else:
                if extension == '':
                      change(files[file])
                
                


