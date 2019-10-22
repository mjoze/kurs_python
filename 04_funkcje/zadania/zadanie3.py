""" Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb.
maximum_of(a, b, c)."""


def my_max(a, b, c):
    """return the minimum element of sequence"""
    list_number = [a, b, c]
    max_n = list_number[0]
    for i in list_number:
        if i > max_n:
            max_n = i
    return max_n


a = my_max(2, 1, 34)
print(a)
