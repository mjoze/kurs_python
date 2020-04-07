""" Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia."""

r_circle = float(input('Podaj promień koła'))


def circle_field(r):
    pi = 3.14
    return pi * r ** 2


print(circle_field(r_circle))
