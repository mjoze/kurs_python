"""Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem
 lub białym znakiem). Następnie powitaj każdą osobę na liście."""
names = input("wprowadź imiona rozdzielone przecinkiem")
names = names.split(',')
print(names)
for i in names:
    print("Witaj", i)