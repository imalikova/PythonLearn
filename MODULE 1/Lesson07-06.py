def positive():
    print("positive")


def negative():
    print("negative")


test = int(input("Please input a number:  "))

if test > 0:
    positive()
else:
    negative()
