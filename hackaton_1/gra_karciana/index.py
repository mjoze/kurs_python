import random


def losowanie_kart(liczba_kart):
    cards_name = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2',
                  '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    talia = []
    while len(talia) < liczba_kart:
        talia.append(random.choice(cards_name))
    return talia


def kto_wygra(user_card, computer_card):
    cards_rules = {
        0: [2, "2"],
        1: [3, '3'],
        2: [4, '4'],
        3: [5, '5'],
        4: [6, '6'],
        5: [7, '7'],
        6: [8, '8'],
        7: [9, '9'],
        8: [10, '10'],
        9: [11, 'J'],
        10: [12, 'Q'],
        11: [13, 'K'],
        12: [14, 'A']
    }
    for key, value in cards_rules.items():
        if user_card == value[1] and computer_card == value[1]:
            user_card = value[0]
            computer_card = value[0]
        if user_card > computer_card:
            return True
        if user_card == computer_card:
            return print("remis")
        else:
            return False


def wybor_karty_user(user):
    print("user", user)
    karta_user = input("wybierz kartę")
    return karta_user


def wybor_karty_computer(computer):
    print("computer", computer)
    karta_computer = random.choice(computer)
    print("komputer wybrał:", karta_computer)
    return karta_computer


def game_mode1(user_talia, computer_talia):
    user_counter = 0
    computer_counter = 0

    while len(user_talia) > 0:
        a = wybor_karty_computer(computer_talia)
        try:
            b = wybor_karty_user(user_talia).upper()
            c = kto_wygra(a, b)
            if c is True:
                computer_counter += 1
            if c is False:
                user_counter += 1
            else:
                pass
            user_talia.remove(b)
            computer_talia.remove(a)
            print("wygrane usera", user_counter)
            print("wygrane computera", computer_counter)
        except Exception:
            print("Brak karty na ręce. Błąd:")
            game_mode1(user_talia, computer_talia)
    return print("Wygrana użytkownika") if user_counter > computer_counter else print("Wygrana komputera")


user_talia1 = losowanie_kart(10)
computer_talia1 = losowanie_kart(10)
game_mode1(user_talia1, computer_talia1)
