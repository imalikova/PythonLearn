# from tkinter import *
#
# groceries_list = ["apple", "banana", "meat", "fish", "bread", "cheese", "candy", "milk", "potato", "cucumber",
#                   "coffee", "pears", "strawberry"]
#
#
# def move_left_to_right():
#     selected_list = list_left.curselection()
#
#     if list_left.curselection():
#         for item in selected_list:
#             list_right.insert(END, list_left.get(item))
#         for item in selected_list[::-1]:
#             list_left.delete(item)
#
#
# def move_right_to_left():
#     selected_list = list_right.curselection()
#
#     if list_right.curselection():
#         for item in selected_list:
#             list_left.insert(END, list_right.get(item))
#         for item in selected_list[::-1]:
#             list_right.delete(item)
#
#
# root = Tk()
#
# header_frame = LabelFrame(text="Frame Header")
# header_frame.pack(fill=Y)
#
# listbox_frame = Frame(header_frame)
# listbox_frame.pack(side=LEFT, fill=Y, expand=1)
#
#
# list_left = Listbox(listbox_frame, selectmode=EXTENDED)
# list_left.pack(side=LEFT, fill=Y)
# scroll = Scrollbar(listbox_frame, command=list_left.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_left.config(yscrollcommand=scroll.set)
#
# for element in range(len(groceries_list)):
#     list_left.insert(END, groceries_list[element])
#
#
# button_frame = LabelFrame(header_frame, text="Frame Button")
# button_frame.pack(side=LEFT)
#
# Button(button_frame, text=">>>", command=move_left_to_right).pack()
# Button(button_frame, text="<<<", command=move_right_to_left).pack()
#
#
# right_frame = Frame(header_frame)
# right_frame.pack(fill=Y)
#
# chosen_frame = Frame(right_frame)
# chosen_frame.pack(fill=Y, expand=1)
#
#
# list_right = Listbox(chosen_frame, selectmode=EXTENDED)
# list_right.pack(side=LEFT, fill=Y)
# scroll = Scrollbar(chosen_frame, command=list_right.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_right.config(yscrollcommand=scroll.set)
#
# root.mainloop()


# from tkinter import *
#
# groceries_list = ["apple", "banana", "meat", "fish", "bread", "cheese", "candy", "milk", "potato", "cucumber",
#                   "coffee", "pears", "strawberry"]
#
#
# def move_to(direction):
#     if direction == "left":
#         move_right_to_left()
#     elif direction == "right":
#         move_left_to_right()
#
#
# def move_left_to_right():
#     selected_list = list_left.curselection()
#
#     if list_left.curselection():
#         for item in selected_list:
#             list_right.insert(END, list_left.get(item))
#         for item in selected_list[::-1]:
#             list_left.delete(item)
#
#
# def move_right_to_left():
#     selected_list = list_right.curselection()
#
#     if list_right.curselection():
#         for item in selected_list:
#             list_left.insert(END, list_right.get(item))
#         for item in selected_list[::-1]:
#             list_right.delete(item)
#
#
# root = Tk()
#
# header_frame = LabelFrame(text="Frame Header")
# header_frame.pack(fill=Y)
#
# listbox_frame = Frame(header_frame)
# listbox_frame.pack(side=LEFT, fill=Y, expand=1)
#
#
# list_left = Listbox(listbox_frame, selectmode=EXTENDED)
# list_left.pack(side=LEFT, fill=Y)
# scroll = Scrollbar(listbox_frame, command=list_left.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_left.config(yscrollcommand=scroll.set)
#
# for element in range(len(groceries_list)):
#     list_left.insert(END, groceries_list[element])
#
#
# button_frame = LabelFrame(header_frame, text="Frame Button")
# button_frame.pack(side=LEFT)
#
# Button(button_frame, text=">>>", command=lambda: move_to("right")).pack()
# Button(button_frame, text="<<<", command=lambda: move_to("left")).pack()
#
#
# right_frame = Frame(header_frame)
# right_frame.pack(fill=Y)
#
# chosen_frame = Frame(right_frame)
# chosen_frame.pack(fill=Y, expand=1)
#
#
# list_right = Listbox(chosen_frame, selectmode=EXTENDED)
# list_right.pack(side=LEFT, fill=Y)
# scroll = Scrollbar(chosen_frame, command=list_right.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_right.config(yscrollcommand=scroll.set)
#
# root.mainloop()


# from tkinter import *
#
# groceries_list = ["apple", "banana", "meat", "fish", "bread", "cheese", "candy", "milk", "potato", "cucumber",
#                   "coffee", "pears", "strawberry"]
#
#
# def move_to(direction):
#     if direction == "left":
#         move_to_direction(list_right, list_left)
#     elif direction == "right":
#         move_to_direction(list_left, list_right)
#
#
# def move_to_direction(list_from, list_to):
#     selected_list = list_from.curselection()
#
#     if list_from.curselection():
#         for item in selected_list:
#             list_to.insert(END, list_from.get(item))
#         for item in selected_list[::-1]:
#             list_from.delete(item)
#
#
# root = Tk()
#
# header_frame = LabelFrame(text="Frame Header")
# header_frame.pack(fill=Y)
#
# listbox_frame = Frame(header_frame)
# listbox_frame.pack(side=LEFT, fill=Y, expand=1)
#
#
# list_left = Listbox(listbox_frame, selectmode=EXTENDED)
# list_left.pack(side=LEFT, fill=Y)
# scroll = Scrollbar(listbox_frame, command=list_left.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_left.config(yscrollcommand=scroll.set)
#
# for element in range(len(groceries_list)):
#     list_left.insert(END, groceries_list[element])
#
#
# button_frame = LabelFrame(header_frame, text="Frame Button")
# button_frame.pack(side=LEFT)
#
# Button(button_frame, text=">>>", command=lambda: move_to("right")).pack()
# Button(button_frame, text="<<<", command=lambda: move_to("left")).pack()
#
#
# right_frame = Frame(header_frame)
# right_frame.pack(fill=Y)
#
# chosen_frame = Frame(right_frame)
# chosen_frame.pack(fill=Y, expand=1)
#
#
# list_right = Listbox(chosen_frame, selectmode=EXTENDED)
# list_right.pack(side=LEFT, fill=Y)
# scroll = Scrollbar(chosen_frame, command=list_right.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_right.config(yscrollcommand=scroll.set)
#
# root.mainloop()


# from tkinter import *
#
# groceries_list = ["apple", "banana", "meat", "fish", "bread", "cheese", "candy", "milk", "potato", "cucumber",
#                   "coffee", "pears", "strawberry"]
#
#
# def move_to_direction(list_from, list_to):
#     selected_list = list_from.curselection()
#
#     if list_from.curselection():
#
#         for item in selected_list:
#             list_to.insert(END, list_from.get(item))
#         for item in selected_list[::-1]:
#             list_from.delete(item)
#
#
# root = Tk()
#
# header_frame = LabelFrame(text="Frame Header")
# header_frame.pack(fill=Y)
#
# listbox_frame = Frame(header_frame)
# listbox_frame.pack(side=LEFT, fill=Y, expand=1)
#
#
# list_left = Listbox(listbox_frame, selectmode=EXTENDED)
# list_left.pack(side=LEFT, fill=Y)
# scroll = Scrollbar(listbox_frame, command=list_left.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_left.config(yscrollcommand=scroll.set)
#
# for element in range(len(groceries_list)):
#     list_left.insert(END, groceries_list[element])
#
#
# button_frame = LabelFrame(header_frame, text="Frame Button")
# button_frame.pack(side=LEFT)
#
# right_frame = Frame(header_frame)
# right_frame.pack(fill=Y)
#
# chosen_frame = Frame(right_frame)
# chosen_frame.pack(fill=Y, expand=1)
#
#
# list_right = Listbox(chosen_frame, selectmode=EXTENDED)
# list_right.pack(side=LEFT, fill=Y)
# scroll = Scrollbar(chosen_frame, command=list_right.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_right.config(yscrollcommand=scroll.set)
#
# Button(button_frame, text=">>>", command=lambda: move_to_direction(list_left, list_right)).pack()
# Button(button_frame, text="<<<", command=lambda: move_to_direction(list_right, list_left)).pack()
#
# root.mainloop()
#


# from tkinter import *
# from tkinter.ttk import *
#
#
# def button_click():
#     print("button click")
#
#
# root = Tk()
#
# for number in range(5):
#
#     Button(text=number, command=button_click).pack()
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def button_click(number):
#     print(f"{number} button click")
#
#
# root = Tk()
#
# Button(text=0, command=lambda: button_click(0)).pack()
# Button(text=1, command=lambda: button_click(1)).pack()
# Button(text=2, command=lambda: button_click(2)).pack()
# Button(text=3, command=lambda: button_click(3)).pack()
# Button(text=4, command=lambda: button_click(4)).pack()
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def button_click(number, color):
#     print(f"{number} and {color} button click")
#
#
# root = Tk()
#
# Button(text=0, command=lambda: button_click(0, "red")).pack()
# Button(text=1, command=lambda: button_click(1, "orange")).pack()
# Button(text=2, command=lambda: button_click(2, "yellow")).pack()
# Button(text=3, command=lambda: button_click(3, "green")).pack()
# Button(text=4, command=lambda: button_click(4, "blue")).pack()
#
# root.mainloop()

#
# from tkinter import *
# # from tkinter.ttk import *
#
# colors = ["red", "orange", "yellow", "green", "blue"]
#
#
# def button_click(number, color):
#     label.config(text=f"{color} and {number}", bg=color)
#
#
# root = Tk()
#
# label = Label(text="text")
# label.pack()
#
# for index, color in enumerate(colors):
#
#     Button(text=color, command=lambda par_1=index, par_2=color: button_click(par_1, par_2)).pack()
#
#
#
# root.mainloop()


# import tkinter as tk # short library name
# import tkinter.ttk as ttk
#
#
# colors = ["red", "orange", "yellow", "green", "blue"]
#
#
# def button_click(number, color):
#     label.config(text=f"{color} and {number}", bg=color)
#
#
# root = tk.Tk()
#
# label = tk.Label(text="text")
# label.pack()
#
# for index, color in enumerate(colors):
#
#     ttk.Button(text=color, command=lambda par_1=index, par_2=color: button_click(par_1, par_2)).pack()
#
#
# root.mainloop()


import tkinter as tk  # short library name
import tkinter.ttk as ttk

colors = ["red", "orange", "yellow", "green", "blue"]


def button_click(number, color, button):
    print(button)
    button.config(text=f"{color} and {number}", fg=color)


root = tk.Tk()

for index, color in enumerate(colors):
    button = tk.Button(text=color)
    button.config(command=lambda par_1=index, par_2=color, par_3=button: button_click(par_1, par_2, par_3)) # create the button in 2 steps
    button.pack()

root.mainloop()
