"""### Generator imienia dla Wojownika RPG:
- Konieczność użycia modułu `random`.
- Program generuje wymawialne(!) imię o zadanej długości i dodaje do niego przydomek
(opcjonalnie również tytuł i liczebnik). Np. 'Jouxdrien II Niemrawy'.
- Pomysł jest zainspirowany grą: http://progressquest.com/play/main.html
- Imię musi zaczynać się od wielkiej litery.
- Program można kontynuować używając pomysłu poniżej."""

import random

a = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
b = ['e', 'y', 'o', 'i', 'a', 'u']
new_nick = []
nickname = ['Niski', 'Wielki', "Waleczny", "Kulawy", "Okrągły", "Czeski", "Brudny", "Cichy"]


def generate_name(n):
    for i in range(n):
        if i % 2 == 0:
            new_nick.append(random.choice(a))
        else:
            new_nick.append(random.choice(b))
    nick = random.choice(nickname)
    name =''.join(new_nick).capitalize() + " " + nick
    return name


numbers = int(input("enter the number of characters"))
a = generate_name(numbers)
print(a)