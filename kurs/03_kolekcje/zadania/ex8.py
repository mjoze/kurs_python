"""Słowniki dla 10 krajów Europy utwórz listy 10 najpopularniejszych imion żeńskich.
Za każdym razem zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem.
Nowa lista powinna zawierać 100 elementów.
Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach."""
names = {
'albania':['Amelia', 'Ajla', 'Melisa', 'Amelija', 'Klea', 'Sara', 'Kejsi', 'Noemi', 'Alesia', 'Leandra'],
'austria' : ['Anna',	'Hannah',	'Sophia',	'Emma',	'Marie',	'Lena',	'Sarah',	'Sophie',	'Laura',	'Mia'],
'belgium' : ['Emma',	'Louise',	'Olivia',	'Elise'	'Alice',	'Juliette',	'Mila',	'Lucie',	'Marie',	'Camille'],
'denmark' : ['Sofia',	'Freja',	'Alma',	'Laura',	'Ida',	'Clara',	'Ella',	'Anna',	'Emma',	'Josefine'],
'england' : ['Olivia',	'Amelia',	'Emily',	'Isla',	'Ava',	'Jessica',	'Isabella',	'Lily',	'Ella',	'Mia'],
'finland' : ['Sofia',	'Aino',	'Eevi',	'Venla',	'Emma',	'Aada',	'Pihla',	'Ella',	'Helmi',	'Emilia'],
'france' : ['Emma',	'Louise',	'Jade',	'Alice',	'Chloé', 'Lina',	'Mila',	'Léa',	'Manon',	'Rose'],
'hungry' : ['Hanna',	'Anna',	'Jázmin',	'Lili',	'Zsófia',	'Emma',	'Luca',	'Boglárka',	'Zoé'],
'poland' : ['Zuzanna',	'Julia',	'Lena',	'Maja',	'Hanna',	'Zofia',	'Amelia',	'Alicja',	'Aleksandra',	'Natalia'],
'spain' : ['Lucía',	'Martina',	'María',	'Sofía',	'Paula',	'Daniela',	'Valeria',	'Alba',	'Julia',	'Noa'],
}
# names = albania + austria + belgium + denmark + england + england + finland + france + hungry + poland + spain


names_list = []
for i, j in names.items():
    for k in j:
        names_list.append(k)
names2 = {}
for i in names_list:
    if i in names2:
        names2[i] += 1
    else:
        names2[i] = 1

for k, v in names2.items():
    if v >= 3:
        print(k, end=" ")
