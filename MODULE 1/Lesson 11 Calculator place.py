from tkinter import *
# from tkinter.ttk import *

root = Tk()
root.title("Calculator")
root.resizable(False, False)

# lesson 3 size of window

# screen

num = StringVar()
num.set(0)
Entry(text=num, justify=RIGHT, width=19).place(x=8, y=5)

#row 1 buttons digits

Button(text=1, width=4).place(x=5,y=50)
Button(text=2, width=4).place(x=42,y=50)
Button(text=3, width=4).place(x=79,y=50)
Button(text=4, width=4).place(x=116,y=50)
Button(text=5, width=4).place(x=153,y=50)


# frame row 2 buttons digits

Button(text=6, width=4).place(x=5,y=85)
Button(text=7, width=4).place(x=42,y=85)
Button(text=8, width=4).place(x=79,y=85)
Button(text=9, width=4).place(x=116,y=85)
Button(text=0, width=4).place(x=153,y=85)

# frame row 3 buttons operations

Button(text="+", width=4).place(x=5,y=120)
Button(text="-", width=4).place(x=42,y=120)
Button(text="*", width=4).place(x=79,y=120)
Button(text="/", width=4).place(x=116,y=120)
Button(text="=", width=4).place(x=153,y=120)


root.mainloop()