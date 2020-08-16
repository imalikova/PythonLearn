# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
#
# Radiobutton(text='The first').pack(anchor=W)
# Radiobutton(text='The second').pack(anchor=W)
# Radiobutton(text='The third').pack(anchor=W)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
#
# rb_var = BooleanVar()
# rb_var.set(0)
# rb1 = Radiobutton(text='The first', variable=rb_var, value=0).pack(anchor=W)
# rb2 = Radiobutton(text='The second', variable=rb_var, value=1).pack(anchor=W)
#
# root.mainloop()


from tkinter import *
from tkinter.ttk import *


def print_1():
    print(rb_var.get())


root = Tk()

rb_var = IntVar()
rb_var.set(0)
Radiobutton(text='The first', variable=rb_var, value=1, command=print_1).pack(anchor=W)
Radiobutton(text='The second', variable=rb_var, value=2, command=print_1).pack(anchor=W)
Radiobutton(text='The third', variable=rb_var, value=3, command=print_1).pack(anchor=W)

root.mainloop()