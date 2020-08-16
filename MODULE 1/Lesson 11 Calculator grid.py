from tkinter import *
# from tkinter.ttk import *

root = Tk()
root.title("Calculator")
root.resizable(False, False)

# screen


num = StringVar()
num.set(0)
Entry(text=num, justify=RIGHT).grid(row=1, column=1, columnspan=5)


# row 1 buttons digits

Button(text=1, width=3).grid(row=3, column=1)
Button(text=2, width=3).grid(row=3, column=2)
Button(text=3, width=3).grid(row=3, column=3)
Button(text=4, width=3).grid(row=3, column=4)
Button(text=5, width=3).grid(row=3, column=5)

# row 2 buttons digits

Button(text=6, width=3).grid(row=5, column=1)
Button(text=7, width=3).grid(row=5, column=2)
Button(text=8, width=3).grid(row=5, column=3)
Button(text=9, width=3).grid(row=5, column=4)
Button(text=0, width=3).grid(row=5, column=5)

# row 3 buttons operations

Button(text="+", width=3).grid(row=7, column=1)
Button(text="-", width=3).grid(row=7, column=2)
Button(text="*", width=3).grid(row=7, column=3)
Button(text="/", width=3).grid(row=7, column=4)
Button(text="=", width=3).grid(row=7, column=5)

root.mainloop()