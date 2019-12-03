import datetime
import holidays



class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod
    def set_min_avg(cls, average):
        cls.min_avg = average

    @staticmethod
    def academic_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'Nie'
        else:
            return 'Tak'

    # @staticmethod
    # def is_holidays(day):
    #     some_day = datetime.datetime.strptime(day, '%Y-%m-%d')
    #     pl_holidays = holidays.Poland()
    #     return True if some_day in pl_holidays else False


obj = Student.is_holidays('2020-09-01')
print(obj)
