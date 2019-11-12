def fibonacci(n):
    lista = []
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
        lista.append(b)
    print(lista)
    return b


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbo(n-1) + fibbo(n - 2)


print(fibo(10))
print(fibonacci(10))
