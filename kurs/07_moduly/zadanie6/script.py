"""6▹ Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.

Wejście:
var = ‘banannnnannnnnnnnnanananananaaaana’

Wyjście
‘nnnnnnnnn’, 9"""
import longest_sequence as ls


if __name__ == "__main__":
    b = 'banannnnannnnnnnnnanananananaaaana'
    x = ls.longest_sequence(b)
    print(x)

