"""2. Poprosić użytkownika o podanie zakresu temperatur, które wg niego są optymalne do uprawiania sportów outdoorowych.
 Użytkownik powinen podać 2 wartość w jednej lini jako zakres oddzielony znakiem specjalnym np. 16 - 23.
Następnie poproś o podanie aktualnej temperatury na dworze.
Sprawdź czy dziś można uprawiać sport na dworze i wyświetl komunikat - temperatura idealna do uprawiania
sportów outdoorowych / pogoda nie sprzyja... .
"""


def opt():
    while True:
        optimal_temp = input("Podaj zakres temperatur odpowiedni dla uprawiania sportu").split('-')
        if len(optimal_temp) == 2:
            if optimal_temp[1] == '':
                print('nie podałeś pełnego zakresu liczymy do 100')
                optimal_temp[1] = '100'
            return optimal_temp
        else:
            continue


def act_temp(actual_temp):
    for i in range(int(a[0]), int(a[1])+1):
        if i == actual_temp:
            return True
    return False



a = opt()
try:
    temp = int(input("Podaj aktualną temp."))
except ValueError:
    print("Błędna wartość")
    temp = 0


print("Pogoda idealna") if act_temp(temp) else print("pogoda nie sprzyja")
