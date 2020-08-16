# Создайте программу с тремя копками: 1, 2, 3.
# Расположите строчкой: 1, 2, 3 с привязкой к левому краю окна.

from tkinter import *

root = Tk()
btn1 = Button(root, text="Button 1")
btn1.pack(side=LEFT)
btn2 = Button(root, text="Button 2")
btn2.pack(side=LEFT)
btn3 = Button(root, text="Button 2")
btn3.pack(side=LEFT)

root.mainloop()