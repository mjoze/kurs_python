"""2) Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
 Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie."""


while True:
    user_num = int(input("Zgadnij liczbę od 0-20"))
    secret_num = 5

    if secret_num == user_num:
        print('Zgadłeś. ukryta liczba to:', secret_num)
        break
    else:
        print('Pudło')