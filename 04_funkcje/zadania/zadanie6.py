"""Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji."""
import random

num = int(input("podaj liczbę rund"))


def _game(num_round):
    win_user = 0
    win_ai = 0
    p = "przegrana runda"
    w = "wygrana runda"

    while num_round > 0:
        user_choice = str(input("podaj k,p lub n"))
        ai_choice = random.choice(['k', 'p', 'n'])
        if user_choice == 'koniec':
            break
        if user_choice == 'k' and ai_choice == 'p':
            print(p)
            win_ai += 1
        elif user_choice == 'p' and ai_choice == 'k':
            print(w)
            win_user += 1
        if user_choice == 'p' and ai_choice == 'n':
            print(p)
            win_ai += 1
        elif user_choice == 'n' and ai_choice == 'p':
            print(w)
            win_user += 1
        if user_choice == 'k' and ai_choice == 'n':
            print(w)
            win_user += 1
        elif user_choice == 'n' and ai_choice == 'k':
            print(p)
            win_ai += 1
        if user_choice == ai_choice:
            print('remis')
        num_round -= 1
        print(win_user, win_ai)
        if win_user > win_ai:
            print('Gratulację wygrałeś!')
        else:
            print("Przegrana")


_game(num)
