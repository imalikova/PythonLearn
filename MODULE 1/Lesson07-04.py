def func_1():
    print("Step 5", end=" ")

def func_2():
    print("Step 1", end=" ")

def func_3():
    func_2()
    print("Step 2", end=" ")

def func_4():
    print("Step 7", end=" ")

def func_5():
    print("Step 4", end=" ")
    func_1()

func_3()
print("Step 3", end=" ")
func_5()
print("Step 6", end=" ")
func_4()