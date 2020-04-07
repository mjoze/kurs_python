""" Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb.
maximum_of(a, b, c)."""


def my_max(a, b, c):
    list_number = [a, b, c]
    max_n = list_number[0]
    for i in list_number:
        if i > max_n:
            max_n = i
    return max_n


a = my_max(26, 190, 78)
print(a)


def max_of(a, b, c):
    return max_of_2(max_of_2(a, b), c)


def max_of_2(first, second):
    return first if first > second else second


x = 3
y = 8
z = 2
result = max_of(x, y, z)
print(result)
