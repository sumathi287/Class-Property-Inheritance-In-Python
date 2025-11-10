class details:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"the name of the student is {self.name} and the age of the student is {self.age}"


var = details("Alice", 23)
print(var)
