""" Napisz kod, który zwraca sumę wszystkich wielokrotności 5 lub 7 poniżej liczby N.

Na przykład dla 21 mamy: 5, 7, 10, 14, 15, 20, stąd wynik 71"""


def multi(a, b, n):
    ab_list = []
    for i in range(1, n - 1):
        ab_list.append(a * i)
        ab_list.append(b * i)
    ab_list.sort()
    return ab_list



print(multi(5, 7, 7))

