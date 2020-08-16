# from tkinter import *
#
#
# def paint_cell(color, row, column, letter):
#     if row == 0 or row == 9:
#         Button(text=letter, fg=color, width=5, command=lambda mark=f"{letter}{9 - row}": click_cell(mark)).grid(row=row, column=column, sticky=NSEW)
#     elif column == 0 or column == 9:
#         Button(text=9 - row, fg=color, width=5, command=lambda mark=f"{letter}{9 - row}": click_cell(mark)).grid(row=row, column=column, sticky=NSEW)
#     else:
#         Button(fg=color, width=5, command=lambda mark=f"{letter}{9 - row}": click_cell(mark)).grid(row=row, column=column, sticky=NSEW)
#
#
# def click_cell(mark):
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, f", {mark}")
#     else:
#         text.insert(END, f"{mark}")
#
#
# root = Tk()
#
# text = Text()
# text.grid(column=10, row=1, rowspan=8, sticky=NSEW)
#
# for row in range(10):
#     for column, letter in enumerate(["", "A", "B", "C", "D", "E", "F", "G", "H", ""]):
#         if (row + column) % 2:
#             paint_cell("green", row, column, letter)
#         else:
#             paint_cell("grey", row, column, letter)
#
#
# root.mainloop()


from tkinter import *


def paint_cell(color, row, column, letter):

    chess_button = Button(fg=color, width=5, command=lambda mark=f"{letter}{9 - row}": click_cell(mark))
    chess_button.grid(row=row, column=column, sticky=NSEW)

    if row == 0 or row == 9:
        chess_button.config(text=letter)
    elif column == 0 or column == 9:
        chess_button.config(text=9 - row)


def click_cell(mark):
    if len(text.get(1.0, END)) > 1:
        text.insert(END, f", {mark}")
    else:
        text.insert(END, f"{mark}")


root = Tk()

text = Text()
text.grid(column=10, row=1, rowspan=8, sticky=NSEW)

for row in range(10):
    for column, letter in enumerate(["", "A", "B", "C", "D", "E", "F", "G", "H", ""]):
        if (row + column) % 2:
            paint_cell("green", row, column, letter)
        else:
            paint_cell("grey", row, column, letter)


root.mainloop()

