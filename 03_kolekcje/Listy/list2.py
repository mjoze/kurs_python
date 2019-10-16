"""2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
"""

num_list = []
for i in range(10):
    x = int(input('Podaj liczbę'))
    if x % 2 == 0:
        num_list.append(x)
print(num_list)
