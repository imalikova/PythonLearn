# # task 1-4
#
# from tkinter import *
# from tkinter.ttk import *
#
#
# def print_1():
#     print(radio_var.get())
#     message.set(f"Radiobutton # {radio_var.get()} is chosen")
#
#
# root = Tk()
#
# Label(text="How to translate 'The current window'?").pack()
#
# radio_var = IntVar()
# radio_var.set(0)
# Radiobutton(text='The first', variable=radio_var, value=1, command=print_1).pack(anchor=W)
# Radiobutton(text='The second', variable=radio_var, value=2, command=print_1).pack(anchor=W)
# Radiobutton(text='The third', variable=radio_var, value=3, command=print_1).pack(anchor=W)
# Radiobutton(text='The forth', variable=radio_var, value=4, command=print_1).pack(anchor=W)
#
# message = StringVar()
# message.set("Radiobutton still not chosen")
#
# Label(textvariable=message).pack()
#
# root.mainloop()

# # task 5
#
# from tkinter import *
# # from tkinter.ttk import *
#
#
# def print_phone_pete():
#     message.set("312 5234353")
#
#
# def print_phone_ann():
#     message.set("312 4532334")
#
#
# def print_phone_bob():
#     message.set("999 3212345")
#
#
# root = Tk()
#
# Label(text="Choose the name for showing the cellphone number").grid(column=1, row=1, columnspan=2)
#
# rb_var = IntVar()
# rb_var.set(0)
# Radiobutton(text='Pete', variable=rb_var, value=1, command=print_phone_pete).grid(column=1, row=2)
# Radiobutton(text='Ann', variable=rb_var, value=2, command=print_phone_ann).grid(column=1, row=3)
# Radiobutton(text='Bob', variable=rb_var, value=3, command=print_phone_bob).grid(column=1, row=4)
#
# message = StringVar()
# message.set("")
# Label(textvariable=message).grid(column=2, row=3)
#
# root.mainloop()


# task #6

from tkinter import *


def check_answer():

    if radio_var.get() == 3 and message.get().lower() == "cat":
        answer.config(text="correct!")

    else:
        answer.config(text="error")


root = Tk()

Label(text="What is the right translation for 'Кот'?").grid(column=1, row=1, columnspan=2)

radio_var = IntVar()
Radiobutton(text='Dog', variable=radio_var, value=1).grid(column=1, row=2, sticky=W)
Radiobutton(text='Giraffe', variable=radio_var, value=2).grid(column=1, row=3, sticky=W)
Radiobutton(text='Your version', variable=radio_var, value=3).grid(column=1, row=4, sticky=W)


message = StringVar()
Entry(textvariable=message).grid(column=2, row=4)

Button(text="Check", command=check_answer).grid(column=1, row=5, columnspan=2)

answer = Label()
answer.grid(column=1, row=6, columnspan=2)


root.mainloop()