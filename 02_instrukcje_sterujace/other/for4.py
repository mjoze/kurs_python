"""Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy.
Z każdym uruchomieniem pętli wyświetli informacje:
– czy liczba jest wielokrotnością 3
– czy liczba jest wielkorotnością 4
– wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
– wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony"""
num = int(input('ile razy chcesz spróbować?'))

while num > 0:
    a = int(input("podaj liczbę"))
    if a % 3 == 0:
        print('liczba jest wilokrotnością 3')
    if a % 4 == 0:
        print('liczba jest wielokrotnością 4')
    if (a % 3 == 0) and (a % 4 == 0):
        print('hurra liczba dzieli się zarówno przez 3 jak i 4')
    if not ((a % 3 == 0) and (a % 4 == 0)):
        print("*")
    num -= 1
