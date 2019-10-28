# filename = 'tekst.txt'
#
# with open(filename, 'r') as fopen:
#     content = fopen.read()
#     print(content)
# #
# with open('tekst.txt', 'r') as fopen:
#     while True:
#         current_line = fopen.readline()
#     # aktualna linia jest pusta
#         if current_line == '':
#          # dotarlismy do konca
#             break
#         print(current_line)











with open('tekst.txt', 'r', encoding='utf-8') as fopen:
    lines = fopen.readlines()

for l in range(len(lines)):
     print("Line " + str(l), lines[l].strip('\n'), end="*")
