"""### Wisielec:
Program, będący implementacją gry "wisielec".
- Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
- Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
- Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
- W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć hasło."""

import random

_words = ['ppiłap', 'arbauza', 'coiastoo', 'woinoo']
ask = []
words_list = []


def generate(words_to_generate):
    guess = random.choice(words_to_generate)
    words = [guess]
    for i in range(len(words[0])):
        words_list.append(words[0][i])
    for i in range(len(words[0])):
        ask.append('-')
    return guess



def game(guess1):
    print('Password length', len(ask))
    for _ in range(0, 10):
        letter = (input('letter or type /ask/ to guess '))
        if letter == 'ask':
            a = input("guess")
            if a == guess1:
                print(a)
                break
        else:
            if ask.count(letter) > 1:
                print("it's been already ")
            else:
                for x in range(len(words_list)):
                    if words_list[x] == letter:
                        ask[x] = letter
                        # print(letter)
                print(ask)
                if ask == words_list:
                    print('End. Password is:', ask)
                    break


a = generate(_words)
print(a)
game(a)
