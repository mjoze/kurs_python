"""Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
(N podane przez użytkownika, ale nie większe niż 8)."""

a = int(input('podaj liczbę mniejszą niż 8'))
silnia = 1
if a < 8:
    for i in range(1, 1 + a):
        silnia = silnia * i
        print(silnia, i)
    print('silnia z {} wynosi {}'.format(a, silnia))
else:
    print('podana liczba jest większa niż 8')