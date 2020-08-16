
from tkinter import *

root = Tk()
root.title("Welcome")


field_entry = Entry()
field_entry.insert(0, "Текстовое поле вводит и выводит текст только одной строкой")

field_entry.pack()
root.mainloop()

