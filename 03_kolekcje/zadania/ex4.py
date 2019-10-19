"""Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10,
 wypełnioną wynikami mnożenia wiersz × kolumna."""
tab = [[''] * 10 for _ in range(1, 11)]
# multi = list(list(range(1, 11)) for _ in range(1, 11))

for i in range(1, 11):
    tab[i - 1][0] = [i]
    for j in range(1, 11):
        tab[j - 1][0] = j
        tab[i-1][j-1] = i * j
print(tab)
print('-------------')

for i in range(len(tab)):
    for j in range(len(tab[i])):
        print([tab[i][j]], end='')
    print()
print('-------------')
for i in range(1, 11):
    for j in range(1, 11):
        print([i * j], end=" ")
    print()
print('-------------')

