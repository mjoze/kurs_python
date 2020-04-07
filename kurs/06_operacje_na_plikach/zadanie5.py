with open('tekst.txt', 'r', encoding='utf-8') as f:
    lines = f.read()

txt = lines.split()
max_length = ''
for i in txt:
    if len(i) > len(max_length):
        max_length = i
print(max_length)
