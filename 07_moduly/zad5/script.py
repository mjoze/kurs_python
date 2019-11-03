"""5▹ Stwórz moduł obliczający pola różnych figur. W nowym pliku utwórz skrypt,
który na podstawie podanych składowych kształtów pomieszczeń oraz ich wymiarów zwraca powierzchnię budynku."""

import fields as f


def home_field(number):
    sum_of_rooms = 0
    for i in range(number):
        a = input('Specify the length of the room {}'.format(i + 1))
        if a == '' or a.isalpha():
            print('tutaj')
            return home_field(number)
        else:
            a = int(a)
        b = input('Enter the width of the room {}'.format(i + 1))
        if b == '' or b.isalpha():
            print('tutaj')
            return home_field(number)
        else:
            b = int(b)
        sum_of_rooms += f.rectangle(a, b)
    return sum_of_rooms




n = int(input("Enter the number of rooms"))
field = home_field(n)
print(field)