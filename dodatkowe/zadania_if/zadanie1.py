"""Napisz program, który przyjmuje 2 imiona, a następnie sprawdza czy:
wprowadzone napisy są imionami (hipotetycznie dowolne imię musi składać się jedynie z liter) popraw imiona,
 jeśli są błędnie napisane np. agNIEszka na Agnieszka czy imiona zawierają taką samą liczbę liter czy oba imiona
 zaczynają się od tej samej litery? czy oba imiona kończą się na tę samą literę?"""

name1 = input("Give me the first name.").capitalize()
name2 = input("Give me the second name.").capitalize()

if name1.isalpha() and name2.isalpha():
    print("Names consist of letters", name2, name1)
    if len(name1) == len(name2):
        print("Names contain the same number of letters")
    if name1[0] == name2[0]:
        print("Names begin with the same letter")
    if name1[-1] == name2[-1]:
        print("Names end with the same letter")
else:
    print("They're not names.")
