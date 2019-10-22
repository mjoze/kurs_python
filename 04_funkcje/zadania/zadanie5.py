""" Napisz grę ciepło - zimno tak, aby korzystać z funkcji."""

import random
from math import fabs

shoots = int(input('Podaj liczbę prób'))


def warm_cold(x):
    ai_choice = random.randrange(1, 100)
    print(ai_choice)
    while x > 0:
        user_choice = int(input("podaj liczbę od 1 do 100"))
        if ai_choice == user_choice:
            print('wygrana')
            break
        if fabs(ai_choice - user_choice) < 20:
            print('ciepło')
        else:
            print('zimno')
        x -= 1
        if x == 0:
            print('Przegrana')


warm_cold(shoots)

