

import random

book = {1: {'name': "Anna", 'surname': 'Kamińska', 'mail': 'anna.kaminska@gmail.com'},
        2: {'name': "Marek", 'surname': "Płaski", 'mail': 'marek.plaski@gmial.com'},
        }


def view(x):
    for k, v in book.items():
        print(v)
    return book


def add_contact(x, y, z):
    w = random.randrange(1, 1000)
    book[w] = {'name': x, 'surname': y, 'mail': z}
    return book


def del_contact(txt):
    n = 0
    for k, v in book.items():
        for i in v.values():
            if i == txt:
                n = k
    if n == 0:
        print('Error. Name not in adress book')
    else:
        book.pop(n)
    return book


def exit_program(q):
    if q == 'Q':
        print("koniec")
    return


start_app = True
while start_app:
    print("Show adress book press A")
    print("Add new contact press B")
    print('Remove contact press R')
    print("Exit program press Q")
    a = input("").upper()
    if a == 'A':
        view(book)
    if a == 'B':
        name = input("Name:").capitalize()
        surname = input('Surname:').capitalize()
        mail = input('Email:')
        add_contact(name, surname, mail)
    if a == "R":
        remove = input("Contact to remove. name or surname").capitalize()
        del_contact(remove)
    if a == "Q":
        exit_program(a)
        start_app = False

