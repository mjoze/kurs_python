"""W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery,
cyfry i znaki specjalne."""

txt = "ciAsteczk#o24$"
l_c = 0
u_c = 0
num = 0
special = 0
for i in txt:
    if i.islower() and i.isalpha():
        l_c += 1
    if i.isupper():
        u_c += 1
    if i.isdigit():
        num += 1
    if not i.isalpha() and not i.isdigit():
        special += 1
print("liczba małych liter:", l_c)
print('liczba dużych liter {}'.format(u_c))
print('w ciągu mamy', num, 'cyfry')
print(special)