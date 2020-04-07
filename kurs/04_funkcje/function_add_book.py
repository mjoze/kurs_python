

def add_book(dict_books):
    counter = int(input('Ile książek chcesz dodać:'))
    for _ in range(counter):
        title = input("podaj tytuł książki:")
        grade = input("podaj ocenę")
        dict_books[title] = grade
    return dict_books


def read_book_by_grade(libr):
    g = input("Podaj ocenę książki jaką chcesz przeczytać:")
    if g in libr.values():
        # pass
        for title, grade in libr.items():
            if g == grade:
                print(title, " - ocena:", grade)
    else:
        print("nie ma książki o takiej ocenie")


books = {}
books = add_book(books)
print(books)
read_book_by_grade(books)




print('*' * 10)


