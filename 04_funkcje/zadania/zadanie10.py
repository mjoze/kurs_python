""" Stwórz grę wisielec “bez wisielca”.
Komputer losuje wyraz z dostępnej w programie listy wyrazów.
Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
Użykownik podaje literę.
Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
“Trafione!” oraz napis ze znanymi literami.
W przeciwnym wpadku pokaż komunikat:
“Nie trafione, spróbuj jeszcze raz!”.
Możesz ograniczyć liczbę prób do np. 10."""

import random


def game():
    words = ['piła', 'arbuz', 'ciasto', 'wino']
    words = [random.choice(words)]
    ask = []
    words_list = []
    for i in range(len(words[0])):
        words_list.append(words[0][i])
    for i in range(len(words[0])):
        ask.append('-')
    for _ in range(0, 10):
        letter = (input('podaj literę'))
        for x in range(len(words_list)):
            if words_list[x] == letter:
                ask[x] = letter
        if ask == words_list:
            print('koniec')
            break
    print(ask)

game()
