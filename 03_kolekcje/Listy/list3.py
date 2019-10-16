"""Dla podanej przez użytkownika liście liczb całkowitych sprawdź
czy pierwszy i ostatni element są takie same."""

num = []
counter = int(input("Ile liczb"))
# _ gdy nie potrzebujemy zmiennej
for _ in range(counter):
    a = int(input('Podaj liczbę'))
    num.append(a)
print(num)


if num[0] == num[-1]:
    print('pierwszy i ostatni element są takie same')
else:
    print('pierwszy i ostatni element są różne')
