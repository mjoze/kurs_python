"""1▹ Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć."""

a = [760, 0, 2.45, "tekst", 100, 2.45, ['a', 23], {1, 2, 3}, 2+3j, {'pl': 'poland', 'en': 'england'}, (32, 67)]

for i in a:
    try:
        result = 10 / i
    except TypeError as e:
        result = "Wyjątek 1" + str(e)
    except ZeroDivisionError as e:
        result = "Wyjątek 2" + str(e)
    print(result)