# call the function which is being inside the another function
def function_1():
    print("the is function_1")

    def function_2():
        print("the is function_2")

    return function_2


temp = function_1()
temp()
