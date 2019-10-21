""" Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych
użytkownika oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość)
 w zależności od otrzymanego parametru."""


def calc_bmi(weight, height):
    return weight / height ** 2


def bmi_status(bmi):
    if bmi < 19:
        print("niedowaga")
    elif bmi < 25:
        print("waga normalna")
    elif bmi < 30:
        print("nadwaga")
    else:
        print("otyłość")


h = 1.85
w = 75

bmi = calc_bmi(w, h)
print(bmi)
bmi_status(bmi)
