from tkinter import *


def show_fields():
    entry_three.delete(0,50)
    text1 = entry_one.get()
    text2 = entry_two.get()
    entry_three.insert(END,text1+" "+text2)


root = Tk()

entry_one = Entry()
entry_one.pack()

entry_two = Entry()
entry_two.pack()

entry_three = Entry()
entry_three.pack()

Button(text="Button 1", command=show_fields).pack()

root.mainloop()