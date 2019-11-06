"""Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się z jedynie z cyfr od 0-9.
 Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika
np. użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
Zaimportuj generator bezpośrednio do programu."""
import random


def numbers_generator(numbers):
    n = []
    for i in range(len(numbers)):
        n.append(str(random.choice(numbers)))

    n.append(str(n[random.randrange(0, len(n))]))
    return n


