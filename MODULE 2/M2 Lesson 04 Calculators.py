# # calculator pack
#
# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
# root.title("Calculator")
# root.resizable(False, False)
#
# buttons_row1 = [1, 2, 3, 4, 5]
# buttons_row2 = [6, 7, 8, 9, 0]
# buttons_row3 = ["+", "-", "*", "/", "="]
#
# # screen
#
# frame_screen = Frame()
# frame_screen.pack(fill=X)
#
# num = StringVar()
# num.set(0)
# Entry(frame_screen, text=num, justify=RIGHT).pack(fill=X)
#
#
# # frame row 1 buttons digits
#
# frame_row1 = Frame()
# frame_row1.pack(fill=X)
#
# for button in buttons_row1:
#     Button(frame_row1, text=button, width=3).pack(side=LEFT)
#
# # frame row 2 buttons digits
#
# frame_row2 = Frame()
# frame_row2.pack(fill=X)
#
# for button in buttons_row2:
#     Button(frame_row2, text=button, width=3).pack(side=LEFT)
#
# # frame row 3 buttons operations
#
# frame_row3 = Frame()
# frame_row3.pack(fill=X)
#
# for button in buttons_row3:
#     Button(frame_row3, text=button, width=3).pack(side=LEFT)
#
# root.mainloop()
#
#
# # calculator grid
#
# from tkinter import *
#
# root = Tk()
# root.title("Calculator")
# root.resizable(False, False)
#
# buttons_row1 = [1, 2, 3, 4, 5]
# buttons_row2 = [6, 7, 8, 9, 0]
# buttons_row3 = ["+", "-", "*", "/", "="]
#
# columns = [1, 2, 3, 4, 5]
#
#
# # screen
#
# num = StringVar()
# num.set(0)
# Entry(text=num, justify=RIGHT).grid(row=1, column=1, columnspan=5)
#
#
# # row 1 buttons digits
#
# for button, column in zip(buttons_row1, columns):
#     Button(text=button, width=3).grid(row=2, column=column)
#
# # row 2 buttons digits
#
# for button, column in zip(buttons_row2, columns):
#     Button(text=button, width=3).grid(row=3, column=column)
#
# # row 3 buttons operations
#
# for button, column in zip(buttons_row3, columns):
#     Button(text=button, width=3).grid(row=4, column=column)
#
# root.mainloop()


# # calculator place
#
# from tkinter import *
# # from tkinter.ttk import *
#
# root = Tk()
# root.title("Calculator")
# root.resizable(False, False) # lesson 3 size of window
#
# buttons_row1 = [1, 2, 3, 4, 5]
# buttons_row2 = [6, 7, 8, 9, 0]
# buttons_row3 = ["+", "-", "*", "/", "="]
# x = [5, 42, 79, 116, 153]
#
# # screen
#
# num = StringVar()
# num.set(0)
# Entry(text=num, justify=RIGHT, width=19).place(x=8, y=5)
#
# #row 1 buttons digits
#
# for button, button_width in zip(buttons_row1, x):
#     Button(text=button, width=4).place(x=button_width, y=50)
#
#
# # frame row 2 buttons digits
#
# for button, button_width in zip(buttons_row2, x):
#     Button(text=button, width=4).place(x=button_width, y=85)
#
# # frame row 3 buttons operations
#
# for button, button_width in zip(buttons_row3, x):
#     Button(text=button, width=4).place(x=button_width, y=120)
#
#
# root.mainloop()


# # calculator modern
#
# from tkinter import *
#
# root = Tk()
# root.title("Calculator")
# root.resizable(False, False)
#
# buttons_M = ["MC", "MR", "MS", "M+", "M-"]
# buttons_special = ["←", "CE", "C", chr(177), chr(8730)]
# buttons_row3 = [7, 8, 9, "/", "%"]
# buttons_row4 = [4, 5, 6, "*", "1/x"]
# buttons_row5 = [1, 2, 3, "-"]
# buttons_row6 = [".", "+"]
#
# columns = [1, 2, 3, 4, 5]
#
# # screen
#
# screen = Entry(justify=RIGHT)
# screen.grid(row=1, column=1, columnspan=6, sticky=NSEW)
# screen.insert(END, "0")
#
#
# # row 1 buttons
#
# for button, column in zip(buttons_M, columns):
#     Button(text=button, width=4, height=2).grid(row=10, column=column)
#
# # row 2 buttons
#
# for button, column in zip(buttons_special, columns):
#     Button(text=button, width=4, height=2).grid(row=20, column=column)
#
#
# # row 3 buttons
#
# for button, column in zip(buttons_row3, columns):
#     Button(text=button, width=4, height=2).grid(row=30, column=column)
#
#
# # row 4 buttons
#
# for button, column in zip(buttons_row4, columns):
#     Button(text=button, width=4, height=2).grid(row=40, column=column)
#
#
# # row 5 buttons
#
# for button, column in zip(buttons_row5, columns):
#     Button(text=button, width=4, height=2).grid(row=50, column=column)
#
# Button(text="=", width=4, height=4).grid(row=50, column=5, rowspan=15, sticky=NSEW)
#
# # row 6 buttons
#
# Button(text="0", width=8, height=2).grid(row=60, column=1, columnspan=2, sticky=NSEW)
#
# for button, column in zip(buttons_row6, columns[2:4]):
#     Button(text=button, width=4, height=2).grid(row=60, column=column)
#
# root.mainloop()

# calculator modern

# from tkinter import *
#
# buttons_text_M = ["MC", "MR", "MS", "M+", "M-"]
# buttons_text_special = ["←", "CE", "C", chr(177), chr(8730)]
# buttons_text_row3 = [7, 8, 9, "/", "%"]
# buttons_text_row4 = [4, 5, 6, "*", "1/x"]
# buttons_text_row5 = [1, 2, 3, "-"]
# buttons_text_row6 = [".", "+"]
#
# root = Tk()
# root.title("Calculator")
# root.resizable(False, False)
#
# screen = Entry(justify=RIGHT) # screen
# screen.grid(row=0, column=1, columnspan=6, sticky=NSEW)
# screen.insert(END, "0")
#
# for index, button in enumerate(buttons_text_M): # row 1 buttons
#     Button(text=button, width=4, height=2).grid(row=1, column=index+1)
#
# for index, button in enumerate(buttons_text_special):   # row 2 buttons
#     Button(text=button, width=4, height=2).grid(row=2, column=index+1)
#
# for index, button in enumerate(buttons_text_row3):  # row 3 buttons
#     Button(text=button, width=4, height=2).grid(row=3, column=index+1)
#
# for index, button in enumerate(buttons_text_row4):  # row 4 buttons
#     Button(text=button, width=4, height=2).grid(row=4, column=index+1)
#
# for index, button in enumerate(buttons_text_row5):  # row 5 buttons
#     Button(text=button, width=4, height=2).grid(row=5, column=index+1)
#
# Button(text="=", width=4, height=4).grid(row=5, column=5, rowspan=15, sticky=NSEW)
#
# for index, button in enumerate(buttons_text_row6):  # row 6 buttons
#     Button(text=button, width=4, height=2).grid(row=6, column=index+3)
#
# Button(text="0", width=8, height=2).grid(row=6, column=1, columnspan=2, sticky=NSEW)
#
# root.mainloop()


# from tkinter import *
#
# # buttons_text_M = ["MC", "MR", "MS", "M+", "M-"]
# # buttons_text_special = ["←", "CE", "C", chr(177), chr(8730)]
# # buttons_text_row3 = [7, 8, 9, "/", "%"]
# # buttons_text_row4 = [4, 5, 6, "*", "1/x"]
# # buttons_text_row5 = [1, 2, 3, "-"]
# # buttons_text_row6 = [".", "+"]
#
# text_buttons = [
#     ["MC", "MR", "MS", "M+", "M-"],
#     ["←", "CE", "C", chr(177), chr(8730)],
#     [7, 8, 9, "/", "%"],
#     [4, 5, 6, "*", "1/x"],
#     [1, 2, 3, "-", "="],
#     [0, ".", "+"]
# ]
#
# root = Tk()
# root.title("Calculator")
# root.resizable(False, False)
#
# screen = Entry(justify=RIGHT)   # screen
# screen.grid(row=0, column=1, columnspan=6, sticky=NSEW)
# screen.insert(END, "0")
#
# for index, button in enumerate(text_buttons[0]): # row 1 buttons
#     Button(text=button, width=4, height=2).grid(row=1, column=index+1)
#
# for index, button in enumerate(text_buttons[1]):   # row 2 buttons
#     Button(text=button, width=4, height=2).grid(row=2, column=index+1)
#
# for index, button in enumerate(text_buttons[2]):  # row 3 buttons
#     Button(text=button, width=4, height=2).grid(row=3, column=index+1)
#
# for index, button in enumerate(text_buttons[3]):  # row 4 buttons
#     Button(text=button, width=4, height=2).grid(row=4, column=index+1)
#
# for index, button in enumerate(text_buttons[4]):  # row 5 buttons
#     if button == "=":
#         Button(text="=", width=4, height=4).grid(row=5, column=index+1, rowspan=2, sticky=NSEW)
#     else:
#         Button(text=button, width=4, height=2).grid(row=5, column=index+1)
#
# for index, button in enumerate(text_buttons[5]):  # row 6 buttons
#     if button == 0:
#         Button(text="0", width=8, height=2).grid(row=6, column=index+1, columnspan=2, sticky=NSEW)
#     else:
#         Button(text=button, width=4, height=2).grid(row=6, column=index+2)


# root.mainloop()


from tkinter import *

text_buttons = [
    ["MC", "MR", "MS", "M+", "M-"],
    ["←", "CE", "C", chr(177), chr(8730)],
    [7, 8, 9, "/", "%"],
    [4, 5, 6, "*", "1/x"],
    [1, 2, 3, "-", "="],
    [0, "", ".", "+"]
]

root = Tk()
root.title("Calculator")
root.resizable(False, False)

screen = Entry(justify=RIGHT)   # screen
screen.grid(row=0, column=1, columnspan=6, sticky=NSEW)
screen.insert(END, "0")

for i in range(6):
    for index, button in enumerate(text_buttons[i]):
        if button == "=":
            Button(text="=", width=4, height=4).grid(row=5, column=index+1, rowspan=2, sticky=NSEW)
        elif button == 0:
            Button(text="0", width=8, height=2).grid(row=6, column=index+1, columnspan=2, sticky=NSEW)
        elif button:  # if button exists
            Button(text=button, width=4, height=2).grid(row=i+1, column=index+1)

root.mainloop()

