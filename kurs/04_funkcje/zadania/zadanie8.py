""" Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
Program zacznie ze stworzonym słownikiem o trzech kluczach:
marka (str)
model (str)
rocznik (int)
Wypisze ten słownik na ekran (bez żadnego formatowania)
Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
“Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
Jeśli nie spełnia powyższego warunku, wypisze komunikat:
“Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!),
aby zobaczyć, czy progam również zmienia swoje zachowanie."""


def check_old_car(brand="audi", model="b80", year=1985):
    car = {
        'marka': '',
        'model': '',
        'rocznik': 0
    }
    if 2019 - car['rocznik'] >= 25:
        car['marka'] = brand
        car['model'] = model
        car['rocznik'] = year
        print("Gratulacje! Twój samochód {} może być zarejestrowany jako zabytek.".format(car['marka']))
    for k, v in car.items():
        print(k, v)


check_old_car()
