from tkinter import *
from tkinter.ttk import *


def add_elements(event):
    if entry.get():
        list_items.insert(END, entry.get())
        entry.delete(0, END)


def delete_items(event):

    for item in list_items.curselection()[::-1]:
        list_items.delete(item)


root = Tk()

entry = Entry()
entry.bind('<Return>', add_elements)
entry.pack()

list_items = Listbox(selectmode=EXTENDED)
list_items.pack()
scroll = Scrollbar(command=list_items.yview)
scroll.pack(fill=Y)
list_items.config(yscrollcommand=scroll.set)

list_items.bind('<a>', delete_items)


root.mainloop()

