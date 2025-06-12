
# Super class
class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

# Subclass
class Employee(Person):
    def __init__(self, person_id, name, salary):
        super().__init__(person_id, name)
        self.salary = salary


emp = Employee(101, "Oved", 10000)
print("-----------")
