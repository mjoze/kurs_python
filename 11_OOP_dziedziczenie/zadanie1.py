"""1▹ Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć z nadrzędnej
klasy Ssaki. Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta. Utwórz obiekty klas - kot, pies i człowiek,
udowodnij, że rzeczywiście korzystają z klas rodziców."""


class Animal:
    def __init__(self):
        print("I'm animal")

    def show_description(self):
        print("Animal: Są najbardziej zróżnicowanym gatunkowo królestwem organizmów. ")


class Ssaki(Animal):
    def __init__(self, name):
        self.name = name
        print("ssak " + self.name)

    def show_description(self):
        super().show_description()
        print("Ssak: zwierzęta należące do kręgowców, charakteryzujące się głównie występowaniem"
              " gruczołów mlekowych u samic")


class Cat(Ssaki):
    def __init__(self):
        super().__init__(name="Mruczek")
        print("cat")

    def show_description(self):
        super().show_description()
        print("Kot: to jest kot")


class Dog(Ssaki):
    def __init__(self):
        print("dog")
        # super().__init__()

    def show_description(self):
        super().show_description()
        print("to jest pies")


class Human(Ssaki):
    def __init__(self):
        print("human")
        # super().__init__()

    def show_description(self):
        super().show_description()
        print("to jest czlowiek")


# ssak = Ssaki("Adas")
# ssak.show_description()
kot = Cat()
kot.show_description()
# pies = Dog()
# pies.show_description()
# czlowiek = Human()
# czlowiek.show_description()
