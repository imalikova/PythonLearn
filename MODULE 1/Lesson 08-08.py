from tkinter import *


def output_1():
    text = (f"{entry_one.get()} - it is the first entry's contents")
    entry_two.insert(END, text)


root = Tk()


entry_one = Entry()
entry_one.pack()

entry_two = Entry()
entry_two.pack()

first_button = Button(text="Button 1", command=output_1)
first_button.pack()

root.mainloop()