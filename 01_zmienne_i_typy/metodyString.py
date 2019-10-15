# 1
txt = '12d3345'
print(txt.isnumeric())
# 2
print(txt.center(10, '*'))
# 3
print(txt.rstrip('345'))
# 4
print(txt.isalpha() and not txt.islower())
#5
word = 'bananana'
print(word.count('na'))