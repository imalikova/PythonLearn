from tkinter import *


root = Tk()
# root.title("GUI на Python")
# root.geometry("300x250")

button_1 = Button(text="button_1", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
button_1.place(x=1, y=1)

button_2 = Button(text="button_2", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
button_2.place(x=1, y=215)

button_3 = Button(text="button_3", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
button_3.place(x=210, y=1)

button_4 = Button(text="button_4", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
button_4.place(x=210, y=215)

button_5 = Button(text="button_5", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
button_5.place(relx=.5, rely=.5)

root.mainloop()