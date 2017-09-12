# Key Typer


punctuation = [' ',':',',','.','/','\'',']','[',';','-','_','=','+','~','`',
               '|','!','@','#','$','%','^','&','*','(',')']




f = open('txt.txt')
data = []
for word in f.read().split():
      for i in word:
            if i in punctuation:
                  pass
            
      data.append(i)
print(data)

import SendKeys
import time

enter = "{ENTER}"

############################################
time.sleep(2)

text = ""
for i in data:
      if i == " ":
            SendKeys.SendKeys("``` ```")
            time.sleep(0.3)
            SendKeys.SendKeys(enter)
            time.sleep(0.3)
      else:
            SendKeys.SendKeys(str(i))
            SendKeys.SendKeys(enter)
