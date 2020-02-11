"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines
whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""


def is_isogram(string):
    return len(string) == len(set(string.lower()))


"""
def is_isogram(string):
    string_lower = string.lower()
    string_list = []
    for i in string_lower:
        if string_lower.count(i) > 1:
            string_list.append(i)
    return True if len(string_list) == 1 or len(string_list) == 0 else False
"""