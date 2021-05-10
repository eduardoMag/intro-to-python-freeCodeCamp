from tkinter import *

root = Tk()

# creating a label widget
mylabel1 = Label(root, text="hello world!")
myLabel2 = Label(root, text="My name is parrotMaster")

mylabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()
