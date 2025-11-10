"""
inheritance --> we pass the class name as a argument inside of another class
1. we can access the another class of (parent class) methods and propertiess from child class
2. called parent constructed automatically if we doesn't use constructor inside the child class
3. Called child class constructor if we use constructor inside the child class
    a. we called the parent constructor using
        def __init__(self, name, age): #child class constructor
            super().__init__(name, age)#parent class constructor
4. We can access multiple parent class through single child class
5.MRO order
    ChildClass  →  Parent1  →  Parent2  →  ...  →  object"""


class details:  # Parent class
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):
        return f"the name of the student is {self.name} and the age of the student is {self.age}"

    def mark(self, student_mark):
        """print the mark info"""
        self.student_mark = student_mark
        return f"the {self.name} mark is {self.student_mark}"


class leader:
    def __init__(self, leader_name):
        self.leader_name = leader_name

    def __str__(self):
        return f"the leader name is {self.leader_name}"

    def leader_status(self, standard):
        self.standard = standard
        return f"the student standard is {self.standard}"


class student(details, leader):  # Child class
    def __init__(self, name, age):
        details.__init__(self, name, age)
        leader.__init__(self, name)

    def __str__(self):
        return f"{details.__str__(self)}\n{leader.__str__(self)}"

    def flower(self, rose):
        self.rose = rose
        return f"the flower name is {self.rose}"


var = student("Alice", 23)
print(var)
print(var.leader_status("5th"))
print(var.flower("white rose"))
print(var.mark(90))
