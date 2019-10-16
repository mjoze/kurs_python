"""Napisz program z wykorzystaniem pętli while, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55"""
num = 1
suma = 0
while num <= 10:
    suma += num
    num +=1

    print(suma, ' ',  end="")
