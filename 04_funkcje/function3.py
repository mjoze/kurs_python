"""Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście."""

numb_list = [1, 2, 3, 4, 8]


def sum_numbers(numbers):
    sum_n = 0
    for i in numbers:
        sum_n += i
    return sum_n


a = sum_numbers(numb_list)
print(a)
