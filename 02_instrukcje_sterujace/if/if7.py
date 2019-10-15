"""Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności
od wyniku: niedowaga / waga normalna / nadwaga / otyłość."""

weight = float(input('ile ważysz?'))
height = float(input('ile masz wzrostu?'))
BMI = weight / (height ** 2)
print(BMI)
if BMI < 18.5:
    print("niedowaga")
if BMI > 18.5:
    print("waga normalna")
if BMI > 25:
    print('nadwaga')
if BMI > 30:
    print('otyłość')
