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
print(word, 'wystepuje w tekscie:', a.count("better"), 'razy')

# Usuń z tekstu symbol gwiazdki
symbol = '*'
n_a = a.replace('*', '')
# print(n_a)

# Zamień jedno wystąpienie explain na understand
print(a.count('explain'))
n2_a = a.replace('explain', 'understand', 1)
print(n2_a.count('explain'))
# print(n2_a)

# Usuń spacje i połącz wszystkie słowa myślnikiem
n3_a = a.replace(' ', '-')
# print(n3_a)

# Podziel tekst na osobne zdania za pomocą kropki
n4_a = a.replace(' ', '.')
print(n4_a)