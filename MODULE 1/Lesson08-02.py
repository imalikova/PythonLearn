# from tkinter import *
#
#
# def print_word():
#     text_entry.set("the button clicked")
#
#
# def clear_word():
#     text_entry.set("")
#
# root = Tk()
# text_entry = StringVar()
# my_entry = Entry(textvariable=text_entry)
# my_entry.pack()
#
# first_button = Button(text="Paste", command=print_word)
# first_button.pack()
#
# second_button = Button(text="Clear", command=clear_word)
# second_button.pack()
#
# root.mainloop()


from tkinter import *


def print_word():
    my_entry.insert(END,'the button clicked!')


def clear_word():
    my_entry.delete(0, END)


root = Tk()
my_entry = Entry()
my_entry.pack()

first_button = Button(text="Paste", command=print_word)
first_button.pack()

second_button = Button(text="Clear", command=clear_word)
second_button.pack()

root.mainloop()