from tkinter import *

root =Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter you name: ")

def myclick():
    helloUser = "Hello " + e.get()
    mylabel = Label(root, text=helloUser)
    mylabel.pack()

myButton = Button(root, text="Enter you name", command=myclick)
myButton.pack()


root.mainloop()
