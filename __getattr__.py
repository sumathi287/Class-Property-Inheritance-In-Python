"""__getattr__() function is called automatically by Python engine while we tried to
access the undeclared instance variable or class variable."""


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


var = details("Alice", 23)
print(var.mark)
