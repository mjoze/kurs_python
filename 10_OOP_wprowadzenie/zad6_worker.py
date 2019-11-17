"""Utwórz klasę Pracownik.
Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
Pracownik powinien mieć pole typu boolowskiego zawierające status studenta.
Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
Wszyscy pracownicy mają wspólną nazwę firmy.
Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np."""


class Employee:
    company = "work_for_free"

    def __init__(self, position, salary, name, surname, seniority, is_student):
        self.position = position
        self.salary = salary
        self.name = name
        self.surname = surname
        self.seniority = seniority
        self.is_student = is_student

    def promo(self):
        self.salary *= 1.07
        return self.salary

    def tax(self):
        return self.salary * 0.04

    def health_care(self):
        if self.is_student:
            proc = 0
        else:
            proc = 0.1
        return self.salary * proc

    def employee_email(self):
        primary = (self.name + '.' + self.surname)
        secondary = self.company.replace(' ', '') + ".com"
        email = primary + '@' + secondary
        return email.lower()


obj_e1 = Employee("a", 100, "Adam", "Bigos", 8, False)
print(obj_e1.employee_email())

