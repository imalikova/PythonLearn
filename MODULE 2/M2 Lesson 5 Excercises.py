# Task 1
# Напишите программу состоящую из ListBox() и кнопки.
# При нажатии на кнопку в листе добавляется случайная цифра в диапазоне от -100 до 100.

# from tkinter import *
# import random
#
#
# def add_number():
#     list_numbers.insert(END, random.randint(0, 100))
#
#
# root = Tk()
#
# list_numbers = Listbox(selectmode=EXTENDED)
# list_numbers.grid(row=1, column=1)
# scroll_list = Scrollbar(command=list_numbers.yview)
# scroll_list.grid(row=1, column=2, sticky=NSEW)
# list_numbers.config(yscrollcommand=scroll_list.set)
#
# Button(text="Add", command=add_number).grid(row=2, column=1, columnspan=2)
#
# root.mainloop()


# Task 2
# # Напишите программу состоящую из ListBox() c полосой прокрутки и кнопки.
# # При нажатии на кнопку в листе добавляется список из 3-х цифр от -50 до 50.

# from tkinter import *
# import random
#
#
# def add_number():
#     for i in range(3):
#         i = random.randint(-50, 50)
#         list_numbers.insert(END, i)
#
#
# root = Tk()
#
# list_numbers = Listbox(selectmode=EXTENDED)
# list_numbers.grid(row=1, column=1)
# scroll = Scrollbar(command=list_numbers.yview)
# scroll.grid(row=1, column=2, sticky=NSEW)
# list_numbers.config(yscrollcommand=scroll.set)
#
# Button(text="Add", command=add_number).grid(row=2, column=1, columnspan=2)
#
#
# root.mainloop()


# Task 3
# # Напишите программу состоящую из ListBox() c полосой прокрутки и кнопки.
# # При нажатии на кнопку в листе добавляется цифра, при каждом следующем нажатии новая добавляющаяся цифра
# # увеличивает свое значение на 5 относительно предыдущей цифры.

# from tkinter import *
# import random
#
#
# def add_number():
#     # if not list_numbers.size(): # check for emptiness, if the list is not empty
#     if not list_numbers.get(0): # check for emptiness, if the list is not empty
#         list_numbers.insert(END, random.randint(1, 100))
#     else:
#         list_numbers.insert(END, list_numbers.get([list_numbers.size()-1])+5)
#
#
# root = Tk()
#
# list_numbers = Listbox(selectmode=EXTENDED)
# list_numbers.grid(row=1, column=1)
# scroll = Scrollbar(command=list_numbers.yview)
# scroll.grid(row=1, column=2, sticky=NSEW)
# list_numbers.config(yscrollcommand=scroll.set)
#
# Button(text="Add", command=add_number).grid(row=2, column=1, columnspan=2)
#
#
# root.mainloop()

# Task 4 (grid)
# Напишите программу состоящую из ListBox() c полосой прокрутки, Text(), кнопки
# "Add elements", "Print to console" и "Print to Text()":
#
# при нажатии на кнопку "Add elements" - ListBox() заполняется элементами списка: \
#     ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt'];
# при нажатии на кнопку "Print to console" - в консоль печатаются все элементы списка;
# при нажатии на кнопку "Print to Text()" - в Text() печатаются все элементы списка.

# from tkinter import *
#
# elements_list = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_button():
#     list_numbers.insert(END, elements_list[list_numbers.size()])
#
#
# def print_button():
#
#     print(elements_list)
#
#
# def print_text_button():
#
#     split_text = text.get(1.0, END).split(",")
#
#     if int(len(text.get(1.0, END))) < 2:
#         text.insert(INSERT, elements_list[0])
#
#     else:
#         for element in range(6):
#             if int(len(split_text)) == element:
#                 text.insert(INSERT, f", {elements_list[element]}")
#
#
# root = Tk()
#
# Button(text="Add Elements", command=add_button).grid(row=1, column=1, columnspan=2)
# Button(text="Print to console", command=print_button).grid(row=2, column=1, columnspan=2)
# Button(text="Print to Text()", command=print_text_button).grid(row=3, column=1, columnspan=2)
#
# list_numbers = Listbox(selectmode=EXTENDED)
# list_numbers.grid(row=4, column=1)
# scroll = Scrollbar(command=list_numbers.yview)
# scroll.grid(row=4, column=2, sticky=NSEW)
# list_numbers.config(yscrollcommand=scroll.set)
#
# text = Text(root)
# text.insert(INSERT, "")
# text.grid(sticky=NSEW, column=3, row=1, rowspan=4)
#
# root.mainloop()


# # Task 4 (Pack)
# # Напишите программу состоящую из ListBox() c полосой прокрутки, Text(), кнопки
# # "Add elements", "Print to console" и "Print to Text()":
# #
# # при нажатии на кнопку "Add elements" - ListBox() заполняется элементами списка: \
# #     ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt'];
# # при нажатии на кнопку "Print to console" - в консоль печатаются все элементы списка;
# # при нажатии на кнопку "Print to Text()" - в Text() печатаются все элементы списка.
#
# from tkinter import *
#
# elements_list = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_button():
#     # print(list_items.size())
#     list_items.insert(END, elements_list[list_items.size()])
#
#
# def print_button():
#     # for item in range(list_items.size()):
#     #     print(f"{list_items.get(item)}")  # ask the teacher
#
#     for item in list_items.get(0, END):
#         print(item, end=", ")   # print in console in one row
#
#
# def print_text_button():
#     for item in range(list_items.size()):
#         text.insert(INSERT, f"{list_items.get(item)}, ")
#
#
# root = Tk()
#
# left_frame = Frame()
# left_frame.pack(side=LEFT, fill=Y)
#
# Button(left_frame, text="Add Elements", command=add_button).pack()
# Button(left_frame, text="Print to console", command=print_button).pack()
# Button(left_frame, text="Print to Text()", command=print_text_button).pack()
#
# listbox_frame = Frame(left_frame)
# listbox_frame.pack(fill=Y, expand=1)
#
#
# list_items = Listbox(listbox_frame, selectmode=EXTENDED)
# list_items.pack(side=LEFT, fill=Y)
# scroll = Scrollbar(listbox_frame, command=list_items.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_items.config(yscrollcommand=scroll.set)
#
# text = Text(root, width=40, height=10)
# text.insert(INSERT, "")
# text.pack(side=LEFT, expand=1, fill=BOTH)
#
# root.mainloop()


# Task 5
#Напишите программу состоящую из ListBox() c полосой прокрутки, Text() и кнопок:
# "Add elements", "Print elements","Print the first element" и "Print the last element":

# при нажатии на кнопку "Add elements" - ListBox() заполняется элементами списка:
# ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt'];
# при нажатии на кнопку "Print elements" - в Text() печатаются все элементы списка;
# при нажатии на кнопку "Print the first element" - в Text() печатается первый элемент;
# при нажатии на кнопку "Print the last element" - в Text() печатается последний элемент.


# from tkinter import *
#
# elements_list = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_elements():
#     for element in elements_list:
#         list_items.insert(END, element)
#
#
# def print_elements():
#     text.insert(INSERT, "ALL:")
#     for item in range(list_items.size()):
#         text.insert(INSERT, f"{list_items.get(item)}, ")
#
#
# def print_first():
#     text.insert(INSERT, f"\nFirst: {list_items.get(0)}")
#
#
# def print_last():
#     text.insert(INSERT, f"\nLast: {list_items.get(END)}")
#
#
# root = Tk()
#
# Button(text="Add elements", command=add_elements).grid(row=1, column=1, columnspan=2)
# Button(text="Print elements", command=print_elements).grid(row=2, column=1, columnspan=2)
# Button(text="Print the first element", command=print_first).grid(row=3, column=1, columnspan=2)
# Button(text="Print the last element", command=print_last).grid(row=4, column=1, columnspan=2)
#
# list_items = Listbox(selectmode=EXTENDED)
# list_items.grid(row=5, column=1)
# scroll = Scrollbar(command=list_items.yview)
# scroll.grid(row=5, column=2, sticky=NSEW)
# list_items.config(yscrollcommand=scroll.set)
#
# text = Text(root)
# text.insert(INSERT, "")
# text.grid(sticky=NSEW, column=3, row=1, rowspan=4)
#
# root.mainloop()


# Task 6

# Напишите программу состоящую из ListBox() c полосой прокрутки и кнопок: "Add elements",
# "Delete elements","Delete the first element" и "Delete the last element":
#
# при нажатии на кнопку "Add elements" - ListBox() заполняется элементами списка:
# ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt'];
# при нажатии на кнопку "Delete elements" - удаляются все элементы списка;
# при нажатии на кнопку "Delete the first element" - удаляется первый элемент;
# при нажатии на кнопку "Delete the last element" - удаляется последний элемент.

# from tkinter import *
#
#
# elements_list = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_elements():
#     for element in range(6):
#         list_numbers.insert(END, elements_list[element])
#
#
# def delete_elements():
#     list_numbers.delete(0, END)
#
#
# def delete_first():
#     list_numbers.delete(0)
#
#
# def delete_last():
#     list_numbers.delete(list_numbers.size()-1)
#
#
# root = Tk()
#
# Button(text="Add elements", command=add_elements).grid(row=1, column=1, columnspan=2)
# Button(text="Delete elements", command=delete_elements).grid(row=2, column=1, columnspan=2)
# Button(text="Delete the first element", command=delete_first).grid(row=3, column=1, columnspan=2)
# Button(text="Delete the last element", command=delete_last).grid(row=4, column=1, columnspan=2)
#
# list_numbers = Listbox(selectmode=EXTENDED)
# list_numbers.grid(row=5, column=1)
# scroll = Scrollbar(command=list_numbers.yview)
# scroll.grid(row=5, column=2, sticky=NSEW)
# list_numbers.config(yscrollcommand=scroll.set)
#
#
# root.mainloop()


# # Task # 7
# # Напишите программу состоящую из ListBox() c полосой прокрутки, Text() и кнопок: "Add elements",
# # "Print an index element" и "Print the selected element":
# #
# # при нажатии на кнопку "Add elements" - ListBox() заполняется элементами списка: \
# #     ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt'];
# # при нажатии на кнопку "Print an index element" - в Text() печатается индекс выделенного элемента списка;
# # при нажатии на кнопку "Print the selected element" - в Text() печатается выбранный элемент. Добавьте проверку,
# # если элемент не выбран программа не должна выдавать ошибку.
#
#
# from tkinter import *
#
#
# elements_list = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_elements():
#     for element in range(6):
#         list_items.insert(END, elements_list[element])
#
#
# def print_index_element():
#     print(list_items.curselection())
#     text.insert(INSERT, f"Index: {list_items.curselection()}")
#
#
# def print_selected_element():
#     if list_items.curselection():
#         text.insert(INSERT, f"The last: {list_items.get(list_items.curselection())}, ")
#     else:
#         text.insert(INSERT, f"")
#
#
# root = Tk()
#
# Button(text="Add elements", command=add_elements).grid(row=1, column=1, columnspan=2)
# Button(text="Print an index element", command=print_index_element).grid(row=2, column=1, columnspan=2)
# Button(text="Print the selected element", command=print_selected_element).grid(row=3, column=1, columnspan=2)
#
#
# list_items = Listbox(selectmode=EXTENDED)
# list_items.grid(row=4, column=1)
# scroll = Scrollbar(command=list_items.yview)
# scroll.grid(row=4, column=2, sticky=NSEW)
# list_items.config(yscrollcommand=scroll.set)
#
# text = Text(root)
# text.insert(INSERT, "")
# text.grid(sticky=NSEW, column=3, row=1, rowspan=4)
#
#
# root.mainloop()


# # Task # 8
# #
# # Напишите программу состоящую из ListBox() c полосой прокрутки, Text() и кнопок: "Add elements", "Print the element" и "Delete the element":
# #
# # при нажатии на кнопку "Add elements" - ListBox() заполняется элементами списка: ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt'];
# # при нажатии на кнопку "Print the element" - в Text() печатается индекс и значение выделенного элемента списка;
# # при нажатии на кнопку "Delete the element" - удаляется выбранный элемент;
# # Добавьте необходимы проверки, если элемент не выбран, что бы программа не вызывала ошибок.
#
# from tkinter import *
#
#
# elements_list = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_elements():
#     for element in range(6):
#         list_items.insert(END, elements_list[element])
#
#
# def print_the_element():
#     if list_items.curselection():
#         text.insert(INSERT, f"\nIndex: Value: {list_items.curselection()}\nValue: {list_items.get(list_items.curselection())}")
#
#
# def delete_element():
#     if list_items.curselection():
#         list_items.delete(list_items.curselection())
#
#
# root = Tk()
#
# Button(text="Add elements", command=add_elements).grid(row=1, column=1, columnspan=2)
# Button(text="Print the element", command=print_the_element).grid(row=2, column=1, columnspan=2)
# Button(text="Delete the element", command=delete_element).grid(row=3, column=1, columnspan=2)
#
#
# list_items = Listbox(selectmode=EXTENDED)
# list_items.grid(row=4, column=1)
# scroll = Scrollbar(command=list_items.yview)
# scroll.grid(row=4, column=2, sticky=NSEW)
# list_items.config(yscrollcommand=scroll.set)
#
# text = Text(root)
# text.insert(INSERT, "")
# text.grid(sticky=NSEW, column=3, row=1, rowspan=4)
#
#
# root.mainloop()

# Task #9
#
# Напишите программу состоящую из ListBox(selectmode=EXTENDED) c полосой прокрутки, Text() и кнопок: "Add elements",
# "Print the selected elements" и
# "Delete the seleсted elements":
#
# при нажатии на кнопку "Add elements" - ListBox() заполняется элементами списка:
# ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt'];
# при нажатии на кнопку "Print the selected elements" - в Text() печатаются индексы и значения выделенных элементов;
# при нажатии на кнопку "Delete the seleсted elements" - удаляются выбранные элементы;
# Добавьте необходимы проверки, если элемент не выбран, что бы программа не вызывала ошибок.

# from tkinter import *
#
#
# elements_list = ['0 a hat', '1 a dress', '2 a tie', '3 a shirt', '4 a belt', '5 a skirt']
#
#
# def add_elements():
#     for element in range(6):
#         list_items.insert(END, elements_list[element])


# def print_selected():
#     if list_items.curselection():
#         text.insert(END, "Index: ")
#         for item in list_items.curselection():
#             text.insert(INSERT, f"{item}, ")
#         text.insert(END, "\nValue: ")
#         for item in list_items.curselection():
#             text.insert(INSERT, f"{list_items.get(item)}, ")
#     else:
#         text.insert(INSERT, f"")


# def print_selected():
#     if list_items.curselection():
#         line_index = "Index: "
#         line_value = "Value: "
#         for item in list_items.curselection():
#             line_index = f"{line_index}{item}, "
#             line_value = f"{line_value}{list_items.get(item)}, "
#
#         text.insert(END, f"{line_index[:-2]}.\n{line_value[:-2]}.") # cut the last symbol "," and add "."
#
#
# def delete_selected():
#
#     for item in list_items.curselection()[::-1]:
#         list_items.delete(item)
#
#
# root = Tk()
#
# Button(text="Add elements", command=add_elements).grid(row=1, column=1, columnspan=2)
# Button(text="Print the selected elements", command=print_selected).grid(row=2, column=1, columnspan=2)
# Button(text="Delete the seleсted elements", command=delete_selected).grid(row=3, column=1, columnspan=2)
#
#
# list_items = Listbox(selectmode=EXTENDED)
# list_items.grid(row=4, column=1)
# scroll = Scrollbar(command=list_items.yview)
# scroll.grid(row=4, column=2, sticky=NSEW)
# list_items.config(yscrollcommand=scroll.set)
#
# text = Text(root)
# text.insert(INSERT, "")
# text.grid(sticky=NSEW, column=3, row=1, rowspan=4)
#
#
# root.mainloop()



# # Task #10
# # Напишите программу состоящую из поля ввода, кнопки и ListBox() c полосой прокрутки. При нажатии на кнопку:
# #
# # в листе должна добавиться строка напечатанная в поле ввода;
# # после добавления значения из поле ввода очищается.
# # .strip() - это метод строки, которые удаляет все пробелы в начале и конце строки.
# # Доработайте программу так, чтобы не добавлялись строки из пробелов, а добавленные строки не начинались и не заканчивались пробелами;
# # Добавьте необходимы проверки, что бы программа не вызывала ошибок.
#
#
# from tkinter import *
#
#
# elements_list = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_item():
#     strip_entry = entry.get().strip()
#
#     if strip_entry:
#         list_items.insert(END, strip_entry)
#
#     entry.delete(0, END)
#
#
# root = Tk()
#
# Button(text="Add item", command=add_item).grid(row=1, column=1, columnspan=2)
#
# entry = Entry()
# entry.grid(row=2, column=1, columnspan=2)
#
# list_items = Listbox(selectmode=EXTENDED)
# list_items.grid(row=4, column=1)
# scroll = Scrollbar(command=list_items.yview)
# scroll.grid(row=4, column=2, sticky=NSEW)
# list_items.config(yscrollcommand=scroll.set)
#
# root.mainloop()

# Task #11
#
# Напишите программу, состоящую из двух списков Listbox() c полосой прокрутки.
# В первом будет, например, перечень товаров, заданный программно.
# Второй изначально пуст, пусть это будет перечень покупок.
# При клике на одну кнопку товар должен переходить из одного списка в другой.
# При клике на вторую кнопку – возвращаться (человек передумал покупать).
# Предусмотрите возможность множественного выбора элементов списка и их перемещения.


# from tkinter import *
#
# groceries_list = ["apple", "banana", "meat", "fish", "bread", "cheese", "candy", "milk", "potato", "cucumber",
#                   "coffee", "pears", "strawberry"]
#
#
# def add_to_list():
#
#     selected_list = list_items.curselection() # did not work without adding the variable!
#
#     if list_items.curselection():
#         for item in range(len(list_items.curselection())):
#             chosen_items.insert(END, list_items.get(selected_list[item]))
#
#     selected_list_rev = (selected_list[::-1])
#
#     for item in selected_list_rev:
#         list_items.delete(item)
#
#
# def return_back():
#
#     return_list = chosen_items.curselection()
#
#     if chosen_items.curselection():
#         for item in range(len(chosen_items.curselection())):
#             list_items.insert(END, chosen_items.get(return_list[item]))
#
#             return_list_rev = (return_list[::-1])
#
#     for item in return_list_rev:
#         chosen_items.delete(item)
#
#
# root = Tk()
#
# left_frame = Frame()
# left_frame.pack(side=LEFT, fill=Y)
#
# listbox_frame = Frame(left_frame)
# listbox_frame.pack(fill=Y, expand=1)
#
#
# list_items = Listbox(listbox_frame, selectmode=EXTENDED)
# list_items.pack(side=LEFT, fill=Y)
# scroll = Scrollbar(listbox_frame, command=list_items.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_items.config(yscrollcommand=scroll.set)
#
# for element in range(len(groceries_list)):
#     list_items.insert(END, groceries_list[element])
#
#
# button_frame = Frame()
# button_frame.pack(side=LEFT)
#
# Button(button_frame, text=">>>", command=add_to_list).pack()
# Button(button_frame, text="<<<", command=return_back).pack()
#
#
# right_frame = Frame()
# right_frame.pack(side=LEFT, fill=Y)
#
# chosen_frame = Frame(right_frame)
# chosen_frame.pack(fill=Y, expand=1)
#
#
# chosen_items = Listbox(chosen_frame, selectmode=EXTENDED)
# chosen_items.pack(side=LEFT, fill=Y)
# scroll = Scrollbar(chosen_frame, command=chosen_items.yview)
# scroll.pack(side=LEFT, fill=Y)
# chosen_items.config(yscrollcommand=scroll.set)
#
#
# root.mainloop()

# Task #12
#
# Написать программу с двумя ListBox() c полосой прокрутки и Text(). Добавить список ведей в оба ListBox(). Реализовать:
#
# перемещение выделенных позицый между ListBox().
# ListBox() и Text(), перемещение из текстового блока выделенных слов.

from tkinter import *

groceries_list = ["apple", "banana", "meat", "fish", "bread", "cheese", "candy", "milk", "potato", "cucumber",
                  "coffee", "pears", "strawberry"]


def move_left_to_right():
    selected_list = list_items.curselection()

    if list_items.curselection():
        for item in selected_list:
            chosen_items.insert(END, list_items.get(item))
        for item in selected_list[::-1]:
            list_items.delete(item)


def move_right_to_left():
    selected_list = chosen_items.curselection()

    if chosen_items.curselection():
        for item in selected_list:
            list_items.insert(END, chosen_items.get(item))
        for item in selected_list[::-1]:
            chosen_items.delete(item)


def up_to_1():
    if text_entry.get():
        for item in text_entry.get().split(", "):
            if item != "":
                list_items.insert(END, item)
    text_entry.delete(0, END)


def down_to_3():
    selected_list = list_items.curselection()
    selected_list_rev = (selected_list[::-1])

    if list_items.curselection():
        for item in range(len(list_items.curselection())):
            text_entry.insert(END, f"{list_items.get(selected_list[item])}, ")

    for item in selected_list_rev:
        list_items.delete(item)


def up_to_2():
    if text_entry.get():
        for item in text_entry.get().split(", "):
            if item != "":
                chosen_items.insert(END, item)
    text_entry.delete(0, END)


def two_to_3():
    chosen_list = chosen_items.curselection()
    chosen_list_rev = (chosen_list[::-1])

    if chosen_items.curselection():
        for item in range(len(chosen_items.curselection())):
            text_entry.insert(END, f"{list_items.get(chosen_list[item])}, ")

    for item in chosen_list_rev:
        list_items.delete(item)


root = Tk()

header_frame = LabelFrame(text="Frame Header")
header_frame.pack(fill=Y)

listbox_frame = Frame(header_frame)
listbox_frame.pack(side=LEFT, fill=Y, expand=1)


list_items = Listbox(listbox_frame, selectmode=EXTENDED)
list_items.pack(side=LEFT, fill=Y)
scroll = Scrollbar(listbox_frame, command=list_items.yview)
scroll.pack(side=LEFT, fill=Y)
list_items.config(yscrollcommand=scroll.set)

for element in range(len(groceries_list)):
    list_items.insert(END, groceries_list[element])


button_frame = LabelFrame(header_frame, text="Frame Button")
button_frame.pack(side=LEFT)

Button(button_frame, text=">>>", command=move_left_to_right).pack()
Button(button_frame, text="<<<", command=move_right_to_left).pack()


right_frame = Frame(header_frame)
right_frame.pack(fill=Y)

chosen_frame = Frame(right_frame)
chosen_frame.pack(fill=Y, expand=1)


chosen_items = Listbox(chosen_frame, selectmode=EXTENDED)
chosen_items.pack(side=LEFT, fill=Y)
scroll = Scrollbar(chosen_frame, command=chosen_items.yview)
scroll.pack(side=LEFT, fill=Y)
chosen_items.config(yscrollcommand=scroll.set)

center_frame = LabelFrame(text="Frame Center")
center_frame.pack(fill=BOTH)

left_frame = LabelFrame(center_frame, text="Frame Left")
left_frame.pack(side=LEFT, fill=BOTH, expand=1)

Button(left_frame, text="Up to 1", command=up_to_1).pack(side=LEFT, expand=1)
Button(left_frame, text="Down to 3", command=down_to_3).pack(side=LEFT, expand=1)

right_frame = LabelFrame(center_frame, text="Frame Right")
right_frame.pack(side=LEFT, fill=BOTH, expand=1)

Button(right_frame, text="Up to 2", command=up_to_2).pack(side=LEFT, expand=1)
Button(right_frame, text="Down to 3", command=two_to_3).pack(side=LEFT, expand=1)

text_frame = LabelFrame(text="Frame Text")
text_frame.pack(fill=BOTH)

text_entry = Entry(text_frame)
text_entry.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()

# Task #12-2

# from tkinter import *
#
# groceries_list = ["apple", "banana", "meat", "fish", "bread", "cheese", "candy", "milk", "potato", "cucumber",
#                   "coffee", "pears", "strawberry"]
#
#
# def add_to_list():
#     pass
#
#     # selected_list = list_items.curselection() # did not work without adding the variable!
#     #
#     # if list_items.curselection():
#     #     for item in range(len(list_items.curselection())):
#     #         chosen_items.insert(END, list_items.get(selected_list[0]))
#     #         list_items.delete(selected_list[0])
#
#
# def return_back():
#     pass
#
#     # return_list = chosen_items.curselection()
#     #
#     # if chosen_items.curselection():
#     #     for item in range(len(chosen_items.curselection())):
#     #         list_items.insert(END, chosen_items.get(return_list[0]))
#     #         chosen_items.delete(return_list[0])
#
#
# def create_header():
#     header_frame = LabelFrame(text="Frame Header")
#     header_frame.pack(fill=Y)
#
#     listbox_frame = Frame(header_frame)
#     listbox_frame.pack(side=LEFT, fill=Y, expand=1)
#
#     list_items = Listbox(listbox_frame, selectmode=EXTENDED)
#     list_items.pack(side=LEFT, fill=Y)
#     scroll = Scrollbar(listbox_frame, command=list_items.yview)
#     scroll.pack(side=LEFT, fill=Y)
#     list_items.config(yscrollcommand=scroll.set)
#
#     for element in range(len(groceries_list)):
#         list_items.insert(END, groceries_list[element])
#
#     button_frame = LabelFrame(header_frame, text="Frame Button")
#     button_frame.pack(side=LEFT)
#
#     Button(button_frame, text=">>>", command=add_to_list).pack()
#     Button(button_frame, text="<<<", command=return_back).pack()
#
#     right_frame = Frame(header_frame)
#     right_frame.pack(fill=Y)
#
#     chosen_frame = Frame(right_frame)
#     chosen_frame.pack(fill=Y, expand=1)
#
#     chosen_items = Listbox(chosen_frame, selectmode=EXTENDED)
#     chosen_items.pack(side=LEFT, fill=Y)
#     scroll = Scrollbar(chosen_frame, command=chosen_items.yview)
#     scroll.pack(side=LEFT, fill=Y)
#     chosen_items.config(yscrollcommand=scroll.set)
#
#
# def create_center():
#     center_frame = LabelFrame(text="Frame Center")
#     center_frame.pack(fill=BOTH)
#
#     left_frame = LabelFrame(center_frame, text="Frame Left")
#     left_frame.pack(side=LEFT, fill=BOTH, expand=1)
#
#     Button(left_frame, text="Up to 1").pack(side=LEFT, expand=1)
#     Button(left_frame, text="Down to 3").pack(side=LEFT, expand=1)
#
#     right_frame = LabelFrame(center_frame, text="Frame Right")
#     right_frame.pack(side=LEFT, fill=BOTH, expand=1)
#
#     Button(right_frame, text="Up to 2").pack(side=LEFT, expand=1)
#     Button(right_frame, text="Down to 3").pack(side=LEFT, expand=1)
#
#
# def create_footer():
#     text_frame = LabelFrame(text="Frame Text")
#     text_frame.pack(fill=BOTH)
#
#     text_entry = Entry(text_frame)
#     text_entry.pack(side=LEFT, fill=BOTH, expand=1)
#
#
# root = Tk()
#
# create_footer()
# create_header()
# create_center()
#
#
# root.mainloop()