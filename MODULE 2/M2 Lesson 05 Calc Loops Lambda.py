from tkinter import *
import operator

list_widgets = []

#
# def sum_numbers():
#     sum_field_result.delete(0,END)
#
#     #check that fields are not letters and not empty
#
#
#     if sum_field_1.get() and sum_field_1.get().isnumeric() and (
#                 sum_field_1.get()[0] == '-' or not sum_field_1.get().isalpha()) and sum_field_2.get() and (
#                 sum_field_2.get().isnumeric() and (sum_field_2.get()[0] == '-' or not sum_field_2.get().isalpha())):
#
#         sum_field_result.insert(END, int(sum_field_1.get())+int(sum_field_2.get()))
#
#     else:
#         sum_field_result.insert(END, "unexpected input")
#
#
# def subtract_numbers():
#
#     subtract_field_result.delete(0, END)
#
#
#     if subtract_field_1.get() and subtract_field_1.get().isnumeric() and (
#             subtract_field_1.get()[0] == '-' or not subtract_field_1.get().isalpha()) and subtract_field_2.get() and (
#             subtract_field_2.get().isnumeric() and (subtract_field_2.get()[0] == '-' or not subtract_field_2.get().isalpha())):
#
#         subtract_field_result.insert(END, int(subtract_field_1.get()) - int(subtract_field_2.get()))
#
#     else:
#         subtract_field_result.insert(END, "unexpected input")
#
#
# def multiply_numbers():
#
#     multiply_field_result.delete(0, END)
#
#     if multiply_field_1.get() and multiply_field_1.get().isnumeric() and (
#             multiply_field_1.get()[0] == '-' or not multiply_field_1.get().isalpha()) and multiply_field_2.get() and (
#             multiply_field_2.get().isnumeric() and (
#             multiply_field_2.get()[0] == '-' or not multiply_field_2.get().isalpha())):
#
#         multiply_field_result.insert(END, int(multiply_field_1.get()) * int(multiply_field_2.get()))
#
#     else:
#         subtract_field_result.insert(END, "unexpected input")
#
#
# def divide_numbers():
#
#     divide_field_result.delete(0, END)
#
#     print(bool(divide_field_1.get() and divide_field_2.get()))
#
#     if divide_field_2.get() == "0":
#
#         divide_field_result.insert(END, "division by zero!")
#
#     elif divide_field_1.get() and divide_field_1.get().isnumeric() and (
#
#             divide_field_1.get()[0] == '-' or not divide_field_1.get().isalpha()) and divide_field_2.get() and (
#
#             divide_field_2.get().isnumeric() and (
#
#             divide_field_2.get()[0] == '-' or not divide_field_2.get().isalpha())):
#
#             divide_field_result.insert(END, int(divide_field_1.get()) / int(divide_field_2.get()))
#
#     else:
#         divide_field_result.insert(END, "unexpected input")

operators_list = ["+", "-", "*", "%"]

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "%": operator.mod,
}


def calculate_result(operation, row):
    field_result.delete(0, END)
    field_result[row].insert(END, ops[operation](int(field_1.get(), int(field_2.get()))))


root = Tk()

for row, operation in enumerate(operators_list):
    Label(text=operation).grid(column=1, row=row)
    list_widgets.append(row)

    Button(text="=", command=lambda par_1=operation, par_2=list_widgets[row]: calculate_result(par_1, par_2)).grid(column=3, row=row)


for row in range(4):
    num_1 = StringVar()
    field_1 = Entry(textvariable=num_1)
    field_1.grid(column=0, row=row)

    num_2 = StringVar()
    field_2 = Entry(textvariable=num_2)
    field_2.grid(column=2, row=row)

    field_result = Entry()
    field_result.grid(column=4, row=row)


root.mainloop()

# from tkinter import *
#
#
# def print_entry():
#     print(entry_1.get())
#
#
# root = Tk()
#
# for row in range(3):
#     entry_1 = Entry()
#     entry_1.grid(column=0, row=row)
#
#     button_1 = Button(text=row, command=print_entry)
#     button_1.grid(column=1, row=row)
#
# root.mainloop()


# from tkinter import *
#
#
# def print_entry(text):
#     print(text)
#
#
# root = Tk()
#
# for row in range(3):
#     entry_1 = Entry()
#     entry_1.grid(column=0, row=row)
#
#     button_1 = Button(text=row, command=lambda widget=entry_1: print_entry(widget.get())) # save the widget not value (in lambda) but set the value
#     button_1.grid(column=1, row=row)
#
# root.mainloop()


# from tkinter import *
#
#
# def print_entry(text):
#     print(text)
#
#
# root = Tk()
#
# for row in range(3):
#     num_1 = StringVar()
#     entry_1 = Entry(textvariable=num_1)
#     entry_1.grid(column=0, row=row)
#
#     button_1 = Button(text=row, command=lambda value=num_1: print_entry(value.get())) # save the widget not value (in lambda) but set the value
#     button_1.grid(column=1, row=row)
#
# root.mainloop()


# from tkinter import *
#
# list_widgets = []
#
#
# def print_entry(text):
#     print(text)
#
#
# root = Tk()
#
# for row in range(3):
#     num_1 = StringVar()
#     entry_1 = Entry(textvariable=num_1)
#     entry_1.grid(column=0, row=row)
#     list_widgets.append(entry_1) #add widget to list
#
#     button_1 = Button(text=row, command=lambda value=list_widgets[row]: print_entry(value.get())) # save the widget not value (in lambda) but set the value
#     button_1.grid(column=1, row=row)
#
# root.mainloop()
#
#
