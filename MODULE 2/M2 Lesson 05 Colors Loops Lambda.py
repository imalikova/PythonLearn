from tkinter import *

color_codes = ["#ff0000", "#ff7d00", "#ffff00", "#00ff00", "#007dff", "#0000ff", "#7d00ff"]

color_names = ["Red", "Orange", "Yellow", "Green", "Light blue", "Blue", "Purple"]


def show_color(color,index):
    message.set(color_codes[index])
    label_1.config(text=color, fg=color)


root = Tk()

label_1 = Label(text="Color name")
label_1.pack()

message = StringVar()
message.set("Color code")
entry_one = Entry(root, textvariable=message, justify=CENTER).pack()


for index, color in enumerate(color_names):
    button = Button(text=color)
    button.config(command=lambda par_1=color, par_2=index: show_color(par_1, par_2))
    button.pack(fill=X)

root.mainloop()

