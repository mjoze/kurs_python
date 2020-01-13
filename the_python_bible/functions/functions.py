def add(x, y):
    return x + y


def add2(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


def rev(text):
    return text[::-1]


def foo(**kwargs):
    for key, value in kwargs.items():
        print("{},{}".format(key, value))


