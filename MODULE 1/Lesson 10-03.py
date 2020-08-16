from tkinter import *

root = Tk()

frame_title = LabelFrame(text="title")
frame_title.pack()

frame_top = LabelFrame(text="top")
frame_top.pack(side=LEFT)

frame_bottom = LabelFrame(text="bottom")
frame_bottom.pack(side=LEFT)

frame_basement = LabelFrame(text="basement")
frame_basement.pack(side=BOTTOM)

label_1 = Label(frame_top, width=7, height=4, bg='yellow', text="1")
label_1.pack(side=LEFT)

label_2 = Label(frame_bottom, width=7, height=4, bg='red', text="2").pack(side=LEFT)
label_3 = Label(frame_basement, width=7, height=4, bg='blue', text="3").pack(side=LEFT)
label_4 = Label(frame_title, width=7, height=4, bg='yellow', text="File").pack(side=LEFT)
label_5 = Label(frame_title, width=7, height=4, bg='yellow', text="View").pack(side=LEFT)
label_6 = Label(frame_title, width=7, height=4, bg='yellow', text="About").pack(side=LEFT)


root.mainloop()

