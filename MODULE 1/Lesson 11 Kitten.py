from tkinter import *
from tkinter.ttk import *


def calculate_row_2():

    cell_26.delete(0, END)

    if cell_24.get() == "0":

        cell_26.insert(END, "divide by zero!")

    elif cell_22.get() and cell_22.get().isnumeric() and (
            cell_22.get()[0] == '-' or not cell_22.get().isalpha()) and cell_23.get() and (
            cell_23.get().isnumeric()) and (
            cell_23.get()[0] == '-' or not cell_23.get().isalpha()) and cell_24.get() and (
                    cell_24.get().isnumeric() and (cell_24.get()[0] == '-' or not cell_24.get().isalpha())):

        cell_26.insert(END, float(cell_22.get()) * float(cell_23.get()) / float(cell_24.get()))

    else:
        cell_26.insert(END, "unexpected input")


def calculate_row_3():
    cell_36.delete(0, END)

    if cell_34.get() == "0":

        cell_36.insert(END, "divide by zero!")

    elif cell_32.get() and cell_32.get().isnumeric() and (
            cell_32.get()[0] == '-' or not cell_32.get().isalpha()) and cell_33.get() and (
            cell_33.get().isnumeric()) and (
            cell_33.get()[0] == '-' or not cell_33.get().isalpha()) and cell_34.get() and (
            cell_34.get().isnumeric() and (cell_34.get()[0] == '-' or not cell_34.get().isalpha())):

        cell_36.insert(END, float(cell_32.get()) * float(cell_33.get()) / float(cell_34.get()))

    else:
        cell_36.insert(END, "unexpected input")


def calculate_row_4():
    cell_46.delete(0, END)

    if cell_44.get() == "0":

        cell_46.insert(END, "divide by zero!")

    elif cell_42.get() and cell_42.get().isnumeric() and (
            cell_42.get()[0] == '-' or not cell_42.get().isalpha()) and cell_43.get() and (
            cell_43.get().isnumeric()) and (
            cell_43.get()[0] == '-' or not cell_43.get().isalpha()) and cell_44.get() and (
            cell_44.get().isnumeric() and (cell_44.get()[0] == '-' or not cell_44.get().isalpha())):

        cell_46.insert(END, float(cell_42.get()) * float(cell_43.get()) / float(cell_44.get()))

    else:
        cell_46.insert(END, "unexpected input")


def calculate_cost_year():
    cell_56.delete(0, END)
    calculate_row_2()
    calculate_row_3()
    calculate_row_4()
    cell_56.insert(END, (float(cell_26.get()) + float(cell_36.get()) + float(cell_46.get())) * 365)


def calculate_grand_total():
    cell_76.delete(0, END)
    if cell_66.get() and cell_66.get().isnumeric() and (
            cell_66.get()[0] == '-' or not cell_66.get().isalpha()):
            cell_76.insert(END, float(cell_56.get()) * float(cell_66.get()))

    else:
        cell_76.insert(END, "unexpected input")


root = Tk()

# row 1 heading

product = Label(text="Product", justify=CENTER)
product.grid(column=1, row=1, sticky=NSEW)

quantity = Label(text="Quantity", justify=CENTER)
quantity.grid(column=2, row=1, sticky=NSEW)

unitprice = Label(text="Price/Unit", justify=CENTER)
unitprice.grid(column=3, row=1, sticky=NSEW)

days = Label(text="Days", justify=CENTER)
days.grid(column=4, row=1, sticky=NSEW)

empty = Label(text="", justify=CENTER)
empty.grid(column=5, row=1, sticky=NSEW)

total_price = Label(text="Total price", justify=CENTER)
total_price.grid(column=6, row=1, sticky=NSEW)

# row 2


num_21 = StringVar()
num_21.set("Cat's food")
cell_21 = Entry(textvariable=num_21)
cell_21.grid(row=2, column=1, sticky=NSEW)

num_22 = StringVar()
num_22.set(5)
cell_22 = Entry(textvariable=num_22, justify=RIGHT)
cell_22.grid(row=2, column=2, sticky=NSEW)

num_23 = StringVar()
num_23.set(4)
cell_23 = Entry(textvariable=num_23, justify=RIGHT)
cell_23.grid(row=2, column=3, sticky=NSEW)

num_24 = StringVar()
num_24.set(3)
cell_24 = Entry(textvariable=num_24, justify=RIGHT)
cell_24.grid(row=2, column=4, sticky=NSEW)

# Button(text="=", command=calculate_row_2).grid(row=2, column=5, sticky=NSEW)

cell_26 = Entry(justify=RIGHT)
cell_26.grid(row=2, column=6, sticky=NSEW)

# row 3

num_31 = StringVar()
num_31.set("Toilet fill")
cell_31 = Entry(textvariable=num_31)
cell_31.grid(row=3, column=1, sticky=NSEW)

num_32 = StringVar()
num_32.set(5)
cell_32 = Entry(textvariable=num_32, justify=RIGHT)
cell_32.grid(row=3, column=2, sticky=NSEW)


num_33 = StringVar()
num_33.set(4)
cell_33 = Entry(textvariable=num_33, justify=RIGHT)
cell_33.grid(row=3, column=3, sticky=NSEW)

num_34 = StringVar()
num_34.set(3)
cell_34 = Entry(textvariable=num_34, justify=RIGHT)
cell_34.grid(row=3, column=4, sticky=NSEW)

# Button(text="=", command=calculate_row_3).grid(row=3, column=5, sticky=NSEW)

cell_36 = Entry(justify=RIGHT)
cell_36.grid(row=3, column=6, sticky=NSEW)

# row 4

num_41 = StringVar()
num_41.set("Vitamins")
cell_41 = Entry(textvariable=num_41)
cell_41.grid(row=4, column=1, sticky=NSEW)


num_42 = StringVar()
num_42.set(5)
cell_42 = Entry(textvariable=num_42, justify=RIGHT)
cell_42.grid(row=4, column=2, sticky=NSEW)

num_43 = StringVar()
num_43.set(4)
cell_43 = Entry(textvariable=num_43, justify=RIGHT)
cell_43.grid(row=4, column=3, sticky=NSEW)

num_44 = StringVar()
num_44.set(3)
cell_44 = Entry(textvariable=num_44, justify=RIGHT)
cell_44.grid(row=4, column=4, sticky=NSEW)

# Button(text="=", command=calculate_row_4).grid(row=4, column=5, sticky=NSEW)

cell_46 = Entry(justify=RIGHT)
cell_46.grid(row=4, column=6, sticky=NSEW)

# row 5

cost_year = Label(text="Total cost per year", justify=RIGHT)
cost_year.grid(row=5, column=1, sticky=NSEW, columnspan=4)

Button(text="=", command=calculate_cost_year).grid(row=5, column=4, sticky=NSEW)

cell_56 = Entry(text="", justify=RIGHT)
cell_56.grid(row=5, column=6, sticky=NSEW)

# row 6

years = Label(text="Years", justify=RIGHT)
years.grid(row=6, column=1, sticky=NSEW, columnspan=5)

cell_66 = Entry(text="", justify=RIGHT)
cell_66.grid(row=6, column=6, sticky=NSEW)

# row 7

years = Label(text="Grand Total", justify=RIGHT)
years.grid(row=7, column=1, sticky=NSEW, columnspan=4)

Button(text="=", command=calculate_grand_total).grid(row=7, column=4, sticky=NSEW)

cell_76 = Entry(text="", justify=RIGHT)
cell_76.grid(row=7, column=6, sticky=NSEW)

root.mainloop()






