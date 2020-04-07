"""Napisz skrypt obliczający wartość silnii. Rozwiąż zadanie za pomocą pętli for oraz pętli while.
Wejście: „Podaj dowolną liczbę całkowitą do 15:” 4
Wyjście: 4! = 24"""

silnia = 1
num = int(input('Podaj liczbę całkowitą do 15'))
if num > 15:
    print("podałeś za dużą liczbę")
    num = int(input('Podaj liczbę całkowitą do 15'))
n = num
# while n > 0:
#     silnia *= n
#     n -= 1
#     print(silnia)
# print("silnia z {} to {}".format(num, silnia))

for n in range(1, 1 + n):
    silnia *= n
    print(silnia)
