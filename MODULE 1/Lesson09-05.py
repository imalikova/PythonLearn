# Создайте программу с двумя кнопками растягиваемые по горизонтали,
# прикрепленными к верхней и нижней границам окна.

from tkinter import *

root = Tk()
btn1 = Button(root, text="Button 1")
btn1.pack(side=TOP, fill=X)
btn2 = Button(root, text="Button 2")
btn2.pack(side=BOTTOM, fill=X)

root.mainloop()