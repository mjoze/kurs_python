# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
title = input("Podaj tytuł ksiązki:")
author = input("Podaj nazwisko autora:")
length = input("Podaj liczbę stron:")

# 1.
# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
check = title, 'składa się z liter:', title.isalpha(), '\n', author, 'sklada sie z liter:', author.isalpha(), '\n', length, 'jest wartoscia liczbowa', length.isnumeric()
print(check)

# 2.
# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
title = title.capitalize()
author = author.capitalize()
print(title, author)

# 3.
# Połącz dane w jeden ciąg book za pomocą spacji
all = title + " " + author + " " + length
print(all)

# 4.
# Policz liczbę wszystkich znaków w napisie book
bookLength = len(title)
print(bookLength)