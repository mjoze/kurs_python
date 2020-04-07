"""Znajdź największa wspólny dzielnik (NWD) dwóch liczby. Wykorzystaj algorytm Euklidesa."""


def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def nwd2(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


c = nwd2(100, 300)
print(c)