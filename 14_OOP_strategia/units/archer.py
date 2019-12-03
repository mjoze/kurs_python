from warrior import Warrior


class Archer(Warrior):
    def __init__(self, health):
        super().__init__()
        self.health = health

    def attack(self):
        print("Archer: I released the arrow!")
        self.experience += 0.4

