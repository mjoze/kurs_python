class Fifo:
    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        return "-".join(self.elements)

    def show(self):
        print(self.elements)

    def get(self):
        if len(self.elements) == 0:
            return 'brak elementów'
        else:
            return self.elements.pop(0)

    def put(self, value):
        self.elements.append(value)



list_elements = ['a', 'b', 'c', 'd']
fifo1 = Fifo(list_elements)

v = input("Podaj element")
fifo1.put(v)
print(fifo1)

