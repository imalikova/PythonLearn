# from tkinter import *
#
# root = Tk()
# # frame_name = LabelFrame(text="Name")
# # frame_name.pack()
#
# frame_name = Frame()
# frame_name.pack(fill=X)
#
# Label(frame_name, bg='yellow', text="Name").pack(side=LEFT)
# Entry(frame_name).pack(side=RIGHT)
#
# frame_surname = LabelFrame(text="Surname")
# frame_surname.pack(fill=X)
#
# Label(frame_surname, bg='blue', text="Surname").pack(side=LEFT)
# Entry(frame_surname).pack(side=RIGHT)
#
# frame_year = LabelFrame(text="Year")
# frame_year.pack(fill=X)
#
# Label(frame_year, bg='red', text="Year").pack(side=LEFT)
# Entry(frame_year).pack(side=RIGHT)
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
# Label(bg='yellow', text='name').grid(column=0, row=0)
#
# Entry().grid(column=1, row=0)
#
# Label(bg='pink', text='surname').grid(column=0, row=1)
#
# Entry().grid(column=1, row=1)
#
# Label(bg="violet", text="year").grid(column=0, row=2)
#
# Entry().grid(column=1, row=2)
#
#
# root.mainloop()


from tkinter import *

root = Tk()

frame_name = Frame()
frame_name.grid(column=0, row=0, columnspan=2)

Label(frame_name, bg='yellow', text='name').pack(side=LEFT)

Entry(frame_name).pack(side=LEFT)

Label(bg='pink', text='surname').grid(column=0, row=1)

Entry().grid(column=1, row=1)

Label(bg="violet", text="year").grid(column=0, row=2)

Entry().grid(column=1, row=2)


root.mainloop()