
import random

game = {'A1': '-', 'A2': '-', 'A3': '-', 'B1': '-', 'B2': '-', 'B3': '-', 'C1': '-', 'C2': '-', 'C3': '-'}
game_wins = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'],
             ['A3', 'B3', 'C3'], ['A1', 'B2', 'C3'], ['C1', 'C2', 'C3'], ['A3', 'B2', 'C1']]
ai_choice = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

xo_list = []
x_win = []
o_win = []


def choice_x(x, user_sign, ai_sign):
    user_sign = user_sign
    ai_sign = ai_sign
    if x not in game.keys():
        print("You've given the wrong value")
        return
    elif x not in xo_list:
        game[x] = user_sign
        xo_list.append(x)
        x_win.append(x)
        ai_choice.remove(x)
        o = random.choice(ai_choice)
        game[o] = ai_sign
        xo_list.append(o)
        o_win.append(o)
        ai_choice.remove(o)
        return xo_list, game
    else:
        print("It's already been done. Select again")


def print_game():
    print(' ', "1", "2", "3")
    print('A', game['A1'], game['A2'], game['A3'])
    print('B', game['B1'], game['B2'], game['B3'])
    print('C', game['C1'], game['C2'], game['C3'])


print_game()
user = input('Select your sign: ')
ai = input("Select a computer sign: ")
while True:
    a = input("What's the position {}?".format(user)).upper()
    choice_x(a, user, ai)
    if x_win in game_wins:
        print('{} win'.format(user))
        break
    elif o_win in game_wins:
        print('{} win'.format(ai))
        break
    print_game()

