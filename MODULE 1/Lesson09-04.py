# Создайте программу с тремя копками: 1, 2, 3. Расположите строчкой: 3, 2, 1 с привязкой к правому краю окна.
# Разверните окно на всей экран и проверьте корректность отображения.

from tkinter import *

root = Tk()
btn1 = Button(root, text="Button 1")
btn1.pack(side=RIGHT)
btn2 = Button(root, text="Button 2")
btn2.pack(side=RIGHT)
btn3 = Button(root, text="Button 2")
btn3.pack(side=RIGHT)

root.mainloop()