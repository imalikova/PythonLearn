new_day_1 = "Monday"
new_day_2 = "Tuesday"
new_day_3 = "Wednesday"

# print(new_day_1, new_day_2, new_day_3)
# print(new_day_1, new_day_2, new_day_3, sep="...")
# print(new_day_1, new_day_2, new_day_3, end="\n")
# print(new_day_1, new_day_2, new_day_3, end="!!!")
# print(new_day_1, new_day_2, new_day_3, end="!!!")
# print(new_day_1, new_day_2, new_day_3, end="!!!")


def write(*text, sep=" ", end="\n"):
    print(*text, sep=sep, end=end)


write(new_day_1, end="!")
write(new_day_2, new_day_3, sep=" % ")
