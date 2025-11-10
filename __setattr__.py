"""__setattr__() is magic or special or dunder method in Python. This method or function is used
called while we are assigning a  values to the attribute and execute the statements which statemets we are used inside the function
"""


class details:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"the name of the student is {self.name} and the age of the student is {self.age}"

    def __repr__(self):
        return "the class name is details"

    def __getattr__(self, other):
        return f"the instance variable {other} is not existed in this class"

    def __setattr__(self, name, value):
        print(
            f"the assigned variable name is {name} and the value assinged variable is {value}"
        )
        super().__setattr__(name, value)


var = details("Alice", 23)
var.mark = 35
print(var.mark)
