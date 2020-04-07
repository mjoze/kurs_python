""" Utwórz klasę zegaro-kalendarza. Zegaro-kalendarza łączy cechy zegara oraz kalendarza.
Zaimplementuj dziedziczenie wielokrotne. Nasz zegaro-kalendarza powinen móc podawać aktualną datę oraz wyświetlać
ile dni ma dany miesiąc. Dodatkowo utwórz sposób wyświetlania tak, aby zegaro-kalendarz zawierał datę,
godzinę oraz widok dni ułożonych tygodniowo.
Dla uproszczenia przyjmij 7 dni w tygodniu zawsze zaczyna się od pierwszego dnia.
Utwórz obiekty, które będą przekazywać różne strefy czasowe i wyświetlać dzięki temu inne czasy zegara."""

import datetime


class Watch:
    def __init__(self):
        print("Zegarek")

    def show_time(self):
        now = datetime.datetime.now()
        a = datetime.time(now.hour, now.minute, now.second)
        print(a)


class Calendar:

    def __init__(self):
        print("Kalendarz")

    def show_date(self):
        a = datetime.date.today()
        print(a)


class Watch_calendar(Watch, Calendar):

    def current_date_time(self):
        super().show_time()
        super().show_date()


# c = Calendar()
# c.show_date()
# w = Watch()
# w.show_time()

wc = Watch_calendar()
wc.current_date_time()