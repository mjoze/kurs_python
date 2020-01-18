"""In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that
value has more than one digit, continue reducing in this way until a single-digit number is produced.
This is only applicable to the natural numbers.
Here's how it works:
digital_root(16)
=> 1 + 6
=> 7
digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6
digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6
digital_root(493193)"""


def digital_root(n):
    sum_digits = 0
    n_converted_to_string = str(n)
    for i in range(len(str(n_converted_to_string))):
        sum_digits += int(n_converted_to_string[i])
    if sum_digits > 9:
        return digital_root(sum_digits)
    else:
        return sum_digits

