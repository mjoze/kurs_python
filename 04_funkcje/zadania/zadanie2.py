"""Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb.
minimum_of(a, b, c)."""


def minimum_of(a, b, c):
    if a < b:
        i = a
        a = b
        b = i
    if a < c:
        i = a
        a = c
        c = i
    if b < c:
        i = b
        b = c
        c = i
    # print(c)
    return c


x_min = minimum_of(487, 210, 890)
print(x_min)
