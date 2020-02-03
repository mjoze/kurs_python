"""
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""


def find_it(seq):
    seq_dict = {}
    for i in seq:
        if i in seq_dict:
            seq_dict[i] += 1
        else:
            seq_dict[i] = 1
    for key, value in seq_dict.items():
        if value % 2 != 0:
            return key

"""
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""