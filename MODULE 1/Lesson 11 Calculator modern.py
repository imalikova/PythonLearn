from tkinter import *
# from tkinter.ttk import *


def click_7():
    screen.insert(END, "7")


def click_8():
    screen.insert(END, "8")


def click_9():
    screen.insert(END, "9")


def click_0():
    screen.insert(END, "0")


def click_1():
    screen.insert(END, "1")


def click_2():
    screen.insert(END, "2")


def click_3():
    screen.insert(END, "3")


def click_4():
    screen.insert(END, "4")


def click_5():
    screen.insert(END, "5")


def click_6():
    screen.insert(END, "6")


root = Tk()
root.title("Calculator")
root.resizable(False, False)

# screen

screen = Entry(justify=RIGHT)
screen.grid(row=1, column=1, columnspan=6, sticky=NSEW)
screen.insert(END, "0")


# row 1 buttons

Button(text="MC", width=4, height=2).grid(row=10, column=1)
Button(text="MR", width=4, height=2).grid(row=10, column=2)
Button(text="MS", width=4, height=2).grid(row=10, column=3)
Button(text="M+", width=4, height=2).grid(row=10, column=4)
Button(text="M-", width=4, height=2).grid(row=10, column=5)

# row 2 buttons

Button(text="←", width=4, height=2).grid(row=20, column=1)
Button(text="CE", width=4, height=2).grid(row=20, column=2)
Button(text="C", width=4, height=2).grid(row=20, column=3)
Button(text=chr(177), width=4, height=2).grid(row=20, column=4)
Button(text=chr(8730), width=4, height=2).grid(row=20, column=5)


# row 3 buttons

Button(text="7", width=4, height=2, command=click_7).grid(row=30, column=1)
Button(text="8", width=4, height=2, command=click_8).grid(row=30, column=2)
Button(text="9", width=4, height=2, command=click_9).grid(row=30, column=3)
Button(text="/", width=4, height=2).grid(row=30, column=4)
Button(text="%", width=4, height=2).grid(row=30, column=5)


# row 4 buttons

Button(text="4", width=4, height=2, command=click_4).grid(row=40, column=1)
Button(text="5", width=4, height=2, command=click_5).grid(row=40, column=2)
Button(text="6", width=4, height=2, command=click_6).grid(row=40, column=3)
Button(text="*", width=4, height=2).grid(row=40, column=4)
Button(text="1/x", width=4, height=2).grid(row=40, column=5)


# row 5 buttons

Button(text="1", width=4, height=2, command=click_1).grid(row=50, column=1)
Button(text="2", width=4, height=2, command=click_2).grid(row=50, column=2)
Button(text="3", width=4, height=2, command=click_3).grid(row=50, column=3)
Button(text="-", width=4, height=2).grid(row=50, column=4)
Button(text="=", width=4, height=4).grid(row=50, column=5, rowspan=15, sticky=NSEW)

# row 6 buttons

Button(text="0", width=8, height=2).grid(row=60, column=1, columnspan=2, sticky=NSEW)
Button(text=".", width=4, height=2).grid(row=60, column=3)
Button(text="+", width=4, height=2).grid(row=60, column=4)



root.mainloop()