"""Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
Go challenge Build Tower Advanced once you have finished this :)"""


def tower_builder(n_floors):
    x = 1
    lista = []
    while n_floors > 0:
        n_floors -= 1
        lista.append(' ' * n_floors + '*' * x + ' ' * n_floors)
        x += 2
    return lista
