"""Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)"""
x = [1, 2, 3, 4, 5, 6, 21]


def is_even(numb_list):
    even_elements = []
    for i in numb_list:
        if i % 2 == 0:
            even_elements.append(i)
    print(even_elements)


is_even(x)