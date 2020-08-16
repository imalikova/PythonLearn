# from tkinter import *
# from tkinter.ttk import *
#
#
# def change(event):
#     print(event)
#     b['text'] = 'Thanks for your click. ;)'
#
#
# root = Tk()
#
# b = Button(text='Click me!')
# b.bind('<Button-1>', change)
# b.bind('<Return>', change)
# b.pack()
#
# root.mainloop()

from tkinter import *
from tkinter.ttk import *


def changeFont(event, font):
    l['font'] = font


root = Tk()

l = Label(text="Hello World")
l.bind('<Button-1>', lambda event, f="Verdana": changeFont(event, f))
l.bind('<Button-2>', lambda event, f="Times": changeFont(event, f))
l.pack()

root.mainloop()

