"""Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
 Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”."""

c = int(input("podaj liczbę"))


def is_number_in(c):
    a = 2
    b = 121
    num_in_range = []
    for i in range(a, b):
        if c == i:
            num_in_range.append(i)
    if not num_in_range:
        print("nie, liczba x jest z poza zakresu")
    else:
        print("tak, liczba x znajduje się w zadanym zakresie")

is_number_in(c)