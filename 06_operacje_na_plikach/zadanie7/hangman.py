"""Wisielec. Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc. Poproś użytkownika o podanie
kategorii przed rozpoczęciemy gry. Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy.
Rozgrywka powinna być maksymalnie intuicyjna."""

import random
import json


def choose_category():
    with open('words.json', encoding='utf-8') as f:
        data = json.load(f)
    print('Available categories:')
    for key in data:
        print('--' + key)
    category = input('Select')
    if category in data.keys():
        _words = []
        for key, values in data.items():
            if key == category:
                _words.append(' '.join(values).split())
        _words = _words[0]
        return _words
    else:
        print("You have chosen the wrong category name. Try again")
        return choose_category()


def make_words(a):
    puzzle = random.choice(a)
    puzzle_list = []
    for i in puzzle:
        puzzle_list.append(i)
    return puzzle_list



def game(number_of_games):
    b = choose_category()
    c = make_words(b)
    puzzle_list_answear = []
    for _ in range(len(c)):
        puzzle_list_answear.append('-')
    print('Password length', len(puzzle_list_answear))

    while number_of_games > 0:
        letter = input('Enter a letter or write a | ask | to guess the password')
        if letter == 'ask':
            ask = input('Enter your password')
            if ask == ''.join(c):
                print('Win')
                break
            else:
                print("Unfortunately, it's not a password. Try again.")
            continue
        if letter.isnumeric():
            print('You have chosen the numbers')
            continue
        if len(letter) > 1:
            print('Give the letter no word')
            continue
        if letter not in c:
            print('The lack of this letter')
        if letter in puzzle_list_answear:
            print('that letter was already there.')
        else:
            for i in range(len(c)):
                if c[i] == letter:
                    puzzle_list_answear[i] = letter
                if c == puzzle_list_answear:
                    print("Well done.")
                    print(c)
                    return False
        print(puzzle_list_answear)
        if number_of_games == 1:
            print('Game end')
        number_of_games -= 1



number = input('Enter the number of games')
flag = True
while flag:
    if number.isalpha():
        print('You picked a letter. Select a number')
        number = input('Enter the number of games')
    if number.isnumeric():
        number = int(number)
        game(number)
        flag = False
