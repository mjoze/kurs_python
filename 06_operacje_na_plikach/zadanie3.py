import random
filename = 'quotes.txt '#input("Your file: ")
with open(filename, 'r', encoding='utf-8') as fopen:
    quotes = fopen.readlines()

    for i in range(5):
        print(quotes[i], end=' ')