

# function to take files out of folders in a specific folder

import os
import shutil

def function():
    path = input('Enter path:  ')
    files = os.listdir(path)

    for folder in files:
        path2 = path+'\\'+folder+'\\'
        try:
            folderfiles = os.listdir(path2)
            for files in folderfiles:
                if 'mp4' in files or 'mkv' in files or 'jpg' in files:
                    path3 = path2+files
                    shutil.move(path3, path)
        except NotADirectoryError:
            pass
        except PermissionError:
            print('failed -',path3)
            pass



function()
