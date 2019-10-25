"""Stwórz gre w kółko i Krzyżyk dla 2 graczy. Zacznij od najważniejszej części – rozgrywki,
a następnie dodaj menu, opcje takie jak imiona graczy, pomysły własne."""
import random

game = {'A1': '-', 'A2': '-', 'A3': '-', 'B1': '-', 'B2': '-', 'B3': '-', 'C1': '-', 'C2': '-', 'C3': '-'}
game_wins = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'],
             ['A3', 'B3', 'C3'], ['A1', 'B2', 'C3'], ['C1', 'C2', 'C3'], ['A3', 'B2', 'C1']]
ai_choice = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

xo_list = []
x_win = []
o_win = []


def choice_x(x):
    if x not in game.keys():
        print('Podałeś złą wartość')
        return
    elif x not in xo_list:
        game[x] = "X"
        xo_list.append(x)
        x_win.append(x)
        ai_choice.remove(x)
        o = random.choice(ai_choice)
        game[o] = "O"
        xo_list.append(o)
        o_win.append(o)
        ai_choice.remove(o)
        return xo_list, game
    else:
        print('To już było. Wybierz ponownie')


def print_game():
    print('', "1", "2", "3")
    print('A', game['A1'], game['A2'], game['A3'])
    print('B', game['B1'], game['B2'], game['B3'])
    print('C', game['C1'], game['C2'], game['C3'])


print_game()


while True:
    a = input('podaj pozycje x').upper()
    choice_x(a)
    if x_win in game_wins:
        print('x win')
        break
    elif o_win in game_wins:
        print('o win')
        break
    print_game()

