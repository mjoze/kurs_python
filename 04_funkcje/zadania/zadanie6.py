""" Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji."""

import random

# loss : win
rules = {
    'n': 'k',
    'k': 'p',
    'p': 'n',
}


def declare_winner(user, ai, ):
    return (user, ai) if user == ai else (ai if (user in rules.keys() and ai == rules[user]) else user)


def game(n):
    result = {
        'user': 0,
        'ai': 0,
        'draw': 0,
    }
    while n > 0:
        user = input("podaj")
        ai = random.choice(['p', 'k', 'n'])
        print('komputer wybrał: {}'.format(ai))
        score = declare_winner(user, ai)
        if score == user:
            print('wygrana')
            result['user'] += 1
        elif score == ai:
            print('przegrana')
            result['ai'] += 1
        else:
            print('remis')
            result['draw'] += 1
        n -= 1
    return result

