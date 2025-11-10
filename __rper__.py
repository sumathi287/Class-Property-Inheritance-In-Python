"""__rper__ () is magic method or dunder method in Python. This function used inside of the class . while we tried to print the instance object that time
this function is called automatically only if __str__()doesn't used inside that class.
Usually programmer used this function for getting details about 'class' . while we called this function
using instance object the statement executed mentioned inside the __repr__()"""


class details:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"the name of the student is {self.name} and the age of the student is {self.age}"

    def __repr__(self):
        return "the class name is details"


var = details("Alice", 23)
print(var.__repr__())
