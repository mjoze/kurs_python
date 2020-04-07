"""Korzystając z modułu random stwórz kolejną prostą grę. Komputer losuje słowo z dostępnego zakresu
(posiada listę słów). Następnie litery są mieszane.
Wymieszane litery pokazywane są graczowi.
Gracz musi zgadnąć co to za słowo. Gracz zgaduje do skutku. Dopiero zgadnięcie przerywa grę.
Rozszerzenie: gracz może wybrać na klawiaturze „q” lub „Q”, aby zakończyć grę przed czasem."""
import random

words = ['cola', 'pies', 'kot', 'woda']
words_random = random.choice(words)
word_mix = list(words_random)
random.shuffle(word_mix)
word_mix = ''.join(word_mix)
game = True

while game:
    print("Zgadnij jakie to słowo:", word_mix)
    word = str(input("Podaj słowo"))

    if word == words_random:
        print("Zgadłeś")
        break
    if word == 'q':
        print('koniec')
        break
    if word == 'Q':
        print('koniec')
        break
    else:
        print("spróbuj ponownie")
