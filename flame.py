"""Gra FLAMES¶
FLAMES to popularna gra, której nazwa postała od akronimu: Friends, Lovers, Affectionate, Marriage, Enemies, Sibling.
 Choć gra nie pozwala dokładnie przewidzieć przyszłości to może sprawdzić się jako andrzejkowa wróżba.
Jak znaleźć naszą parę?
Pobierz imion dwóch osób
Usuń wspólne litery występujące w obu imionach..
Policz pozostałe litery.
Użyj wyniku, by znaleźć prawdziwy związek między dwoma osobami.
Dokładne zasady gry FLAMES"""

a = "Mar"
b = "Mausz"

game = ['Friends', 'Lovers', 'Affectionate', 'Marriage', 'Enemies', 'Sibling']
names = {}


def create_names_dict(x):
    for i in list(x):
        if i in names:
            names[i] += 1
        else:
            names[i] = 1
    return names


def count_letter():
    suma = 0
    for k, v in names.items():
        if v == 1:
            suma += 1
    print(game[suma-1])
    return game[suma-1]

create_names_dict(a)
create_names_dict(b)
count_letter()

