"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""


def pig_it(text):
    word = []
    for i in text.split():
        word.append(i[1:len(i)] + i[0] + 'ay')
    return ' '.join(word)
