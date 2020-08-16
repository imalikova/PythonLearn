from tkinter import *
from tkinter.ttk import *

root = Tk()

rows = [1, 2, 3, 4, 5, 6, 7]
columns = [1, 2, 3, 4, 5, 6]
heading_labels = ["Product", "Quantity", "Price/Unit", "Days", "", "Total price"]


# row 1 heading

for heading, column in zip(heading_labels, columns):
    Label(text=heading, width=4, justify=CENTER).grid(column=column, row=1, sticky=NSEW)


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

Button(text="=").grid(row=5, column=4, sticky=NSEW)

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

Button(text="=").grid(row=7, column=4, sticky=NSEW)

cell_76 = Entry(text="", justify=RIGHT)
cell_76.grid(row=7, column=6, sticky=NSEW)

root.mainloop()
