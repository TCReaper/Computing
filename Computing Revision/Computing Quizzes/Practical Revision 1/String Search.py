

# Strings should only be used to hang



a = "abcdefghijklmnopqrstuvwxyz"

def strsearch(source_string,start_index,end_index,search_key):
    string=source_string[start_index:end_index+1]
    
    
##    if search_key in string:
##        return True
##    else:
##        return False


def startsearch(source_string,start_index,end_index,search_key):
    changer = len(search_key)
    e = start_index + changer - 1
    print(strsearch(source_string,start_index,e,search_key))

print("functions are strsearch() and startsearch()")
