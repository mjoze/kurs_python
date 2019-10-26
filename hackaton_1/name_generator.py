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
c = []
nickname = ['Niski', 'Wielki', "Waleczny", "Kulawy", "Okrągły", "Czeski"]


def generate_name(n):
    for i in range(n):
        if i % 2 == 0:
            c.append(random.choice(a))
        else:
            c.append(random.choice(b))
    nick = random.choice(nickname)
    name =''.join(c).capitalize() + " " + nick
    return name


i = int(input("enter the number of characters"))
a = generate_name(8)
print(a)