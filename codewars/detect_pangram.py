"""A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence
"The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.

"""
import string


def is_pangram(s):
    new_pangram = []
    test_pangram = string.ascii_lowercase
    for i in s.replace(' ', '').lower():
        if i in string.ascii_lowercase:
            new_pangram.append(i)
    a = ''.join(list(set(new_pangram)))
    if len(a) == len(test_pangram):
        return True
    else:
        return False


"""
import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())"""