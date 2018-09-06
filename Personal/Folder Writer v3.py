

# function to rewrite files in a specific folder v3
# added manual control as well as specific file extension to edit
# added auto change function with string of text as input

import os

def change(filename):
      print(filename)
      new = input('New filename (with extension):  ')
      if new.lower() == 'skip':
            new = filename
      os.rename(os.path.join(path,filename), \
                os.path.join(path,new))
      print('Success!\n')

def autochange(filename,changes):
      store = filename
      for pair in range(len(changes)):
            group = changes[pair]
            filename = filename.replace(group[0],group[1])
      try:
            os.rename(os.path.join(path,store), \
                      os.path.join(path,filename))
      except:
            print('Oops {0} already exists'.format(filename))
      else:
            print('{0} changed to {1}'.format(store,filename))
      
      
manual=False
auto=False
query = input('Manual/Auto Writing [m/a]:  ')
if query == 'm':
      manual = True
elif query == 'a':
      auto = True

if manual:
      path = input('Enter path:  ')
      files = os.listdir(path)
      # retrives all files in specified path as array
      editing = []
      extension = input('Enter extension to edit:  ').replace('.','')
      for file in range(len(files)):
            if files[file].split('.')[-1] == extension:
                change(files[file])
            else:
                if extension == '':
                      change(files[file])
                
if auto:
      path = input('Enter path:  ')
      files = os.listdir(path)
      changes = []
      
      while True:
            change = input('Type in string to replace [None to end]:  ')
            if change == 'None':
                  break
            replacer = input('Type in string to replace with:  ')
            changes.append([change,replacer])

      for file in range(len(files)):
            autochange(files[file],changes)

            


