"""Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n.
Elementy powinny być oddzielone spacją

wejście:

n = 3

tab = [['-', '-', '-']
  ['-', '-', '-'],
  ['-', '-', '-']]
wyjście:

- - -
- - -
- - -"""
n = 3
x = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]

for i in range(n):
    for j in range(len(x[i])):
        print(x[i][j], end=' ')

    print()
