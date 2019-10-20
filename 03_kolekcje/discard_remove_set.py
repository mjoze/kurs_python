txt = {'d', 'r', 'a', 'b', 'k'}
txt.discard('q')
print(txt)
"KeyError if elem is not contained in the set."
txt.remove('b')
print(txt)
"Remove element from the set if it is present."
"remove - error. discard - not"
