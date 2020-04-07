""" Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób,
natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
Dorota, Wellman, dziennikarka
Adam, Małysz, sportowiec
Robert, Lewandowski, piłkarz
Krystyna, Janda, aktorka
Wyświetl w sposób przyjazny dla użytkownika"""

names = [['Dorota', 'Wellman', 'dziennikarka'], ['Adam', 'Małysz', 'sportowiec'], ['Robert', 'Lewandowski', 'piłkarz'],
         ['Krystyna', 'Janda', 'aktorka'], ['Krystian', 'Panda', 'aktor']]
for i in names:
    print('Imię:', i[0], '||', 'Nazwisko:', i[1], '||', 'zawód:', i[2])
print('---------')

for row in range(len(names)):
    for col in range(len(names[row])):
        if col == 1:
            print(names[row][col], end=' - ')
        elif col == 2:
            print(names[row][col], end=' * ')
        else:
            print(names[row][col], end=' ')
    print()
print('----------')
# for i in range(len(names)):
#     for j in range(len(names[i])):
#         print(names[i][j], end=" ")
#     print()
