"""Wisielec. Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc. Poproś użytkownika o podanie
kategorii przed rozpoczęciemy gry. Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy.
Rozgrywka powinna być maksymalnie intuicyjna."""

import random
import json


def choose_category():
    with open('words.json', encoding='utf-8') as f:
        data = json.load(f)
    print('Dostępne kategorie:')
    for key in data:
        print('--' + key)
    category = input('wybierz')
    if category in data.keys():
        _words = []
        for key, values in data.items():
            if key == category:
                _words.append(' '.join(values).split())
        _words = _words[0]
        return _words
    else:
        print("Wybrałeś złą nazwę kategorii. Spróbuj ponownie")
        return choose_category()


def make_words(a):
    puzzle = random.choice(a)
    puzzle_list = []
    for i in puzzle:
        puzzle_list.append(i)
    return puzzle_list



def game():
    b = choose_category()
    c = make_words(b)
    puzzle_list_answear = []
    for _ in range(len(c)):
        puzzle_list_answear.append('-')
    print('Długość hasła', len(puzzle_list_answear))
    while True:
        letter = input('litera')
        if letter not in c:
            print('brak tej litery')
        if letter in puzzle_list_answear:
            print('ta litera już była')
        else:
            for i in range(len(c)):
                if c[i] == letter:
                    puzzle_list_answear[i] = letter
                if c == puzzle_list_answear:
                    print("brawo")
                    print(c)
                    return False
        print(puzzle_list_answear)

game()