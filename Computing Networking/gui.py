from tkinter import *

root = Tk()

var = StringVar()
label = Message( root, textvariable=var, relief='raised')

var.set("hey!? How are you doing?")
label.pack()
root.mainloop()
