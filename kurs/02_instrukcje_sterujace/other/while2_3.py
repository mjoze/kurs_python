"""
Zapoznaj się z modułem random.

>>> import random
Stwórz prostą grę zgadywankę. Komputer losuje wartość z przedziału od 1-30. Poproś użytkownika o zgadnięcie liczby.
Program pyta użytkownika o podanie liczby tak długo, dopóki gracz nie zgadnie."""

"""Zadanie 3
Rozszerz grę z punktu powyżej. Gracz powinen otrzymać informację czy jego liczba jest za duża czy za mała."""

import random

num_win = random.randrange(1, 30)
# print(num_win)

while 1:
    num = int(input("podaj numer z przedziału 1-30"))

    if num > 30:
        print("wartość ponad przedział")
        num = int(input("podaj numer z przedziału 1-30"))
    if num < 1:
        print("numer za niski")
        num = int(input("podaj numer z przedziału 1-30"))
    if num == num_win:
        print("wygrana")
        break
    else:
        print("Spróbuj ponownie")
