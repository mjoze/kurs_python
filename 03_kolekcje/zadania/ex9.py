"""5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
Wyświetl najpopularniejszy przedmiot.
(Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)"""
subjects = []
sub_multi = {}
for i in range(5):
    print('Podaj 4 przedmioty szkolne')
    for j in range(4):
        i = input('Witaj podaj {} przedmiot:'.format(j+1)).lower().capitalize()
        subjects.append(i)
# print(subjects)

for i in subjects:
    if i in sub_multi:
        sub_multi[i] += 1
    else:
        sub_multi[i] = 1

max_subject_value = max(sub_multi.values())
max_key_subject = ''

for key, value in sub_multi.items():
    if value == max_subject_value:
        max_key_subject = key
print('Najpopularniejszy przedmiot:', max_key_subject)






