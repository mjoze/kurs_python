"""Co na prezent?¶
Stwórz listę pomysłów na prezent dla swoich bliskich. Kiedy nadarzy się okazja, aby dać im prezent
 (święta, urodziny, rocznicę), program losowo wybierze jeden (i być może miejsca, w których możesz go zdobyć)."""
import random

gifts = {
        'holidays': ('książka', 'film', 'płyta', 'wino', 'perfumy'),
        'birthday': ('1000zł', '2000zł', '3000zł'),
        'anniversary': ('biżuteria', 'rower', 'czapka')
    }


def choose_gift(x):
    return random.choice(gifts[x])


a = input("Wybierz prezent. Dostępne możliwości: -holidays. -birthday. -anniversary")
b = choose_gift(a)
print('Nasza propozycja to:', b)
