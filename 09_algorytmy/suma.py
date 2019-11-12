def suma(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s


def suma_while(n):
    s = 0
    while n > 0:
        s = s + n
        n = n - 1
    return s


def suma_recursion(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursion(n-1)


number = 10
print('while', suma_while(number))
print('for', suma(number))
print('rec', suma_recursion(number))