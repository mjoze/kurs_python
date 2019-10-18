""" W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce
Zadbaj o sposób wyświetlania np.:

szybko : 5

zbudź : 1"""
txt = "Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce"
txt = txt.lower()
a = txt.split()
dict_txt = {}
for i in a:
    if i in dict_txt:
        dict_txt[i] += 1
    else:
        dict_txt[i] = 1
print(dict_txt)
# ladnie wyswietlic slownik

