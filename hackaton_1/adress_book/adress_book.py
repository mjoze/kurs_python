

import random

book = {1: {'name': "Anna", 'surname': 'Kamińska', 'mail': 'anna.kaminska@gmail.com'},
        2: {'name': "Marek", 'surname': "Płaski", 'mail': 'marek.plaski@gmial.com'},
        }


def view(x):
    for key, value in book.items():
        print(value)
    return book


def add_contact(name_to_add, surname_to_add, mail_to_add):
    index_book = random.randrange(1, 1000)
    book[index_book] = {'name': name_to_add, 'surname': surname_to_add, 'mail': mail_to_add}
    return book


def del_contact(txt):
    num_to_del = 0
    for key, value in book.items():
        for i in value.values():
            if i == txt:
                num_to_del = key
    if num_to_del == 0:
        print('Error. Name not in adress book')
    else:
        book.pop(num_to_del)
    return book


def exit_program(ex):
    if ex == 'Q':
        print("Program is closed")
    return


start_app = True
while start_app:
    print('||', "Show adress book", '||', "---- press A")
    print('||', "Add new contact ", '||', "---- press B")
    print('||', "Remove contact  ", '||', "---- press R")
    print('||', "Exit program   ", ' ||', "---- press Q")
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

