"""Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).
Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"""
# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python


def to_camel_case(text):
    index = []
    for i in text:
        if not i.isalpha():
            index.append(text.index(i))
    for i in index:
        text = text.replace(text[i], ' ')
    lista = text.split()
    new_lista = []
    for i in range(len(lista)):
        if i > 0:
            new_lista.append(lista[i].title())
        else:
            new_lista.append(lista[i])
    return ''.join(new_lista)


"""def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s"""