"""Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę
 wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”."""

target = 13
a = int(input('podaj liczbę z przedziału 1 do 100'))

if a == target:
    print('gratulację')
else:
    print("pudło")