lista_obiektów = ['dom', 'szkoła', 'kościół', 'bar', 'szpital', 'kino', 'teatr']
# graph = {
#     0: [1, 2, 3],
#     1: [0, 4],
#     2: [0, 3, 5],
#     3: [0, 2, 4],
#     4: [1, 3, 5, 6],
#     5: [2, 4, 6],
#     6: [4, 5]
# }
# graph = [(0,1),(0,2),(0,3),(1,4),(2,3)]
graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

for row in range(4):
    print(lista_obiektów[row], ':')
    for col in range(5):
        if graph[row][col] == 1:
            print(lista_obiektów[row], "<-->", lista_obiektów[col])