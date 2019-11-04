# a = 23 + "kot"
# result = 'hello' + 4
# result = input('gadu', 32, 21)
# res = 4 / 0
#
# for i in a:
#     print(a[i])

# f = open('lala.txt')
# content = f.read()
# w = float(input("podaj wagę"))
# h = float(input("podaj wzrost"))
# bmi = "nie zdefiniowane"
# try:
#     bmi = w / h ** 2
# except ZeroDivisionError as e:
#     print("wzrost nie moze byc zerem")
# print(bmi)
#
#
try:
  x = 5 / 0
except ZeroDivisionError as e:
  print("Nie dziel przez zero! Twój wyjątek to:", e)
  x = 0 # potrzebujemy x więc go nadpiszemy
finally:
  print ("Zawsze się wyświetlę")

print(x + 4)