"""1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem
lub białym znakiem). Następnie powitaj każdą osobę na liście."""
# names = input("Podaj dowolną liczbę imion podzielone spacja")
# names = names.split()
names = ['as', 'ss', 'ss', 'iu']
for i in names:
    print("hello", i)

id = 0
while id < len(names):
    print(names[id])
    id = id + 1

