# call the function which is being inside the another function
def decorator_function(temp):  # temp --> wraped function
    # print("the is function_1")
    def wrapped_function(*agr, **agkrs):
        print("first entered in  function_2")
        return temp(*agr, **agkrs)

    return wrapped_function


@decorator_function
def display(name, age):  # actual functio or main function
    print("second entered in display function")
    print("the name is {}".format(name))
    print("the age is {}".format(age))


# display=decorator_function(display)
display("Alice", 34)  # called wrapped_function()
print(display.__name__)  # __name__ shows the function name stored inside the object.
