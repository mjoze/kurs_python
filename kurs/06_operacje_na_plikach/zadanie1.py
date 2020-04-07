import random

filename = 'quotes.txt '#input("Your file: ")
with open(filename, 'r', encoding='utf-8') as fopen:
    quotes = fopen.readlines()

quote_for_today = random.choice(quotes).strip('')
quote_for_today = quote_for_today.split(' - ')
print("Quote of day is:")
print("*" * 150)
print(quote_for_today[0].center(150))
print(quote_for_today[1].center(150))
print("*" * 150)
