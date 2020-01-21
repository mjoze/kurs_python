class Employee:

    raise_amount = 1.04

    def __init__(self, first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Pol', 'Madera', 78000, 'Python')
dev_2 = Developer('Test', 'User', 67000, 'Java')
mgr_1 = Manager('Sue', 'Smith', 900000, [dev_1])

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Developer))
# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Employee))
# print(issubclass(Manager, Developer))