# wrap() -->no inbuild function, we used this function via import module from outside
from functools import wraps


def decorator(temp):
    """
    A decorator function that wraps another function to add extra behavior
    before calling it.

    This decorator prints a welcome message each time the decorated function
    is called, then executes the original function.

    Args:
        temp (function): The original function being decorated.

    Returns:
        function: The wrapped version of the original function, which first
        prints a message and then calls the original function.
    """

    @wraps(temp)
    def wrapper_funcion(*args, **arkgs):
        print("Hi welcome to wrapper_function")
        return temp(*args, **arkgs)

    return wrapper_funcion


@decorator
def display(name, size):
    print("welcome to display function")
    print("the display name is {} and the display size is {}".format(name, size))


# display = decorator(dispaly)

display("Digital", 34)  # called wrapper_function

print(
    display.__name__
)  # we get original function name using wraps() inside the decorator function
print(display.__doc__)
