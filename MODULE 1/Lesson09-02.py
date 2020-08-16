# Создайте программу с тремя копками: 1, 2, 3.
# Расположите сверху вниз столбиком: 3, 2, 1 с привязкой к нижнему краю окна.


from tkinter import *

root = Tk()
btn1 = Button(root, text="Button 1")
btn1.pack(side=BOTTOM)
btn2 = Button(root, text="Button 2")
btn2.pack(side=BOTTOM)
btn3 = Button(root, text="Button 2")
btn3.pack(side=BOTTOM)

root.mainloop()