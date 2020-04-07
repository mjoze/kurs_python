"""8▹ Stwórz moduł, który dla dowolnej wartości n, zwróci ciąg fibonnaciego."""


def fibonnaci(n):
    a, b = n, n + 1
    n = []
    for _ in range(10):
        a, b = b, a + b
        n.append(b)
    return n

