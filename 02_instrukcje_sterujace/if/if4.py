"""Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz
czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis."""

a = 'pomarancza23'

if len(a) > 5 and a.count('a') > 0:
    a = a.replace('a', 'z')
    print(a)
