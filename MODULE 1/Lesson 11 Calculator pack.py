from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Calculator")
root.resizable(False, False)

# screen

frame_screen = Frame()
frame_screen.pack(fill=X)

num = StringVar()
num.set(0)
Entry(frame_screen, text=num, justify=RIGHT).pack(fill=X)


# frame row 1 buttons digits

frame_row1 = Frame()
frame_row1.pack(fill=X)

Button(frame_row1, text=1, width=3).pack(side=LEFT)
Button(frame_row1, text=2, width=3).pack(side=LEFT)
Button(frame_row1, text=3, width=3).pack(side=LEFT)
Button(frame_row1, text=4, width=3).pack(side=LEFT)
Button(frame_row1, text=5, width=3).pack(side=LEFT)

# frame row 2 buttons digits

frame_row2 = Frame()
frame_row2.pack(fill=X)

Button(frame_row2, text=6, width=3).pack(side=LEFT)
Button(frame_row2, text=7, width=3).pack(side=LEFT)
Button(frame_row2, text=8, width=3).pack(side=LEFT)
Button(frame_row2, text=9, width=3).pack(side=LEFT)
Button(frame_row2, text=0, width=3).pack(side=LEFT)

# frame row 3 buttons operations

frame_row3 = Frame()
frame_row3.pack(fill=X)

Button(frame_row3, text="+", width=3).pack(side=LEFT)
Button(frame_row3, text="-", width=3).pack(side=LEFT)
Button(frame_row3, text="*", width=3).pack(side=LEFT)
Button(frame_row3, text="/", width=3).pack(side=LEFT)
Button(frame_row3, text="=", width=3).pack(side=LEFT)

root.mainloop()