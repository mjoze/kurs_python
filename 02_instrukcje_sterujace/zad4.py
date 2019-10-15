""" Napisz grę - kamień (k) / papier (p) / nożyce (n).

Użytkownik podaje jedną z 3 figur.

Komputer losuje jedną z 3 figur.

Sprawdź kto wygrał tę rundę.

Zmień kod tak, by użytkownik mógł podac liczbę rund.

Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.

Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’"""
import random

game = input("Czy gramy w kamień, papier, nożyczki. Y/N? ")
if game.upper() == 'Y':
    print('zaczynamy')
else:
    print('dziękujemy może następnym razem')
num_round = int(input("podaj liczbę rund"))
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