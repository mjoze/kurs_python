class Warrior:
    def __init__(self):
        self.experience = 0

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name}: hp:{self.health}, exp={self.experience}"

    def walk(self, distance):
        name = self.__class__.__name__
        print(f"{name}: walked {distance}m")
        self.experience += 0.02 * distance


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60

    def attack(self):
        print("Knight: cut with a sword")
        self.experience += 0.3


class Archer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.arrow = 5

    def attack(self):
        self.arrow -= 1
        if self.arrow < 0:
            print("Archer: no arrows")
            self.arrow = 0
        else:
            print("Archer: I released the arrow!")
            self.experience += 2


def main():
    player = Archer()
    print(player)




if __name__ == '__main__':
    main()

