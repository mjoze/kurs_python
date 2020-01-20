class Employee:

    def __init__(self, first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Pol', 'Madera', 78000)
emp_2 = Employee('Test', 'User', 67000)

print(emp_1.email)
print(emp_1.fullname())