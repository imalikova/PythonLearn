# Напишите программу с кнопкой растягивающейся на всё окно, независимо от размера окна.

from tkinter import *

root = Tk()
btn1 = Button(root, text="Button 1")
btn1.pack(expand=1, fill=BOTH)


root.mainloop()