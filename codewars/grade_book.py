"""
Grade book
Complete the function so that it finds the mean of the three scores passed to it and returns the letter
value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
"""


def get_grade(s1, s2, s3):
    s = (s1 + s2 + s3) // 3
    if s >= 90:
        return "A"
    if s >=80:
        return "B"
    if s >= 70:
        return "C"
    if s >= 60:
        return "D"
    else:
        return "F"
