"""
Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""


def order(sentence):
    arr_sentence = sentence.split(' ')
    dict_s = {}
    for i in arr_sentence:
        for j in i:
            if j.isdigit():
                dict_s[int(j)] = i
    arr = []
    for i in range(1, len(dict_s) + 1):
        arr.append(dict_s[i])
    return ' '.join(arr)


# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
"""
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
"""