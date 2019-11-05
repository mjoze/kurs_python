"""7▹ Wróć do pierwszego zadania z lekcji o plikach, zmodyfikuj go tak,
aby to użytkownik podawał nazwę pliku z cytatami.
Pamiętaj, by użytkownik po wykonaniu błędnej akcji (np. literówki w nazwie pliku) miał możliwość poprawić swój błąd."""
import random


def quotes_generator(file):
    with open(file + '.txt', encoding='utf-8') as f:
        quotes = f.readlines()

    quote_for_today = random.choice(quotes).strip('')
    quote_for_today = quote_for_today.split(' - ')
    print("Quote of day is:")
    print("*" * 150)
    print(quote_for_today[0].center(150))
    print(quote_for_today[1].center(150))
    print("*" * 150)


while True:
    try:
        files = input('Podaj nazwę pliku')
        quotes_generator(files)
        break
    except FileNotFoundError as fne:
        print("Podałeś zły plik", fne)

