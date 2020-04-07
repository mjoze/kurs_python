"""Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.
"""
example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

a = tuple(list(set(example_list)))
print(a)
a_max = max(a)
print(a_max)
a_min = min(a)
print(a_min)