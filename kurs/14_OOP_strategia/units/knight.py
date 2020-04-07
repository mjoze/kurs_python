from warrior import Warrior


class Knight(Warrior):
    def __init__(self, health):
        super().__init__()
        self.health = health

    def attack(self):
        print("Knight: cut with a sword")
        self.experience += 0.3

