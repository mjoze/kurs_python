"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""


# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
def solution(s):
    if len(s) % 2 != 0:
        s = s + '_'
    n = 0
    iterator = 2
    new_arr = []
    a = len(s) / 2
    while a > 0:
        new_arr.append(s[n: iterator])
        n += 2
        iterator += 2
        a -= 1
    return new_arr


"""
def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
"""

"""
def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]
"""