
import time
import SendKeys
import pyperclip

# EDIT THIS SECTION

time = 0.5 #units of seconds
message = '@aeronxyc#7757' #put 'None' for copied text

# - - - - - - - - - -

time.sleep(5) #5 second delay to get to text field
while True:
      time.sleep
      if message != 'None':
            pyperclip.copy(message)
      pyperclip.paste()
      SendKeys.SendKeys('{ENTER}')
      
