"""what is property --> using property we can access the method as a attribute
    proper definition -->A property in Python is a special built-in feature that allows you to control access to instance attributes — by defining getter, setter, and deleter methods
    why it is called property -->It’s called a property because it represents the “characteristic” or “attribute” of an object,
but with extra control — like validation, computation, or read-only access — just like real-world properties of something.

"""


class student:
    def function1(self):
        print("function2")

    @property
    def function2(self):
        return f"hi this is getter function2"

    @function2.setter
    def function2(self, mark):
        print(mark)

    @function2.deleter
    def function2(self):
        print("the function2 is successfully deleted")


var = student()
var.function2 = 23
print(var.function2)
del var.function2
