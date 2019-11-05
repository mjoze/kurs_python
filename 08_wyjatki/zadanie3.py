"""Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi podać dowolny index.
Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy."""
x = ['test', 2, True, 2.45, 320, (3, 6), [65, 'ty'], {'a': 67}]
try:
    index = int(input("Podaj index"))
    try:
        value = 1 / x[index]
        print(value)
    except TypeError as e:
        print("Błąd", e)
except ValueError as ve:
    print("brak indeksu")
except IndexError as ie:
    print("indeks poza skalą")

