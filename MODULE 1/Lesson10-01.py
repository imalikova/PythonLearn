from tkinter import *

def sum_numbers():
    sum_field_result.delete(0,END)

    #check that fields are not letters and not empty


    if sum_field_1.get() and sum_field_1.get().isnumeric() and (
                sum_field_1.get()[0] == '-' or not sum_field_1.get().isalpha()) and sum_field_2.get() and (
                sum_field_2.get().isnumeric() and (sum_field_2.get()[0] == '-' or not sum_field_2.get().isalpha())):

        sum_field_result.insert(END, int(sum_field_1.get())+int(sum_field_2.get()))

    else:
        sum_field_result.insert(END, "unexpected input")

def subtract_numbers():

    subtract_field_result.delete(0, END)

    print(bool(subtract_field_1.get() and subtract_field_2.get()))

    if subtract_field_1.get() and subtract_field_1.get().isnumeric() and (
            subtract_field_1.get()[0] == '-' or not subtract_field_1.get().isalpha()) and subtract_field_2.get() and (
            subtract_field_2.get().isnumeric() and (subtract_field_2.get()[0] == '-' or not subtract_field_2.get().isalpha())):

        subtract_field_result.insert(END, int(subtract_field_1.get()) - int(subtract_field_2.get()))

    else:
        subtract_field_result.insert(END, "unexpected input")

def multiply_numbers():

    multiply_field_result.delete(0, END)

    print(bool(multiply_field_1.get() and multiply_field_2.get()))

    if multiply_field_1.get() and multiply_field_1.get().isnumeric() and (
            multiply_field_1.get()[0] == '-' or not multiply_field_1.get().isalpha()) and multiply_field_2.get() and (
            multiply_field_2.get().isnumeric() and (
            multiply_field_2.get()[0] == '-' or not multiply_field_2.get().isalpha())):

        multiply_field_result.insert(END, int(multiply_field_1.get()) * int(multiply_field_2.get()))

    else:
        subtract_field_result.insert(END, "unexpected input")

def divide_numbers():

    divide_field_result.delete(0, END)

    print(bool(divide_field_1.get() and divide_field_2.get()))

    if divide_field_2.get() == "0":

        divide_field_result.insert(END, "division by zero!")

    elif divide_field_1.get() and divide_field_1.get().isnumeric() and (

            divide_field_1.get()[0] == '-' or not divide_field_1.get().isalpha()) and divide_field_2.get() and (

            divide_field_2.get().isnumeric() and (

            divide_field_2.get()[0] == '-' or not divide_field_2.get().isalpha())):

            divide_field_result.insert(END, int(divide_field_1.get()) / int(divide_field_2.get()))


    else:
        divide_field_result.insert(END, "unexpected input")

root = Tk()

#sum

sum_field_1 = Entry()
sum_field_1.grid(column=0, row=0)

Label(text="+").grid(column=1, row=0)

sum_field_2 = Entry()
sum_field_2.grid(column=2, row=0)

Button(text="=", command=sum_numbers).grid(column=3, row=0)

sum_field_result = Entry()
sum_field_result.grid(column=4, row=0)

#subtract

subtract_field_1 = Entry()
subtract_field_1.grid(column=0, row=1)

Label(text="-").grid(column=1, row=1)

subtract_field_2 = Entry()
subtract_field_2.grid(column=2, row=1)

Button(text="=", command=subtract_numbers).grid(column=3, row=1)

subtract_field_result = Entry()
subtract_field_result.grid(column=4, row=1)

# multiplication

multiply_field_1 = Entry()
multiply_field_1.grid(column=0, row=2)

Label(text="*").grid(column=1, row=2)

multiply_field_2 = Entry()
multiply_field_2.grid(column=2, row=2)

Button(text="=", command=multiply_numbers).grid(column=3, row=2)

multiply_field_result = Entry()
multiply_field_result.grid(column=4, row=2)

# division

divide_field_1 = Entry()
divide_field_1.grid(column=0, row=3)

Label(text="/").grid(column=1, row=3)

divide_field_2 = Entry()
divide_field_2.grid(column=2, row=3)

Button(text="=", command=divide_numbers).grid(column=3, row=3)

divide_field_result = Entry()
divide_field_result.grid(column=4, row=3)

root.mainloop()


root = Tk()

# a = "cat"
#
#
# print(f"variable a is positive integer {a.isnumeric()}")
# print(f"variable a is negative integer {a[0]=='-' and a[1:].isnumeric()}")
# print(f"variable a is total integer {a[0]=='-' and a[1:].isnumeric() or a.isnumeric()}")
# print(f"variable is string {a.isalpha()}")
# print(f"variable is not string {not a.isalpha()}")
# print(f"variable is integer and not string {a.isnumeric() and not a.isalpha()}")
#
# print((a.isnumeric() or a[0]=='-' and a[1:].isnumeric()) or not a.isalpha())
#
#
# (sum_field_1.get().isnumeric() or sum_field_1.get() and sum_field_1.get()[0]=='-' or not sum_field_1.get().isalpha()) and
# (sum_field_2.get().isnumeric() or sum_field_2.get() and sum_field_2.get()[0]=='-' or not sum_field_2.get().isalpha())

# print(a.isnumeric())
# print(a[0]=="-" and a[1:].isnumeric())
# print(a[1:])
#
# print(a.islower())
# print(a.isalpha())
# # print(a.__dir__())
# print(root.__dir__())
#
# # root.mainloop()