import sys
# try:
#     x = float(input("Podaj liczbę"))
#     result = 4/x
# # except ValueError as e:
# #     print("ve", e)
# # except (TypeError, ZeroDivisionError) as e:
# #     print(e)
# except:
#     print("inny błąd")
import sys


# try:
#     x = float(input("podaj liczbę"))
#     result = 4/x
# except Exception as e:
#     print("mój błąd to", e)
#
# print('Początek programu')
# raise ArithmeticError('To jest ogólny wyjątek')
# print('Koniec programu')

# def predict_future():
#   num = int(input("Podaj dowolną liczbę naturalną: "))
#   if num < 0:
#     raise ValueError("To nie jest liczba naturalna!")
#   else:
#     print("Za", 10 * num, "ludzkość będzie mogła się teleportować")
#
# try:
#   predict_future()
# except ValueError as e:
#     print(e)


def hello_exception():
    print('Początek programu')
    raise ArithmeticError('To jest błąd arytmetyczny')
    print('Koniec programu')


try:
    hello_exception()
except ArithmeticError as ex:
    print("błąd", ex)
    print(sys.exc_info())
finally:
    print("inny")
