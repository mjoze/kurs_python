"""Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

Napisz rozwiązanie zarówno z użyciem pętli while jak i for."""

print("while")
temp_F = 0
while temp_F <= 200:
    temp_C = round(5/9 * (temp_F - 32), 2)
    print(temp_F, '=', temp_C, end=' || ')
    temp_F += 20
print("\nfor")
for f in range(0, 220, 20):
    temp_C = round(5 / 9 * (f - 32), 2)
    print(f, '=', temp_C,end=' || ')
