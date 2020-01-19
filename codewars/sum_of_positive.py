"""
You get an array of numbers,
return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""


def positive_sum(arr):
    sum_numbers = 0
    if len(arr) > 1:
        for i in arr:
            if i > 0:
                sum_numbers += i
        return sum_numbers
    else:
        return 0


"""
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

"""