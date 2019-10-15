"""Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę.
 Wyświetl liczby od największej do najmniejszej."""

a = int(input('podaj 1 liczbę'))
b = int(input('podaj 2 liczbę'))
c = int(input('podaj 3 liczbę'))
# a=3 b=4 c=5
if a < b:
    i = a
    a = b
    b = i
if a < c:
    i = a
    a = c
    c = i
if b < c:
    i = b
    b = c
    c = i
print(a, b, c)