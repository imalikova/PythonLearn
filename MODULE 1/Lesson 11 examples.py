import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()

ttk.Button(text='ttk').pack()

tk.Button(text='tk', fg="red").pack()

ttk.Label(text="ttk").pack()

tk.Label(text="tk").pack()

tk.Scale().pack()

ttk.Scale().pack()

ttk.LabeledScale().pack()

tk.Spinbox().pack()

ttk.Spinbox().pack()

ttk.Menubutton().pack()

root.mainloop()


