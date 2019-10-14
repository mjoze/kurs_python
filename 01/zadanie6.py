# Przekopiuj zawartość import this do zmiennej.
a = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# Policz liczbę wystąpień słowa better.
word = 'better'
print(word, 'występuje w tekście:', a.count("better"), 'razy')

# Usuń z tekstu symbol gwiazdki
symbol = '*'
a_n = a.replace('*', '')
# print(a_n)

# Zamień jedno wystąpienie explain na understand
print(a.count('explain'))
a_n2 = a.replace('explain', 'understand', 1)
print(a_n2.count('explain'))
# print(a_n2)

# Usuń spacje i połącz wszystkie słowa myślnikiem
a_n3 = a.replace(' ', '-')
# print(a_n3)

# Podziel tekst na osobne zdania za pomocą kropki

# poprawić używając split

n4_a = a.replace(' ', '.')
print(n4_a)