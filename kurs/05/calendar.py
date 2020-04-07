data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
]

# Podpowiedź: Zacznij od funkcji, która wyświetli dni 1 miesiąca. Uruchom ją dla każdego elementu listy dane.
# Pamiętaj, że tydzień ma 7 dni.


def calendar(month):
    month -= 1
    d = data[month][1]
    length = []
    for i in d:
        length.append(i)
    tab = []
    k = - 1
    limit = len(length)
    for i in range(1, 6):
        tab_r = []
        for j in range(0, 7):
            k += 1
            if k > limit - 1:
                break
            tab_r.append(k + 1)
        tab.append(tab_r)

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j], end=" ")
        print()


a = int(input('podaj numer miesąca'))
calendar(a)
