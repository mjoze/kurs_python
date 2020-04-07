"""Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i
mieć długość conajmniej 8 znaków. Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
Wyświetl różne komunikaty w zależności od rodzaju błędu."""
password = input("Podaj hasło")
alphanum = password.isalnum()
condition_1_upper = alphanum and password.islower()

if len(password) < 8:
    print('Password is too short. Should be 8 chars')
if not alphanum:
    print('Your pass should be alphanumeric')
if password.isalpha():
    print('should contain digits too')
if password.isdigit():
    print('should contain letters too')
if condition_1_upper:
    print('hasło nie zawiera dużej litery')
print('END')



