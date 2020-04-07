""" Napisać funkcję, która sprawdza czy liczba jest parzysta."""

number = int(input("podaj liczbę"))


def is_even(x):
    if x % 2 == 0:
        print("liczba jest parzysta")
    else:
        print('liczba jest nieparzysta')


is_even(number)
