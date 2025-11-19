# function decorator
def decorator(temp):
    print("Welcome to decorator function")

    def wrap(*args, **arkgs):
        print("Welcome to Wrap function")
        return temp(*args, **arkgs)

    return wrap


@decorator
def display(name, size): #original funciton
    print("Welcome to display function")
    print(
        "The name of the display is {} and the size of the display is {}".format(
            name, size
        )
    )


# display = decorator(display)
# display = memory address of 'wrap'
display("Digital", 45)  # wrap("Digital",45) , here called wrapped function 
print(display.__name__)  # name of the function hold by "display" object
