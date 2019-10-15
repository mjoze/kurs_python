"""Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
 W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry,
  ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi."""
a = int(input("Podaj 1 ocenę w skali 0-10"))
b = int(input("Podaj 2 ocenę w skali 0-10"))
c = int(input("Podaj 3 ocenę w skali 0-10"))
av = (a + b + c) / 3

if av > 7:
    print("bardzo dobry")
elif av >= 5:
    #av > 6
    print("przeciętna")
else:
    print("nie warta uwagi")

