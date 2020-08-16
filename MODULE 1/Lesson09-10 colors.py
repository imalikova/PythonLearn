from tkinter import *

def show_red():
    message.set("#ff0000")
    label_1.config(text="Red", fg="#ff0000")


def show_orange():
    message.set("#ff7d00")
    label_1.config(text="Orange")


def show_yellow():
    message.set("#ffff00")
    label_1.config(text="Yellow")


def show_green():
    message.set("#00ff00")
    label_1.config(text="Green")


def show_light_blue():
    message.set("#007dff")
    label_1.config(text="Light blue")


def show_blue():
    message.set("#0000ff")
    label_1.config(text="Blue")


def show_purple():
    message.set("#7d00ff")
    label_1.config(text="Purple")


root = Tk()

label_1 = Label(text="Color name")
label_1.pack()

message = StringVar()
message.set("Color code")
entry_one = Entry(root, textvariable=message, justify=CENTER).pack()

red_button = Button(text="1", fg="#ff0000", command=show_red)
red_button.pack(fill=X)

orange_button = Button(text="1", fg="#ff7d00", command=show_orange)
orange_button.pack(fill=X)

yellow_button = Button(text="1", fg="#ffff00", command=show_yellow)
yellow_button.pack(fill=X)

green_button = Button(text="1", fg="#00ff00", command=show_green)
green_button.pack(fill=X)

light_blue_button = Button(text="1", fg="#007dff", command=show_light_blue)
light_blue_button.pack(fill=X)

blue_button = Button(text="1", fg="#0000ff", command=show_blue)
blue_button.pack(fill=X)

purple_button = Button(text="1", fg="#7d00ff", command=show_purple)
purple_button.pack(fill=X)

root.mainloop()