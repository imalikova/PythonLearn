# # task 1
#
# from tkinter import *
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack(expand=1, fill=BOTH)
#
# root.mainloop()


# # task 2
#
# from tkinter import *
#
# def insert_text():
#
#     text.insert(INSERT, "This is a new text!")
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack(expand=1, fill=BOTH)
#
#
# Button(text="Add", command=insert_text).pack()
#
# root.mainloop()

# task 3

# from tkinter import *
#
# buffer = ""
#
#
# def copy_all():
#     global buffer
#     buffer = text.get(1.0, END)
#
#
# def paste_text():
#     global buffer
#     text.insert(1.0, buffer)
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack(expand=1, fill=BOTH)
#
#
# Button(text="Copy all", command=copy_all).pack()
#
# Button(text="Paste", command=paste_text).pack()
#
# root.mainloop()

# task 4
# Copy all - при нажатии на которую, происходит копирование всего текста,
# Copy - при нажатии на которую, происходит копирование выделенного текста,
# Paste - при нажатии на которую, происходит добавление скопированного текста в место расположения курсора.

# from tkinter import *
#
# buffer = ""
#
#
# def copy_all():
#     global buffer
#     buffer = text.get(1.0, END)
#
#
# def copy():
#     global buffer
#     buffer = text.selection_get()
#
#
# def paste_text():
#     global buffer
#     text.insert(END, buffer)
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.pack(expand=1, fill=BOTH)
#
#
# Button(text="Copy all", command=copy_all).pack()
#
# Button(text="Copy", command=copy).pack()
#
# Button(text="Paste", command=paste_text).pack()
#
# root.mainloop()


# task 5
# Copy all - при нажатии, происходит копирование всего текста,
# Copy - при нажатии, происходит копирование выделенного текста;
# Cut - при нажатии, происходит вырезание выделенного текста в буфер;
# Paste - при нажатии, происходит добавление скопированного текста в место расположения курсора.

# from tkinter import *
#
# buffer = ""
#
#
# def copy_all():
#     global buffer
#     buffer = text.get(1.0, END)
#
#
# def copy():
#     global buffer
#     buffer = text.selection_get()
#
#
# def cut():
#     global buffer
#     buffer = text.selection_get()
#     text.delete(SEL_FIRST, SEL_LAST)
#
#
# def paste_text():
#     global buffer
#     text.insert(END, buffer)
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.pack(expand=1, fill=BOTH)
#
#
# Button(text="Copy all", command=copy_all).pack()
#
# Button(text="Copy", command=copy).pack()
#
# Button(text="Cut", command=cut).pack()
#
# Button(text="Paste", command=paste_text).pack()
#
# root.mainloop()


# task 6
# Напишите программу с текстовым полем и строкой состояния, виджеты должны масштабироваться под размер окна. В стоке состояния вывести информацию:
# общее количество символов,
# общее количество строк,
# номер строки, в которой находиться курсор,
# номер символа в строке, в которой находиться курсор.

# from tkinter import *
#
# def get_status():
#
#     print(text.index(INSERT))
#     print(text.index(INSERT)[0])
#     print(text.index(INSERT)[2])
#
#     current_position = text.index(INSERT).split(".")
#
#     print(current_position)
#
#     state.config(text=f"symbols={symbols_qty}, rows = {text.index(INSERT)[0]}, ln {text.index(INSERT)[0]}, col {current_position[1]}")
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, '''Try to write
# any text test test test'''*10)
# text.pack(expand=1, fill=BOTH)
#
#
# symbols_qty = len(text.get(1.0, END))
#
#
#
# state = Label()
# state.pack(fill=X)
#
# initial_position = text.index(INSERT).split(".")
#
# state.config(text=f"symbols={symbols_qty}, rows = {text.index(INSERT)[0]}, ln {text.index(INSERT)[0]}, col {initial_position[1]}")
#
#
# Button(text="update", command=get_status).pack()
#
# root.mainloop()


# task 7

# Напишите программу с текстовым полем и кнопкой отмена действия.
# При нажатии на кнопку будет удаляться последний напечатанный символ.

# from tkinter import *
#
# buffer = ""
#
#
# def delete_symbol():
#     global buffer
#     buffer = text.get(1.0, END)
#     text.delete(1.0, END)
#     text.insert(END, buffer[0:-2])
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....1234")
# text.pack(expand=1, fill=BOTH)
#
#
# Button(text="Cancel", command=delete_symbol).pack()
#
# root.mainloop()


# task 8

# Напишите программу с текстовым полем и кнопкой отмена действия.
# При нажатии на кнопку будет удаляться последнее напечатанное слово.

from tkinter import *

buffer = ""


def delete_word():
    global buffer
    buffer = text.get(1.0, END)
    cut = buffer.split(" ")
    text.delete(1.0, END)
    text.insert(END, cut[0:-1])


root = Tk()
text = Text(root)
text.insert(INSERT, "Hello..... 1234 bye")
text.pack(expand=1, fill=BOTH)


Button(text="Delete Word", command=delete_word).pack()

root.mainloop()



# # task 9
#
# from tkinter import *
#
# buffer = ""
#
#
# def make_upper():
#     global buffer
#     buffer = text.get(1.0, END)
#     text.delete(1.0, END)
#     upper = buffer.upper()
#     text.insert(END, upper)
#
#
# def make_lower():
#     global buffer
#     buffer = text.get(1.0, END)
#     text.delete(1.0, END)
#     lower = buffer.lower()
#     text.insert(END, lower)
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....1234")
# text.pack(expand=1, fill=BOTH)
#
#
# Button(text="Upper", command=make_upper).pack()
#
# Button(text="Lower", command=make_lower).pack()
#
# root.mainloop()

