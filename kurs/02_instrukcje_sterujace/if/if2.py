"""Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik,
 w przeciwnym wypadku wyświetl “Koniec”."""

a = int(input("Podaj liczbę"))
b = int(input("Podaj drugą liczbę"))
sum = a + b

if sum > 100:
    print("twój wynik to", sum)
else:
    print('koniec')