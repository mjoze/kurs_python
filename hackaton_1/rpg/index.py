"""- Konieczność użycia modułu `random`.
- Program wypisuje kolejne "przygody" bohatera.
- Przygody są zdefiniowanymi zdaniami, które będą losowo wypełniane odpowiednimi wyrazami,
 np: "(bohater) poszedł do (miejsce) aby (czasownik).
 " może stać się "Jouxdrien II Niemrawy poszedł do tawerny aby zasnąć."
- Historyjka ma mieć zadaną długość i ma być możliwie losowa."""
import name_generator as ng
import random


def place_choice(name):
    for i in miejsca:
        print("--", i)
    place = input("Wybierz cel swojej wędrówki")

    if place in miejsca:
        print("Witaj w {} {}".format(place, name))
    else:
        print("Zły wybór. Porwano cię i uwięziono w lochu")


bohater = {"ruch": ["idź do", "skocz na", "wyjdź z", "zasnął z"],
           "walka": ["uderzył kijem", "ciął toporem", "pchnął mieczem"],
           "dialog": ["nie słucham tych głupot", "zabiję cię"]}
miejsca = ["gospoda", "cmentarz", "klasztor"]

numbers = int(input("enter the number of characters"))
a = ng.generate_name(numbers)
print("Twój bohater to:", a)
place_choice(a)
