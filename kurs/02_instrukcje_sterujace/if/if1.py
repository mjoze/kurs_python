"""Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika
jest podzielna przez 3 bez reszty i wyświetl komunikat “liczba parzysta”."""

n = int(input('Podaj liczbę'))

if n % 3 == 0:
    print('liczba nieparzysta')
else:
    print('liczba parzysta')

print(n)