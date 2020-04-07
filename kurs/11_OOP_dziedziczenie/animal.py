class Vertebrate:
    backbone = True

    def __init__(self):
        print("Szkielet wewnętrzny stanowi podporę")

    def desc(self):
        print("Pierwsze charakterystyczne są dla wszystkich kręgoustych,")


class Cat(Vertebrate):
    def __init__(self, name):
        self.name = name

    def desc(self):
        super().__init__()
        print("Koty są super")


ver = Vertebrate()
kitty = Cat("Kitty")
kitty.desc()
