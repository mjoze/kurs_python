""" Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części.
W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
ponownie wyświetl zmieniony słownik
Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności.
Dopisz odpowiednie komunikaty."""


def check_old_car(brand="audi", model="b80", year=1985, is_original=True):
    car = {
        'marka': '',
        'model': '',
        'rocznik': 0,
        'is_original': False
    }
    ask_is_original = input("czy samochód posiada conamniej 75% oryginalnych części: tak/nie")
    if ask_is_original.lower() == 'tak':
        car['is_original'] = True
        if 2019 - car['rocznik'] >= 25:
            car['marka'] = brand
            car['model'] = model
            car['rocznik'] = year
            print("Gratulacje! Twój samochód {} może być zarejestrowany jako zabytek.".format(car['marka']))
            for k, v in car.items():
                print(k, v)
    elif ask_is_original.lower() == 'nie':
        car['is_original'] = False
        print('Samochód nie może zostać zarejestrowany jako zabytek')
    else:
        print('nie udzieliłeś poprawnej odpowiedzi. nie możemy zweryfikować')




check_old_car()


