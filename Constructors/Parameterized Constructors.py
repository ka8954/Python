class Employee():
    def __init__(self, sal, ag, ex):
        self.salary = sal
        self.age = ag
        self.expr = ex


e1 = Employee(25000, 21, "Fresher")
e2 = Employee(10000, 30, "Developer")

print(e1.__dict__)
print(e2.__dict__)
