""" Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku. Napisz funkcję,
która przyjmie wartości i wyświetli średnią. Program powinen być odporny na błędy użytkownika.
Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku."""
numbers = input("liczby")
numbers = numbers.split(',')
print(numbers)
exceptions = []

for index, elem in enumerate(numbers):
    try:
        numbers[index] = float(elem)
    except (ValueError, TypeError) as exc:
        exceptions.append(exc)
        numbers[index] = '-'

print(numbers)

while '-' in numbers:
    numbers.remove('-')
print(numbers)
try:
    avg = sum(numbers)/len(numbers)
except ZeroDivisionError as e:
    exceptions.append(e)
print(exceptions)
with open('exceptions.txt', 'w') as f:
    f.write('blad')
    for i in exceptions:
        f.write(str(i) + '\n')

