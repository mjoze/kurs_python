"""Przypomnij sobie szkolny wzór na silnię. Zapisz funkcję silnia iteracyjnie np. pętlą for,
a następnie analogiczną funkcję tylko, że rekurencyjnie."""


def silnie(n):
    silnia = 1
    for n in range(1, 1 + n):
        silnia *= n
    return silnia


def sil(n):
    if n in (0, 1):
        return 1
    elif n > 1:
        return n * sil(n - 1)


a = silnie(3)
print(a)
print(sil(2))
