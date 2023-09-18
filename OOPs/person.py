<<<<<<< HEAD
class Person:
    def __init__(self, n, c, d):
        self.name = n
        self.city = c
        self.dept = d

# We're using named parameters i.e. n,c and d
emp = Person(n="sam", c="Pune", d="Sales")

=======
class Person:
    def __init__(self, n, c, d):
        self.name = n
        self.city = c
        self.dept = d

# We're using named parameters i.e. n,c and d
emp = Person(n="sam", c="Pune", d="Sales")

>>>>>>> 69a79bbc7ebf13241089edb722e487619ff6f61f
print(emp.name, "is in", emp.dept, "department")