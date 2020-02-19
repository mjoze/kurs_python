"""
Mamy taką oto listę: lista = [1 ,2, 0, 0, 5, 0, 1]

Naszym zadaniem jest sprawienie by wszystkie zera znalazły się po prawej stronie.

Zatem nasza lista będzie wyglądać tak: lista = [1 ,2, 5, 1, 0, 0, 0]
"""

def check_list(arr):
    new_arr = []
    new_zero = []
    for i in arr:
        if i == 0:
            new_zero.append(i)
        else:
            new_arr.append(i)
    return new_arr + new_zero


