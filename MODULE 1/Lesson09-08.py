# Создайте четыре программы с кнопкой, которая будет привязана к углу окна.
# И при увеличении размеров окна виджет продолжит оставаться в том же углу:
#
# в левом верхнем углу окна;
# в правом верхнем углу окна;
# в левом нижнем углу окна;
# в правом нижнем углу окна;


from tkinter import *

root = Tk()
btn1 = Button(root, text="Button 1")
btn1.pack(anchor=NW)

root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 2")
# btn1.pack(anchor=NE)
#
# root.mainloop()
#
#
# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 3")
# btn1.pack(side=BOTTOM, anchor=SW)
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 4")
# btn1.pack(side=BOTTOM, anchor=SE)
#
# root.mainloop()