""" Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie
z pierwszej krotki, a oraz nieparzystych elementów z drugiej."""

a = (1, 'a', 'p', 4, 6)
b = (23, 'o', 'k')
c = []
for i in a:
    if a.index(i) % 2 == 0:
        c.append(i)
for i in b:
    if b.index(i) % 2 != 0:
        c.append(i)
print(c)
