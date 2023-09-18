class Person:
    def __init__(self, n, c, d):
        self.name = n
        self.city = c
        self.dept = d

# We're using named parameters i.e. n,c and d
emp = Person(n="sam", c="Pune", d="Sales")

print(emp.name, "is in", emp.dept, "department")