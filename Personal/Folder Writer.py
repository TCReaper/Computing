

# function to rewrite files in a specific folder

import os




def write(replacer):
      print(replacer)
      print(files)
      for original in files:
            new = original
            for element in replacer:
                  new = new.replace(element,' ')
            os.rename(os.path.join(path,original), os.path.join(path,new+'.mp4'))
            print('Replaced!')
      return True

while True:
      path = input('Enter path:  ')
      files = os.listdir(path)
      # retrives all files in specified path as array
      replace = input('Enter strings to replace separated by |:  ').split('|')
      if input('|'.join(replace) + str('\tCorrect? [y/n]:  ')).lower() == 'y':
               if write(replace):
                     print('\nThanks!')
                     break
      else:
               print('Ok! Let\'s try again!\n\n')
