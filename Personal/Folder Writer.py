

# function to rewrite files in a specific folder

import os

path = 'C:\\Users\\haosh\\Downloads\\Movies'
files = os.listdir(path)      # retrives all files in specified path as array

def write():
      for original in files:
            new = original
            new = new.replace('.',' ').replace(',',' ').replace('_',' ').replace(' mp4','')
            new = new.split('20')[0]

            os.rename(os.path.join(path,original), os.path.join(path,new+'.mp4'))


while True:
      if input('Is  '+str(path)+'  correct?    [ y/n ]    ').lower() == 'y':
            write()


