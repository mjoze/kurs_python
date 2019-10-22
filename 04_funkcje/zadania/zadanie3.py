""" Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb.
maximum_of(a, b, c)."""

x = [21, 3, 54, 98, 1, 0, 2, 3]


def my_max(list_number):
    """return the minimum element of sequence"""
    max_n = list_number[0]
    for i in list_number:
        if i > max_n:
            max_n = i
    return max_n


a = my_max(x)
print(a)
