# from tkinter import *
#
#
# def print_word_1():
#     text1 = entry_one.get()
#     text2 = entry_two.get()
#     print(f"{text1} {text2}")
#
# def print_word_2():
#     text1 = entry_one.get()
#     text2 = entry_two.get()
#     print(f"Значеине первого поля: {text1} Значеине второго поля: {text2}")
#
#
# root = Tk()
#
# entry_one = Entry()
# entry_one.pack()
#
# entry_two = Entry()
# entry_two.pack()
#
# first_button = Button(text="Button 1", command=print_word_1)
# first_button.pack()
#
# second_button = Button(text="Button 2", command=print_word_2)
# second_button.pack()
#
# root.mainloop()


from tkinter import *


def print_word_1():
    text1 = entry_one.get()
    text2 = entry_two.get()
    print(f"{text1} {text2}")

def print_word_2():
    text1 = entry_one.get()
    text2 = entry_two.get()
    print(f"Значеине первого поля: {text1} Значеине второго поля: {text2}")


root = Tk()

entry_one = Entry()
entry_one.pack()

entry_two = Entry()
entry_two.pack()


Button(text="Button 1", command=print_word_1).pack()

Button(text="Button 2", command=print_word_2).pack()


root.mainloop()


# from tkinter import *
#
#
# def translate():
#     first_button.config(text="Кнопка_1")
#     second_button.config(text="Кнопка_2")
#     # third_button.config(text="Кнопка_3")
#
# root = Tk()
#
# first_button = Button(text="Button 1", command=translate)
# first_button.pack()
#
# second_button = Button(text="Button 2", command=translate)
# second_button.pack()
#
# Button(text="Button 3", command=translate).pack()
#
# print(first_button, second_button)
#
# root.mainloop()