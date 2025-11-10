"""
inheritance --> we pass the class name as a argument inside of another class
1. we can access the another class of (parent class) methods and propertiess from child class
2. called parent constructed automatically if we doesn't use constructor inside the child class
3. Called child class constructor if we use constructor inside the child class
    a. we called the parent constructor using
        def __init__(self, name, age): #child class constructor
            super().__init__(name, age)#parent class constructor
4. We can access multiple parent class through single child class"""


class details:  # Parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"the name of the student is {self.name} and the age of the student is {self.age}"

    def mark(self, mark):
        self.mark = mark
        return f"the {self.name} mark is {self.mark}"


class student(details):  # Child class
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return super().__str__()

    def flower(self):
        return "hi welcome to student class"


var = student("Alice", 23)
print(var)
print(var.flower())
print(var.mark(45))
