# Используя LabelFram() и расположите виждеты внутри используя метод pack(side=LEFT) напишите программу "Примеры" состоящую из:
#
# одно-строчного текстового поля,
# метки с отображением знака "+",
# второго одно-строчного текстового поля,
# кнопкой "=", при нажатии на которую результат вычисления выводиться в третье текстовое поле,
# третьего одно-строчного тестового поля.
# реализуйте растяжение виджетов по ширине в зависимости от ширины окна.

from tkinter import *


def sum_numbers():
    sum_result.delete(0,END)

    #check that fields are not letters and not empty


    if sum_field_1.get() and sum_field_1.get().isnumeric() and (
                sum_field_1.get()[0] == '-' or not sum_field_1.get().isalpha()) and sum_field_2.get() and (
                sum_field_2.get().isnumeric() and (sum_field_2.get()[0] == '-' or not sum_field_2.get().isalpha())):

        sum_result.insert(END, int(sum_field_1.get())+int(sum_field_2.get()))

    else:
        sum_result.insert(END, "unexpected input")


def subtract_numbers():

    subtract_result.delete(0, END)

    print(bool(subtract_field_1.get() and subtract_field_2.get()))

    if subtract_field_1.get() and subtract_field_1.get().isnumeric() and (
            subtract_field_1.get()[0] == '-' or not subtract_field_1.get().isalpha()) and subtract_field_2.get() and (
            subtract_field_2.get().isnumeric() and (subtract_field_2.get()[0] == '-' or not subtract_field_2.get().isalpha())):

        subtract_result.insert(END, int(subtract_field_1.get()) - int(subtract_field_2.get()))

    else:
        subtract_result.insert(END, "unexpected input")


def multiply_numbers():

    multiply_result.delete(0, END)

    print(bool(multiply_field_1.get() and multiply_field_2.get()))

    if multiply_field_1.get() and multiply_field_1.get().isnumeric() and (
            multiply_field_1.get()[0] == '-' or not multiply_field_1.get().isalpha()) and multiply_field_2.get() and (
            multiply_field_2.get().isnumeric() and (
            multiply_field_2.get()[0] == '-' or not multiply_field_2.get().isalpha())):

        multiply_result.insert(END, int(multiply_field_1.get()) * int(multiply_field_2.get()))

    else:
        subtract_result.insert(END, "unexpected input")


def divide_numbers():

    divide_result.delete(0, END)

    print(bool(divide_field_1.get() and divide_field_2.get()))

    if divide_field_2.get() == "0":

        divide_result.insert(END, "division by zero!")

    elif divide_field_1.get() and divide_field_1.get().isnumeric() and (

            divide_field_1.get()[0] == '-' or not divide_field_1.get().isalpha()) and divide_field_2.get() and (

            divide_field_2.get().isnumeric() and (

            divide_field_2.get()[0] == '-' or not divide_field_2.get().isalpha())):

            divide_result.insert(END, int(divide_field_1.get()) / int(divide_field_2.get()))


    else:
        divide_result.insert(END, "unexpected input")


root = Tk()

# sum frame

frame_sum = LabelFrame(text="sum")
frame_sum.pack(fill=BOTH)

sum_field_1 = Entry(frame_sum)
sum_field_1.pack(side=LEFT)

Label(frame_sum, text="+").pack(side=LEFT)

sum_field_2 = Entry(frame_sum)
sum_field_2.pack(side=LEFT)

Button(frame_sum, text="=", command=sum_numbers).pack(side=LEFT)

sum_result = Entry(frame_sum)
sum_result.pack(side=LEFT)

# subtract frame

frame_subtract = LabelFrame(text="subtract")
frame_subtract.pack(fill=BOTH)

subtract_field_1 = Entry(frame_subtract)
subtract_field_1.pack(side=LEFT)

Label(frame_subtract, text="-").pack(side=LEFT)

subtract_field_2 = Entry(frame_subtract)
subtract_field_2.pack(side=LEFT)

Button(frame_subtract, text="=", command=subtract_numbers).pack(side=LEFT)

subtract_result = Entry(frame_subtract)
subtract_result.pack(side=LEFT)


# multiplication frame


frame_multiply = LabelFrame(text="multiplication")
frame_multiply.pack(fill=BOTH)

multiply_field_1 = Entry(frame_multiply)
multiply_field_1.pack(side=LEFT)

Label(frame_multiply, text="*").pack(side=LEFT)

multiply_field_2 = Entry(frame_multiply)
multiply_field_2.pack(side=LEFT)

Button(frame_multiply, text="=", command=multiply_numbers).pack(side=LEFT)

multiply_result = Entry(frame_multiply)
multiply_result.pack(side=LEFT)


# division frame


frame_divide = LabelFrame(text="division")
frame_divide.pack(fill=BOTH)

divide_field_1 = Entry(frame_divide)
divide_field_1.pack(side=LEFT)

Label(frame_divide, text="/").pack(side=LEFT)

divide_field_2 = Entry(frame_divide)
divide_field_2.pack(side=LEFT)

Button(frame_divide, text="=", command=divide_numbers).pack(side=LEFT)

divide_result = Entry(frame_divide)
divide_result.pack(side=LEFT)


root.mainloop()