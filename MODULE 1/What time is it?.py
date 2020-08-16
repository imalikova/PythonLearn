input_time = int(input("What time is it?  "))


if input_time > 0 and input_time <= 3:
    print("Good night")

elif input_time > 3 and input_time < 12:
    print("Good morning")
elif input_time >= 12 and input_time <= 16:
    print("Good afternoon")
elif input_time > 16 and input_time <= 24:
    print("Good evening")
elif input_time <= 0 or input_time > 24:
    print("Error")

else:
    print('Bad input')


