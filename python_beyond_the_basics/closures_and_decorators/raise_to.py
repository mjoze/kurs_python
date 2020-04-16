def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


square = raise_to(2)
num_a = square(5)
num_b = square(9)
print(num_a)
print(num_b)
