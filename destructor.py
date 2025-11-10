"""destructor --> __del__() is called special method or magic method in Python
This function is called automatically by Python engine while we tried to delete any instanc object
The statement executed which we mentioned inside this function
"""


class details:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"the name of the student is {self.name} and the age of the student is {self.age}"

    def __repr__(self):
        return "the class name is details"

    # def __getattr__(self, other):
    #     return f"the instance variable {other} is not existed in this class"

    # def __setattr__(self, name, value):
    #     print(
    #         f"the assigned variable name is {name} and the value assinged variable is {value}"
    #     )
    #     super().__setattr__(name, value)

    def __del__(self):
        print("the instant object is delete successfully")


var = details("Alice", 23)
print(var)
del var
