# from tkinter import *
#
#
# def print_word():
#     print("Hi")
#
#
# root = Tk()
#
# first_button = Button(text="Click", command=print_word)
# first_button.pack()
#
# root.mainloop()


# from tkinter import *
# from tkinter import messagebox
#
#
# def print_word():
#     messagebox.showinfo("My title","Hi!")
#
#
# root = Tk()
#
# first_button = Button(text="Click", command=print_word)
# first_button.pack()
#
# root.mainloop()


# from tkinter import *
#
#
# def print_word():
#     my_entry = Entry()
#     my_entry.pack()
#
#
# root = Tk()
#
# first_button = Button(text="Click", command=print_word)
# first_button.pack()
#
# root.mainloop()


# from tkinter import *
#
#
# def print_word():
#     second_button = Button(text="Close window", command=root.destroy)
#     second_button.pack()
#
#
# root = Tk()
#
# my_entry = Entry()
# my_entry.pack()
#
# first_button = Button(text="Click", command=print_word)
# first_button.pack()
#
# root.mainloop()


# from tkinter import *
#
#
# def print_word():
#     my_entry.delete(0,4)
#     my_entry.insert(END,'Hello')
#
# root = Tk()
#
# my_entry = Entry()
# my_entry.pack()
#
# first_button = Button(text="Click", command=print_word)
# first_button.pack()
#
# root.mainloop()

# from tkinter import *
#
#
# def print_word():
#     print(my_entry.get())
#
# root = Tk()
#
# my_entry = Entry()
# my_entry.pack()
#
# first_button = Button(text="Click", command=print_word)
# first_button.pack()
#
# root.mainloop()

# from tkinter import *
#
#
# def print_word():
#     text = my_entry.get()
#     my_entry2.delete(0, END)
#     my_entry2.insert(END,text)
#
# root = Tk()
#
# my_entry = Entry()
# my_entry.pack()
#
# my_entry2 = Entry()
# my_entry2.pack()
#
# first_button = Button(text="Click", command=print_word)
# first_button.pack()
#
# root.mainloop()

# from tkinter import *
#
#
# def print_word():
#    print(text_entry.get())
#    text_entry.set(99)
#
# root = Tk()
# text_entry = StringVar()
# my_entry = Entry(textvariable=text_entry)
# my_entry.pack()
#
# my_entry2 = Entry()
# my_entry2.pack()
#
# first_button = Button(text="Click", command=print_word)
# first_button.pack()
#
# root.mainloop()

# from tkinter import *
#
#
# def print_word():
#    print(text_entry.get())
#    text_entry.set(99)
#
# root = Tk()
# text_entry = StringVar()
# my_entry = Entry(textvariable=text_entry)
# my_entry.pack()
#
# my_entry2 = Entry(textvariable=text_entry)
# my_entry2.pack()
#
# first_button = Button(text="Click", command=print_word)
# first_button.pack()
#
# root.mainloop()

from tkinter import *


def print_word():
   print(text_entry.get())
   number=99
   text_entry.set(f"{number},{number-9}")

root = Tk()
text_entry = StringVar()
my_entry = Entry(textvariable=text_entry)
my_entry.pack()

my_entry2 = Entry(textvariable=text_entry)
my_entry2.pack()

first_button = Button(text="Click", command=print_word)
first_button.pack()

root.mainloop()