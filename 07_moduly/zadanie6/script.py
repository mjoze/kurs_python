"""6▹ Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.

Wejście:
var = ‘banannnnannnnnnnnnanananananaaaana’

Wyjście
‘nnnnnnnnn’, 9"""

var = "banannnnannnnnnnnnanananananaaaana"

max_count = 1
count = 1

for i in range(len(var)-1):
    if var[i] == var[i+1]:
        count += 1
    else:
        count = 1
    if count > max_count:
        max_count = count

print(max_count)