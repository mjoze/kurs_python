import random


def random_quote(words):
    quote_for_today = random.choice(words).strip('')
    return quote_for_today.split(' - ')


def show(quote):
    print("Quote of day is:")
    print("*" * 150)
    print(quote[0].center(150))
    print(quote[1].center(150))
    print("*" * 150)


filename = 'quotes.txt '  # input("Your file: ")
with open(filename, 'r', encoding='utf-8') as f:
    quotes = f.readlines()

for i in range(3):
    sentence = random_quote(quotes)
    print('-------------')
    show(sentence)
