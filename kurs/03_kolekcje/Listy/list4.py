"""Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same."""

a = int(input('Podaj liczbę elementów '))
elements = []
for _ in range(a):
    if a % 2 == 0:
        x = input("podaj element")
        elements.append(x)
    else:
        print('musisz podać parzystą liczbę')
        break

if len(elements) % 2 == 0 and len(elements) > 0:
    if elements[int(len(elements)/2)] == elements[int(len(elements)/2) - 1]:
        print('2 środkowe elementy są takie same')



