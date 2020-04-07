"""Napisz funkcję przeszukiwania połówkowego (binarenego),
która przyjmuje dwa parametry - szukany element oraz listę elementów.
 Zwraca informację czy element jest obecny na liście, albo nie.

Wejście:

data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 21
Wyjście:

“Number 21 is on the list”"""


def search(a, b):
    return print("Number {} is on the list".format(a)) if a in b else 0


data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 6
search(elem, data)

