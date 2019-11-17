
import random


class Dog:
    tail = True

    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    # def pseudo(self):
    #     adj = ["destroyer", "powerful", "funny", "sweet"]
    #     return self.name + "-" + random.choice(adj)
    def bark(self):
        return "hau" * self.age

obj_pimpek = Dog('Pimpek', 'Collie', 5, 'white')
obj_dyzio = Dog("Dyzio", "Cotton de tulear", 7, "blond")

print(Dog.bark(obj_dyzio))
names = "Anna, Marta, Anna"
print(names.split(","))
print(type(names))
print(str.split(names, ","))
