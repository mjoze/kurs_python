result = [(x, y) for x in range(10) for y in range(x)]
print(result)

result = []
for x in range(10):
    for y in range(x):
        result.append((x, y))
