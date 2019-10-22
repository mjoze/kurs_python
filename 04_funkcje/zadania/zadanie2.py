"""Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb.
minimum_of(a, b, c)."""


# def minimum_of(a, b, c):
#     if a < b:
#         i = a
#         a = b
#         b = i
#     if a < c:
#         i = a
#         a = c
#         c = i
#     if b < c:
#         i = b
#         b = c
#         c = i

# return c


def minimum_of(a, b, c):
    numbers_list = [a, b, c]
    min_n = numbers_list[0]
    for i in numbers_list:
        if i < min_n:
            min_n = i
    return min_n


x_min = minimum_of(487, 21, 890)
print(x_min)
