class UsefullStuff:
    def __init__(self):
        print("I'm useful")


class Watch(UsefullStuff):
    def __init__(self):
        print("I'can check what time is it")


class Phone(UsefullStuff):
    def __init__(self):
        print("I can call")


class Smartwatch(Watch, Phone):
    def __init__(self):
        print("I'm smartwatch")
        super().__init__()


# u = UsefullStuff()
# w = Watch()
# p = Phone()
s = Smartwatch()