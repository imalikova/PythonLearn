# Создайте программу с двумя кнопками растягиваемые по вертикали,
# прикрепленными к левой и правой границам окна.

from tkinter import *

root = Tk()
btn1 = Button(root, text="Button 1")
btn1.pack(side=LEFT, fill=Y)
btn2 = Button(root, text="Button 2")
btn2.pack(side=RIGHT, fill=Y)

root.mainloop()