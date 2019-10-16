"""1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem
lub białym znakiem). Następnie powitaj każdą osobę na liście."""
# names = input("Podaj dowolną liczbę imion podzielone spacja")
# names = names.split()
names = ['Asia', 'Saska', 'Ania', 'Jurek']
print("Pętla for")
for i in names:
    print("hello", i)
print('\n', "Pętla while")
i_d = 0
while i_d < len(names):
    if i_d == (len(names) - 1):
        print("hello", names[i_d])
    else:
        print("hello", names[i_d], end=" | ")
    i_d += 1
