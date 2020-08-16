# array = [10, 40, 20, 30]
# for element in array:
#     print(element + 2)

# from tkinter import *
#
# list_buttons = ["YES", "NO", "CANCEL"]
#
# root = Tk()
#
# Label(text="Do you want to save changes?").pack()
#
# for i in list_buttons:
#    Button(text=i).pack()
#
# root.mainloop()

#
# for i in range(10):
#     print(i)


from tkinter import *

root = Tk()

Label(text="Do you want to save changes?").pack()

for i in range(15, 5, -1):
    Button(text=i+10).pack()

root.mainloop()

#
# array = [10, 40, 20, 30]
# i = 0
# for element in array:
#     array[i] = element + 2
#     i += 1
#
# print(array)


