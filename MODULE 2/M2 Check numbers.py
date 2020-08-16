from tkinter import *

checks_list = ["is_int_positive",
               "is_int_negative",
               "is_float_positive",
               "is_float_negative",
               "is_number_positive",
               "is_number_negative",
               "is_any_number"]


def is_int_positive(event, widgets):

    widgets[1].config(text=str(widgets[0].get().isdigit()))


root = Tk()

for row, item in enumerate(checks_list):
    Label(text=item, anchor=W).grid(column=0, row=row)
    entry_1 = Entry()
    entry_1.grid(column=1, row=row)
    label_2 = Label()
    label_2.grid(column=3, row=row)
    entry_1.bind('<Return>', lambda event, widgets=[entry_1, label_2]: is_int_positive(event, widgets))

root.mainloop()

# TO DO:

# remove spaces
# concentrate on negative check
