"""Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index oraz wartość.
Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd"""

a = (1, 2, 3, 'tekst')
index = input("wybierz index:")
value = input("wybierz wartość")
try:
    a[index] = value
except TypeError:
    print("Nie możesz zmienić wartości typu Tuple")
