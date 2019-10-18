"""Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

output:

[4, 3, 2, 1]
[14, 13, 12, 11]
[24, 23, 22, 21]"""

numbers = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
num1 = numbers[:int(len(numbers)/3)]
num1.reverse()
print(num1)
num2 = numbers[int(len(numbers)/3):(int(len(numbers)/3))*2]
num2.reverse()
print(num2)
num3 = numbers[(int(len(numbers)/3))*2:]
num3.reverse()
print(num3)