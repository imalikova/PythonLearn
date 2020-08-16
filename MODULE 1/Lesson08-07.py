from tkinter import *


def output_1():
    text = my_entry.get()
    my_entry1.insert(END,text)



root = Tk()
text_entry1 = StringVar()

my_entry = Entry(textvariable=text_entry1)
my_entry.pack()

text_entry2 = StringVar()

my_entry1 = Entry(textvariable=text_entry2)
my_entry1.pack()

first_button = Button(text="Button1", command=output_1)
first_button.pack()


root.mainloop()