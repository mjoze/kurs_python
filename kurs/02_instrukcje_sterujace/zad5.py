""" Stwórz grę ciepło zimno.

Komputer losuje liczbę z zakresu od 1 do 100.

Użytkownik podaje swój traf.

Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.

Jeśli użytkownik zgadnie wygrywa gracz.

Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer."""

import random
from math import fabs

ai_choice = random.randrange(1, 100)
print(ai_choice)
shoots = 6
while shoots > 0:
    user_choice = int(input("podaj liczbę od 1 do 100"))
    if ai_choice == user_choice:
        print('wygrana')
        break
    if fabs(ai_choice - user_choice) < 20:
        print('ciepło')
    else:
        print('zimno')
    shoots -= 1
    if shoots == 0:
        print('Przegrana')
