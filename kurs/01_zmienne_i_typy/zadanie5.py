# word = "kajak"
# wordReverse = word[::-1]
# print(word == wordReverse)

word = input('wprowadź wyrażenie aby sprawdzić czy to palindrom')
word = word.lower().replace(' ', '')
# print(word)
wordReverse = word[::-1]
# print(wordReverse)
print('to palindrom :', word == wordReverse)

