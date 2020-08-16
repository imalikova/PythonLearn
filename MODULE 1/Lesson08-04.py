# from tkinter import *
#
#
# def print_word():
#     text = my_entry.get()
#     print(text)
#
#
# root = Tk()
# my_entry = Entry()
# my_entry.pack()
#
# first_button = Button(text="Copy", command=print_word)
# first_button.pack()
#
# root.mainloop()
#

from tkinter import *


def print_word():
    text = text_entry.get()
    print(text)
    text_button.set("Copy3")


root = Tk()

text_entry = StringVar()
Entry(textvariable=text_entry).pack()

text_button = StringVar()
text_button.set("Copy2")
Button(textvariable=text_button, text="Copy", command=print_word).pack()

root.mainloop()