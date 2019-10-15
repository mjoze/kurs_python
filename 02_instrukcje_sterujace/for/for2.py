"""Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać.
Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”."""
ingredients = ['Sos pomidorowy', 'Starty żółty ser', 'Szynka', 'salami', 'boczek', 'Pieczarki', 'Kolorowa papryka',
               'Cebula', 'Czosnek']
print("Dodaj:")
for i in ingredients:
    print(i, end=',')
print('\n', "Wrzuć do piekarnika")