from tkinter import *

def translate_fields():
    name.config(text="Имя:")
    surname.config(text="Фамилия:")
    year.config(text="Год рождения:")


root = Tk()

root.geometry("300x250")

name = Label(text="Name:")
name.place(x=1, y=1)

name_field = Entry()
name_field.place(x=80, y=1)

surname = Label(text="Surname:")
surname.place(x=1, y=50)

surname_field = Entry()
surname_field.place(x=80, y=50)

year = Label(text="Year:")
year.place(x=1, y=100)

year_field = Entry()
year_field.place(x=80, y=100)

button_translate = Button(text="Russian", command=translate_fields)
button_translate.place(relx=.5, y=150)

root.mainloop()