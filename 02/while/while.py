# zamienic string metoda split na tablice, podaj trzy przedmioty i 3 oceny. wyswietl przedmiot i ocene
subject = input("Podaj przedmiot oddzielając je myślnikiem")
grade = input("Podaj oceny oddzielając je myślnikiem")
subject = subject.split('-')
grade = grade.split('-')

i = 0
while i < 3:
    print(subject[i], "-", grade[i])
    i = i + 1

