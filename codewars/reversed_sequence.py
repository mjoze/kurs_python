"""
Get the number n (n>0) to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]
"""


def reverse_seq(n):
    numbers_list = []
    for i in range(1, n + 1):
        numbers_list.append(i)
    numbers_list.reverse()
    return numbers_list


"""
def reverse_seq(n):
    return list(range(n, 0, -1))
"""