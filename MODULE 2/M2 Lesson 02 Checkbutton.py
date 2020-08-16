# # task #1
#
# from tkinter import *
#
#
# def check_answer():
#
#     # print((checkbox_var1.get() == 0 or checkbox_var3.get() == 0 or checkbox_var4.get() == 0) and checkbox_var2.get() == 0)
#     # print((checkbox_var1.get() or checkbox_var3.get() or checkbox_var4.get()) and not checkbox_var2.get())
#
#     if checkbox_var1.get() and checkbox_var3.get() and checkbox_var4.get() and not checkbox_var2.get():
#
#         answer.set("Correct")
#
#     # elif (checkbox_var1.get() == 0 or checkbox_var3.get() == 0 or checkbox_var4.get() == 0) and checkbox_var2.get() == 0:
#
#     elif (checkbox_var1.get() or checkbox_var3.get() or checkbox_var4.get()) and not checkbox_var2.get():
#
#         answer.set("Answer incomplete")
#
#     else:
#
#         answer.set("Nope!")
#
#
# root = Tk()
#
# Label(text="Сколько будет: 1+1=").pack()
#
# checkbox_var1 = BooleanVar()
# checkbox_var1.set(0)
# Checkbutton(text="11, для строчного типа данных", variable=checkbox_var1, onvalue=1, offvalue=0).pack(anchor=W)
#
# checkbox_var2 = BooleanVar()
# checkbox_var2.set(0)
# Checkbutton(text="5, цена с надбавкой для рыночной экономики", variable=checkbox_var2, onvalue=1, offvalue=0).pack(anchor=W)
#
# checkbox_var3 = BooleanVar()
# checkbox_var3.set(0)
# Checkbutton(text="10, для чисел двоичной системы исчисления", variable=checkbox_var3, onvalue=1, offvalue=0).pack(anchor=W)
#
# checkbox_var4 = BooleanVar()
# checkbox_var4.set(0)
# Checkbutton(text="2, для чисел троичной системы исчисления и выше", variable=checkbox_var4, onvalue=1, offvalue=0).pack(anchor=W)
#
# Button(text="Check", command=check_answer).pack()
#
# answer = StringVar()
# answer.set("Выберите ответы, которые считаете верными")
# Label(textvariable=answer).pack()
#
#
# root.mainloop()


# # task #2
#
# from tkinter import *
# from tkinter.ttk import *
#
#
# def print_color():
#     text.delete(1.0, END)
#     text.insert(INSERT, "{}, {}, {}, {}, {}.".format(checkbox_black.get(), checkbox_green.get(), checkbox_blue.get(),
#                                                     checkbox_red.get(), checkbox_white.get()))
#
#
# root = Tk()
#
#
# checkbox_black = StringVar()
# Checkbutton(text="Black", variable=checkbox_black, onvalue="black", offvalue="").grid(row=1, column=1, sticky=W)
#
# checkbox_green = StringVar()
# Checkbutton(text="Green", variable=checkbox_green, onvalue="green", offvalue="").grid(row=2, column=1, sticky=W)
#
# checkbox_blue = StringVar()
# Checkbutton(text="Blue", variable=checkbox_blue, onvalue="blue", offvalue="").grid(row=3, column=1, sticky=W)
#
# checkbox_red = StringVar()
# Checkbutton(text="Red", variable=checkbox_red, onvalue="red", offvalue="").grid(row=4, column=1, sticky=W)
#
# checkbox_white = StringVar()
# Checkbutton(text="White", variable=checkbox_white, onvalue="white", offvalue="").grid(row=5, column=1, sticky=W)
#
# Button(text="Print", command=print_color).grid(row=6, column=1)
#
# text=Text()
# text.grid(column=2, row=1, rowspan=6, sticky=NSEW)
#
#
# root.mainloop()

# task #3

from tkinter import *


def check_answer():

    if checkbox_var4.get() and (message.get() == "7" or message.get() == "8"):

        answer.set("сэмь, восэм, но не больше дэвяти")

    elif checkbox_var1.get() or checkbox_var2.get() or checkbox_var3.get() or checkbox_var4.get():

        answer.set("Нэт!")

    else:

        answer.set("Error")


root = Tk()

Label(text="Дэты, сколко будэт 2+2?").grid(column=1, row=1, columnspan=2)

checkbox_var1 = BooleanVar()
checkbox_var1.set(0)
Checkbutton(text="3!", variable=checkbox_var1, onvalue=1, offvalue=0).grid(column=1, row=2, sticky=W)

checkbox_var2 = BooleanVar()
checkbox_var2.set(0)
Checkbutton(text="5!", variable=checkbox_var2, onvalue=1, offvalue=0).grid(column=1, row=3, sticky=W)

checkbox_var3 = BooleanVar()
checkbox_var3.set(0)
Checkbutton(text="4!", variable=checkbox_var3, onvalue=1, offvalue=0).grid(column=1, row=4, sticky=W)

checkbox_var4 = BooleanVar()
checkbox_var4.set(0)
Checkbutton(text="своя версия", variable=checkbox_var4, onvalue=1, offvalue=0).grid(column=1, row=5, sticky=W)

message = StringVar()
Entry(textvariable=message).grid(column=2, row=5, sticky=W)

Button(text="Check", command=check_answer).grid(column=1, row=6, columnspan=2)

answer = StringVar()
answer.set("Выберите ответы, которые считаете верными")
Label(textvariable=answer).grid(column=1, row=7, columnspan=2)


root.mainloop()