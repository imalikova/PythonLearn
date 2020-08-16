from tkinter import *
from tkinter import filedialog

root = Tk()

op = filedialog.askopenfilename()
print(op)

sa = filedialog.asksaveasfilename()
print(sa)

root.mainloop()