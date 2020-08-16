from tkinter import *

# yellow buttons

def click_A8():

    # print(", A8")

    # how to check what is inside the field:

    # print(text.get(1.0, END))
    # print(list(text.get(1.0, END)))
    # print(text.get(1.0, END) == "")
    # print(bool(text.get(1.0, END)))
    # print(len(text.get(1.0, END)))
    # print(len(text.get(1.0, END))>1)

    if len(text.get(1.0, END))>1:
        text.insert(END, ", A8")
    else:
        text.insert(END, "A8")


def click_C8():
    print("C8")
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", C8")
    else:
        text.insert(END, "C8")


def click_B7():
    print("B7")

    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", B7")
    else:
        text.insert(END, "B7")


def click_D7():
    print("D7")

    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", D7")
    else:
        text.insert(END, "D7")


def click_A6():
    print("A6")

    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", A6")
    else:
        text.insert(END, "A6")


def click_C6():
    print("C6")

    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", C6")
    else:
        text.insert(END, "C6")


def click_B5():
    print("B5")
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", B5")
    else:
        text.insert(END, "B5")


def click_D5():
    print("D5")
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", D5")
    else:
        text.insert(END, "D5")

# red buttons

def click_B8():
    print("B8")
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", B8")
    else:
        text.insert(END, "B8")

def click_D8():
    print("D8")
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", D8")
    else:
        text.insert(END, "D8")

def click_A7():
    print("A7")

    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", A7")
    else:
        text.insert(END, "A7")

def click_C7():
    print("C7")
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", C7")
    else:
        text.insert(END, "C7")

def click_B6():
    print("B6")
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", B6")
    else:
        text.insert(END, "B6")


def click_D6():
    print("D6")
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", D6")
    else:
        text.insert(END, "D6")


def click_A5():
    print("A5")
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", A5")
    else:
        text.insert(END, "A5")


def click_C5():
    print("C5")
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", C5")
    else:
        text.insert(END, "C5")




root = Tk()


Label(text="A").grid(column=2, row=0)
Label(text="B").grid(column=3, row=0)
Label(text="C").grid(column=4, row=0)
Label(text="D").grid(column=5, row=0)
Label(text="8").grid(column=1, row=1)
Label(text="7").grid(column=1, row=2)
Label(text="6").grid(column=1, row=3)
Label(text="5").grid(column=1, row=4)

Button(fg="yellow", text="yellow", width="10", height="5", command=click_A8).grid(column=2, row=1)
Button(fg="yellow", text="yellow", width="10", height="5", command=click_C8).grid(column=4, row=1)
Button(fg="yellow", text="yellow", width="10", height="5", command=click_B7).grid(column=3, row=2)
Button(fg="yellow", text="yellow", width="10", height="5", command=click_D7).grid(column=5, row=2)
Button(fg="yellow", text="yellow", width="10", height="5", command=click_A6).grid(column=2, row=3)
Button(fg="yellow", text="yellow", width="10", height="5", command=click_C6).grid(column=4, row=3)
Button(fg="yellow", text="yellow", width="10", height="5", command=click_B5).grid(column=3, row=4)
Button(fg="yellow", text="yellow", width="10", height="5", command=click_D5).grid(column=5, row=4)

Button(fg="red", text="red", width="10", height="5", command=click_B8).grid(column=3, row=1)
Button(fg="red", text="red", width="10", height="5", command=click_D8).grid(column=5, row=1)
Button(fg="red", text="red", width="10", height="5", command=click_A7).grid(column=2, row=2)
Button(fg="red", text="red", width="10", height="5", command=click_C7).grid(column=4, row=2)
Button(fg="red", text="red", width="10", height="5", command=click_B6).grid(column=3, row=3)
Button(fg="red", text="red", width="10", height="5", command=click_D6).grid(column=5, row=3)
Button(fg="red", text="red", width="10", height="5", command=click_A5).grid(column=2, row=4)
Button(fg="red", text="red", width="10", height="5", command=click_C5).grid(column=4, row=4)

text=Text()
text.grid(column=6, row=1, rowspan=8, sticky=NSEW)

root.mainloop()

