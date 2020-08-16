def cylinder():
    try:
        r = float(input("Enter radius: "))
        h = float(input("Enter hight: "))
    except ValueError:
        return "Wrong value"
    side = 2 * 3.14 * r * h
    circle = 3.14 * r**2
    full = side + 2 * circle
    return full

print(cylinder())