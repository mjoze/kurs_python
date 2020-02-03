"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""


def solution(string, ending):
    return True if ending == string[-len(ending):] or ending == ' ' else False


"""
def solution(string, ending):
    return string.endswith(ending)
"""