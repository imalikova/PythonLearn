# from tkinter import *
#
#
# root = Tk()
#
# letters_list = ["", "A", "B", "C", "D", "E", "F", "G", "H", ""]
#
# # letters list
#
# for row in range(10):
#
#     for column, letter in enumerate(letters_list):
#
#         # axis
#
#         if row == 0 and column%2 == 1: # odd
#             Label(text=letter, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#         elif row == 0 and column%2 == 0:  # even, remainder form division (% - division)
#             Label(text=letter, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#         elif row == 9 and column % 2 == 1:  # odd
#             Label(text=letter, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#         elif row == 9 and column % 2 == 0:  # even, remainder form division (% - division)
#             Label(text=letter, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#
#         if column == 0 and row%2 == 1:
#             Label(text=9-row, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#         elif column == 0 and row%2 == 0:
#             Label(text=9-row, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#         elif column == 9 and row%2 == 1:
#             Label(text=9-row, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#         elif column == 9 and row%2 == 0:
#             Label(text=9-row, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#
#
#         # chess field
#
#         elif row != 9 and row != 0:
#             if row%2 == 0:  # even
#                 if column%2 == 0:
#                     Label(bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#                 elif column%2 == 1:
#                     Label(bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#             if row % 2 == 1:  # odd
#                 if column%2 == 1:
#                     Label(bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#                 elif column%2 == 0:
#                     Label(bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#
# text=Text()
# text.grid(column=10, row=1, rowspan=8, sticky=NSEW)
#
# root.mainloop()


# from tkinter import *
#
#
# root = Tk()
#
# letters_list = ["", "A", "B", "C", "D", "E", "F", "G", "H", ""]
#
# # letters list
#
# for row in range(10):
#
#     for column, letter in enumerate(letters_list):
#
#         # axis
#
#         if (row == 0 and column%2 == 1) or (row == 9 and column % 2 == 0): # even
#             Label(text=letter, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#         elif (row == 0 and column%2 == 0) or (row == 9 and column % 2 == 1):  # odd, remainder form division (% - division)
#             Label(text=letter, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#
#         if (column == 0 and row%2 == 1 or column == 9 and row%2 == 0) and (row != 0 and row != 9):
#             Label(text=9-row, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#         elif (column == 0 and row%2 == 0 or column == 9 and row%2 == 1) and (row != 0 and row != 9):
#             Label(text=9-row, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#
#
#         # chess field
#
#         elif row != 9 and row != 0:
#             if (row + column) % 2 == 0:
#                 Label(bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#             else:
#                 Label(bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#
#
# text=Text()
# text.grid(column=10, row=1, rowspan=8, sticky=NSEW)
#
# root.mainloop()


# from tkinter import *
#
#
# root = Tk()
#
# letters_list = ["", "A", "B", "C", "D", "E", "F", "G", "H", ""]
#
# # letters list
#
# for row in range(10):
#
#     for column, letter in enumerate(letters_list):
#
#         # # axis
#         #
#         # if (row == 0 and column%2 == 1) or (row == 9 and column % 2 == 0): # even
#         #     Label(text=letter, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#         # elif (row == 0 and column%2 == 0) or (row == 9 and column % 2 == 1):  # odd, remainder form division (% - division)
#         #     Label(text=letter, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#         #
#         # if (column == 0 and row%2 == 1 or column == 9 and row%2 == 0) and (row != 0 and row != 9):
#         #     Label(text=9-row, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#         # elif (column == 0 and row%2 == 0 or column == 9 and row%2 == 1) and (row != 0 and row != 9):
#         #     Label(text=9-row, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#         #
#         #
#         # # chess field
#         #
#         # elif row != 9 and row != 0:
#         #     if (row + column) % 2 == 0:
#         #         Label(bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#         #     else:
#         #         Label(bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#
#         if (row + column) % 2 == 0:
#             if row == 0 or row == 9:
#                 Label(text=letter, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#             elif column == 0 or column == 9:
#                 Label(text=9 - row, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#             else:
#                 Label(bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#
#         else:
#             if row == 0 or row == 9:
#                 Label(text=letter, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#             elif column == 0 or column == 9:
#                 Label(text=9 - row, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#             else:
#                 Label(bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#
#
#
# text=Text()
# text.grid(column=10, row=1, rowspan=8, sticky=NSEW)
#
# root.mainloop()


# from tkinter import *
#
# def paint_cell(color, row, column):
#
#     if row == 0 or row == 9:
#         Label(text=letter, bg=color, width=5).grid(row=row, column=column, sticky=NSEW)
#     elif column == 0 or column == 9:
#         Label(text=9 - row, bg=color, width=5).grid(row=row, column=column, sticky=NSEW)
#     else:
#         Label(bg=color, width=5).grid(row=row, column=column, sticky=NSEW)
#
#
# root = Tk()
#
# letters_list = ["", "A", "B", "C", "D", "E", "F", "G", "H", ""]
#
# # letters list
#
# for row in range(10):
#     for column, letter in enumerate(letters_list):
#         if (row + column) % 2 == 0:
#             # if row == 0 or row == 9:
#             #     Label(text=letter, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#             # elif column == 0 or column == 9:
#             #     Label(text=9 - row, bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#             # else:
#             #     Label(bg="white", width=5).grid(row=row, column=column, sticky=NSEW)
#
#             paint_cell("white", row, column)
#
#         else:
#             # if row == 0 or row == 9:
#             #     Label(text=letter, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#             # elif column == 0 or column == 9:
#             #     Label(text=9 - row, bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#             # else:
#             #     Label(bg="grey", width=5).grid(row=row, column=column, sticky=NSEW)
#             paint_cell("grey", row, column)
#
#
# text=Text()
# text.grid(column=10, row=1, rowspan=8, sticky=NSEW)
#
# root.mainloop()


from tkinter import *


def paint_cell(color, row, column):
    if row == 0 or row == 9:
        Label(text=letter, bg=color, width=5).grid(row=row, column=column, sticky=NSEW)
    elif column == 0 or column == 9:
        Label(text=9 - row, bg=color, width=5).grid(row=row, column=column, sticky=NSEW)
    else:
        Label(bg=color, width=5).grid(row=row, column=column, sticky=NSEW)


root = Tk()

for row in range(10):
    for column, letter in enumerate(["", "A", "B", "C", "D", "E", "F", "G", "H", ""]):
        if (row + column) % 2 == 0:
            paint_cell("white", row, column)
        else:
            paint_cell("grey", row, column)

text = Text()
text.grid(column=10, row=1, rowspan=8, sticky=NSEW)

root.mainloop()
