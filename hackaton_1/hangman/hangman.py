

import random

words_game = ['piła', 'arbuz', 'ciasto', 'wino', 'kolanko']
words_ask = []
words_list = []


def generate(words_to_generate):
    guess = random.choice(words_to_generate)
    words = [guess]
    for i in range(len(words[0])):
        words_list.append(words[0][i])
    for i in range(len(words[0])):
        words_ask.append('-')
    return guess



def game(guess1):
    print('Word length', len(words_ask))
    for _ in range(0, 10):
        letter = (input('Give me the letter or type --ask-- to guess '))
        if letter == 'ask':
            a = input("guess")
            if a == guess1:
                print(a)
                break
        else:
            if words_ask.count(letter) > 1:
                print("it's been already ")
            else:
                for x in range(len(words_list)):
                    if words_list[x] == letter:
                        words_ask[x] = letter
                        # print(letter)
                print(words_ask)
                if words_ask == words_list:
                    print('End. Password is:', guess1)
                    break


a = generate(words_game)
# print(a)
print("|\/| Hangman: Uncover the word |\/|")
game(a)
