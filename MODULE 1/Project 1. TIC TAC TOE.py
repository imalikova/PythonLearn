from tkinter import *
from tkinter.ttk import *

switch = True


def click_11():
    global switch

    # print(button_11["text"])

    if not button_11["text"]:

        if switch:
            button_11.config(text="X")
            # switch = False
        else:
            button_11.config(text="0")
            # switch = True

        switch = not switch


def click_12():
    global switch

    if not button_12["text"]:

        if switch:
            button_12.config(text="X")
            switch = False
        else:
            button_12.config(text="0")
            switch = True


def click_21():
    global switch

    if not button_21["text"]:

        if switch:
            button_21.config(text="X")
            switch = False
        else:
            button_21.config(text="0")
            switch = True


def click_22():
    global switch

    if not button_22["text"]:

        if switch:
            button_22.config(text="X")
            switch = False
        else:
            button_22.config(text="0")
            switch = True


root=Tk()
root.title("Tic tac toe v.04")


button_11 = Button(command=click_11)
button_11.grid(row=1, column=1, ipadx=100, ipady=100, sticky=NSEW)

button_12 = Button(command=click_12)
button_12.grid(row=1, column=2, ipadx=100, ipady=100, sticky=NSEW)

button_21 = Button(command=click_21)
button_21.grid(row=2, column=1, ipadx=100, ipady=100, sticky=NSEW)

button_22 = Button(command=click_22)
button_22.grid(row=2, column=2, ipadx=100, ipady=100, sticky=NSEW)

root.mainloop()