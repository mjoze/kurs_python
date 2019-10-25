"""Love Calculator
Stwórz grę inspirowaną miłosną wróżbą z czasów szkolnych. Zasady gry przedstawia to wideo.
Pobierz imiona zakochanych
Policz wystąpienia każdej z liter w obu imionach oraz słowie LOVE.
Redukuj liczbę elementów tablicy dodając pierwszą i ostatnią liczbę do siebie, tak długo, aż zostną dwie cyfry.
Dwie ostatnie cyfry tworzą wartość procentową dopasowania pary wg. wróżby."""


def name_count_letter(x):
    name = {}
    for i in x.lower():
        if i in name:
            name[i] += 1
        else:
            name[i] = 1
    return name


def name_list(_name):
    letter = []
    for i in _name.values():
        letter.append(i)
    return letter


def calc_list(name_lists):
    z = 0
    x = -1
    suma = []
    length = len(name_lists)/2
    if length % 2 == 0:
        while length > 0:
            s = name_lists[z] + name_lists[x]
            suma.append(s)
            z += 1
            x -= 1
            length -= 1
    else:
        while length - 1 > 0:
            s = name_lists[z] + name_lists[x]
            suma.append(s)
            z += 1
            x -= 1
            length -= 1
        middle = int(len(name_lists) / 2)
        suma.append(name_lists[middle])
    return suma


print("Podaj imiona do gry Love Calculator")
a = input("podaj pierwsze imię")
b = input("podaj drugie imię")
x = name_count_letter(a)
y = name_count_letter(b)
q = name_list(x)
w = name_list(y)
name_to_game = q + w
game = len(name_to_game)
a1 = calc_list(name_to_game)
a2 = calc_list(a1)
a3 = calc_list(a2)
if len(a1) == 2:
    print('Dopasowanie w {}{}%'.format(a1[0], a1[1]))
elif len(a2) == 2:
    print('Dopasowanie w {}{}%'.format(a2[0], a2[1]))
else:
    print('Dopasowanie w {}{}%'.format(a3[0], a3[1]))
