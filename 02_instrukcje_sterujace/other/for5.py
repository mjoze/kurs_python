"""Spróbuj wyświetlić choinkę z trójkątów w taki sposób, aby każdy poziom choinki był o 1 wiersz dłuższy:"""


for i in range(2, 5):
    for j in range(i):
        print((j+1) * '*')
