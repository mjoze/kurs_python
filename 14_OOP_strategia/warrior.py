class Warrior:
    def __init__(self, health):
        self.experience = 0
        self.health = health

    def __repr__(self):
        name = self.__class__.__name__
        if self.health < 0:
            raise Exception("you've been defeated")
        return f"{name}: hp:{self.health}, exp={self.experience}"

    def walk(self, distance):
        name = self.__class__.__name__
        print(f"{name}: walked {distance}m")
        self.experience += 0.02 * distance
