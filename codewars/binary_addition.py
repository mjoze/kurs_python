"""
Implement a function that adds two numbers together and returns their sum in binary.
The conversion can be done before, or after the addition.

The binary number returned should be a string.


"""


def add_binary(a, b):
    sum_a_b = a + b
    binary = []
    while sum_a_b > 0:
        one_binary = sum_a_b % 2
        division = sum_a_b // 2
        binary.append(str(one_binary))
        sum_a_b = division
    binary.reverse()
    return "".join(binary)


"""
def add_binary(a,b):
    return bin(a+b)[2:]
"""