from tkinter import *

root = Tk()
lbl = Label(root, text="This text wrote in the first label!")
lbl.pack()
root.title('Top-left')
root.geometry("400x300+0+0")
# root.mainloop()

root1 = Tk()
lbl = Label(root1, text="This text wrote in the first label!")
lbl.pack()
root1.title('Top-right')
root1.geometry("400x300+1400+0")
root1.mainloop()

