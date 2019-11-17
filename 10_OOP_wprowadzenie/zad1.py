class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def bark(self):
        return "hau " * len(self.name)

    def tail(self):
        return "merdu " * len(self.breed)


obj_azor = Dog("Azor", 'Owczarek', "brown")
print(obj_azor.tail())
print(obj_azor.__dict__)
obj_harry = Dog("Harry", 'Beagle', "brown")
print(obj_harry.tail())
print(obj_harry.__dict__)
print(obj_harry.name)
