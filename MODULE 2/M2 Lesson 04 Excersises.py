# Task 1
# Заполните список из пяти элементов случайными числами.
# Используйте в коде цикл for, функции range() и randint().

# from tkinter import *
# from random import randint
#
#
# root = Tk()
#
# random_list = [randint(100, 200), randint(100, 200), randint(100, 200), randint(100, 200),  randint(100, 200)]
#
# for i in random_list:
#     Button(text=i).pack()
#
# root.mainloop()


# from tkinter import *
# from random import randint
#
#
# root = Tk()
#
# for _ in range(5):
#     random_number = randint(100, 200)
#     Button(text=random_number).pack()
#
# root.mainloop()



# Task 2

# Если объект range(диапазон) передать встроенной в Python функции list(),
# то она преобразует его к списку. Создайте таким образом список с элементами от 0 до 100 и шагом 17.


from tkinter import *
from random import randint

# list_range = list(range(1, 100, 17))
#
# print(list_range)


# Task 3

# В заданном списке, состоящем из положительных и отрицательных чисел,
# посчитайте количество отрицательных элементов. Выведите результат на экран.

# given_array = [-2, 5, 10, -40, -7, -134, 5, 18]
#
# i = 0
#
# for element in given_array:
#     if element < 0:
#         i += 1
#
# # print(given_array)
# print(f"Negative numbers: {i}")


# Task 4
# Напишите программу, которая содержит список из пяти слов, измеряет длину каждого слова и добавляет полученное значение
# в другой список. Например, список слов – ['yes', 'no', 'maybe', 'ok', 'what'],
# список длин – [3, 2, 5, 2, 4]. Оба списка должны выводиться на экран.

# words_list = ['yes', 'no', 'maybe', 'ok', 'what']
#
#
# print(words_list)
#
# len_list = []
#
# for word in words_list:
#
#     len_list.append(len(word))
#
# print(len_list)

#Task 4

# Напишите программу генерации кнопок, английских кнопок. Названия берутся из списка: ['yes', 'no', 'maybe', 'ok', 'what'].
# При нажатии на любую кнопку происходит перевод, смена на русские названия: ["да", "нет", "наверно", "ок", "что"].

# from tkinter import *
#
# your_array = ["да", "нет", "наверно", "ок", "что"]
#
#
# def translate_word(_index):
#     # print(your_array[_index])
#     if _index == 0:
#         buttonIndex="!button"
#     else:
#         buttonIndex="!button" + str(_index+1)
#         # print(buttonIndex)
#
#     root.children[buttonIndex]["text"] = your_array[_index]
#
#
# root = Tk()
#
# buttons_list = ['yes', 'no', 'maybe', 'ok', 'what']
#
#
# for i in range(len(buttons_list)):
#     Button(text=buttons_list[i], command=lambda j=i: translate_word(j)).pack()
#
# # for child in root.children:
# #     root.children[child]["text"] = "new text"
# #     print(root.children[child])
#
# root.mainloop()


# from tkinter import *
#
#
# buttons_en = ['yes', 'no', 'maybe', 'ok', 'what']
#
# buttons_ru = ["да", "нет", "наверно", "ок", "что"]
#
#
# def translate_word(button,index):
#     button.config(text=buttons_ru[index])
#
#
# root = Tk()
#
# for index, text in enumerate(buttons_en):
#     button = Button(text=text)
#     button.pack()
#     button.config(command=lambda widget=button, i=index: translate_word(widget,i))
#
# root.mainloop()

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)