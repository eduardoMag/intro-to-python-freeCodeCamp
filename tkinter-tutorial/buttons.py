from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! i clicked on a button!")
    myLabel.pack()


mybutton = Button(root, text="click Me!", command=myClick)
mybutton.pack()

root.mainloop()
