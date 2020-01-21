class Employee:

    def __init__(self, first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email'.format(self.first, self.last).lower()

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_1 = Employee('Pol', 'Madera', 78000)
emp_2 = Employee('Test', 'User', 67000)
emp_1.first = 'Jim'

emp_1.fullname = 'Bogus Kowalski'

del emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)