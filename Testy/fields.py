def check_values(*values):
    for i in values:
        if not isinstance(i, (int, float)):
            raise ValueError(f'Bok {i} musi być wartością numeryczną')


def rectangle(a, b):
    check_values(a, b)
    return a * b
    # pass


def triangle(a, h):
    check_values(a, h)
    return 0.5 * a * h


def trapeze(a, b, h):
    check_values(a, b, h)
    return (a + b)/2 * h


def main():
    print(rectangle(2, 3))
    print(triangle(2, 3))
    print(trapeze(2, 3, 4))


if __name__ == "main":
    main()