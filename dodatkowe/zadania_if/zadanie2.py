"""2. Poprosić użytkownika o podanie zakresu temperatur, które wg niego są optymalne do uprawiania sportów outdoorowych.
 Użytkownik powinen podać 2 wartość w jednej lini jako zakres oddzielony znakiem specjalnym np. 16 - 23.
Następnie poproś o podanie aktualnej temperatury na dworze.
Sprawdź czy dziś można uprawiać sport na dworze i wyświetl komunikat - temperatura idealna do uprawiania
sportów outdoorowych / pogoda nie sprzyja... .
"""


def opt():
    optimal_temp = input("podaj").split('-')
    if len(optimal_temp) == 2:
        if optimal_temp[1] == '':
            print('nie podałeś pełnego zakresu liczymy od 0')
            optimal_temp[1] = '0'
        return optimal_temp
    else:
        opt()


a = opt()

print(a)
