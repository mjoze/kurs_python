""" ▹ Utwórz generator dowolnego typu np. generator zdań, tweetów czy konferencji. Dane wejściowe pobierz z pliku csv
(plik csv możesz traktować jako plik txt ze znanym znakiem podziału),
który będzie przechowywał dane potrzebne do generowania.
Przykład z generatora konferencji: http://generatorkonferencji.pl (niektóre potrafią wyjść zabawne).
Wygenerujcie kilka. Czy widzicie wzorzec?
Przykład generatora cytatów: http://wisdomofchopra.com/ (Można wykorzystać istniejące dane wejściowe json,
lub przepisać na własny format danych)."""
import json
import random


def generator(n):
    txt = ''
    for i in range(n):
        category = input("Select categories")
        txt += random.choice(data[category]) + ' '
        print(txt)
    return txt


with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

for key in data.keys():
    print(key, end=", ")
print()

number = int(input("Give me how many words you're building a quote from."))
c = generator(number)
print(c)
